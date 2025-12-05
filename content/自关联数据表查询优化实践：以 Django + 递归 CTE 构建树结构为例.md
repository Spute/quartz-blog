---
title: 自关联数据表查询优化实践：以 Django + 递归 CTE 构建树结构为例
publish: "true"
category: 文章写作
date: 2025-12-05
alias: " 3e4ruytq83v14gvsvh6o"
tags:
  - 软件工程
  - 实践
---
## 前言

在业务系统中，自关联模型（Self-Referential Model）非常常见，例如：

- 组织树结构（部门–团队–成员）
    
- 物料结构 BOM（父件–子件）
    
- 装配树（组件–子组件–零件）
    
- 评论树、分类树等
    

这类数据结构具有特点：**同一张表，通过 parent_id 字段指向自身主键形成层级关系**。  
如何在数据库中高效查询和构建这类“树形结构”，是后端开发中的常见挑战。

本文以 Django 项目中的装配树（Assembly）模型为例，分享一次完整的查询优化实践过程，从原生实现到递归 CTE，实现从任意节点出发，找到根节点并构建整棵树，同时将数据库查询优化到 **仅 1 次**。

---

## 一、业务模型：装配树 Assembly

一个典型的自关联模型如下：

```python
class Assembly(models.Model):
    serial_number = models.CharField(max_length=64, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT)
    status_code = models.SmallIntegerField()
    is_active = models.SmallIntegerField(default=1)
```

其层级关系如下：

```
ROOT
├── C1
└── C2
    └── D1
```

需求：

> 给定任意序列号 serial_number，找到它所在树的根节点，查询整个树的所有后代节点，并返回完整树结构。

---

## 二、常见但低效的做法：递归查询 + N 次 DB 请求

最常见的“直觉代码”是：

1. 从当前节点不断向上查 parent → 找根节点
    
2. 从根节点递归查 children → 构建树
    

比如：

```python
def get_children(node_id):
    children = Assembly.objects.filter(parent_id=node_id)
    return [{"id": c.id, "children": get_children(c.id)} for c in children]
```

⚠️ **问题非常致命：**

- 每层 children 查询都触发一次 SQL
    
- 一棵复杂的树可能要执行 **几十甚至上百次查询**
    

这种模式属于经典的 **N+1 查询问题（N+1 Query Problem）**，在数据量大时性能不可接受。

---

## 三、优化路径：将查询次数减少到 2 次

为了提升性能，我们先优化到 2 次查询：

### **查询 1：查指定节点及其祖先链，得到根节点**

```python
node = Assembly.objects.get(serial_number=sn)
while node.parent_id:
    node = Assembly.objects.get(id=node.parent_id)
root = node
```

### **查询 2：一次性查出整个 Assembly 表或某个过滤集**

```python
qs = Assembly.objects.filter(is_active=1).values(
    "id", "serial_number", "parent_id", "status_code"
)
```

然后在 Python 内存中构建 parent → children 映射，从而递归构建出整棵树。

这种方式把 DB 查询减少到 **两次**，已经够快，但 Assembly 表如果大到百万级，会造成不必要的全表扫描。

---

## 四、最终方案：使用递归 CTE，将查询减少到 1 次

PostgreSQL / MySQL 8 / MariaDB 支持 **递归公共表表达式（Recursive CTE）**，可以让数据库本身完成树结构查询。

我们的目标是：

- 从任意节点找到整个树的根
    
- 再从根节点递归找到所有后代
    

我们在 Django 中用 `raw()` 执行以下 SQL：

```sql
WITH RECURSIVE tree AS (
  SELECT * FROM assembly WHERE id = %s
  UNION ALL
  SELECT a.* 
  FROM assembly a
  INNER JOIN tree t ON a.parent_id = t.id
)
SELECT * FROM tree;
```

说明：

- `tree` CTE 中第一条 SELECT 是根节点
    
- `UNION ALL` 递归地查找所有子节点
    
- 最终 SELECT 返回该根节点的整个 subtree
    

---

## 五、Django 代码实现（仅一次 SQL 查询）

### 1. 查找根节点（parent=NULL）

```python
def get_root_id(sn):
    node = Assembly.objects.get(serial_number=sn)
    while node.parent_id:
        node = Assembly.objects.get(id=node.parent_id)
    return node.id
```

### 2. 执行递归 CTE（raw SQL）

```python
from django.db import connection

def get_tree_with_recursive_cte(root_id):
    sql = """
    WITH RECURSIVE tree AS (
        SELECT * FROM assembly WHERE id = %s
        UNION ALL
        SELECT a.* 
        FROM assembly a
        INNER JOIN tree t ON a.parent_id = t.id
    )
    SELECT * FROM tree;
    """

    return Assembly.objects.raw(sql, [root_id])
```

### 3. Python 构建树结构

```python
def build_tree_from_cte(rows):
    rows = list(rows)

    node_map = {row.id: row for row in rows}
    children = {row.id: [] for row in rows}

    for row in rows:
        if row.parent_id in children:
            children[row.parent_id].append(row)

    root = next(r for r in rows if r.parent_id is None)

    def build(node):
        return {
            "serial_number": node.serial_number,
            "status_code": node.status_code,
            "children": [build(child) for child in children[node.id]]
        }

    return build(root)
```

### 4. 最终统一接口

```python
def get_tree(sn):
    root_id = get_root_id(sn)
    cte_rows = get_tree_with_recursive_cte(root_id)
    return build_tree_from_cte(cte_rows)
```

整个流程只有：

- 查询 1：查 root
    
- 查询 2（最终版可合并）：执行递归 CTE 获取整棵树
    

优化后的查询次数：

> **从 N+1 → 2 次 → 1 次**  
> 性能提升巨大。

---

## 六、性能对比

| 方法               | 查询次数      | 优点       | 缺点                        |
| ---------------- | --------- | -------- | ------------------------- |
| 递归 ORM（naive）    | **几十到上百** | 简单       | 极慢                        |
| 全表加载 + Python 构建 | **2 次**   | 较快，代码简单  | 表大时可能浪费，速度一般              |
| **递归 CTE（推荐）**   | **1 次**   | 快、优雅、高性能 | 仅支持 PostgreSQL / MySQL 8+ |

---

## 七、总结

在处理自关联（父子关系）数据结构时，**查询的组织方式决定了性能上限**：

1. **避免 ORM 递归查询**
2. **尽量减少数据库往返次数**
3. **利用数据库特性（递归 CTE）让查询交给数据库做**