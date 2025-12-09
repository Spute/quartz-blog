---
title: 使用SimpleNamespace优雅快速地创建对象
publish: "true"
category: 文章写作
date: 2025-12-08
alias: " 3mit4qajs6bx0kv61vsg"
tags:
  - 软件工程
  - python
---
## 前言

在写 Python 时，我们经常需要创建一个带有属性的对象。  
比如 Django 测试时快速伪造一个 `request` 对象、函数临时传参、构建简易配置对象等。
常规的方案是写一个 class，可是太麻烦。更优雅的解决方案是使用 `types.SimpleNamespace` 。

---

## **什么是 SimpleNamespace？**

`SimpleNamespace` 是 Python 标准库 `types` 模块中的一个轻量级对象，它允许你像字典一样存储键值，又可以像对象一样通过点号访问属性。

可以把它理解为：一个可以随意加属性、删属性的“动态对象”，本质上就是更好用的字典。

---

## **使用场景**

### **1. 快速构造模拟对象（Mock Object）**

例如写单元测试需要一个“类似 request 的对象”，但不想写完整类：

```python
from types import SimpleNamespace

request = SimpleNamespace(
    data={"name": "Tom"},
    user_info={"role": "admin"}
)
```

简单、直观，而且和访问正规对象属性的体验一致。

---

### **2. 动态组装数据结构**

用来临时组合一组参数，比写 class 更省力：

```python
options = SimpleNamespace(debug=True, version="1.0")
print(options.version)
```

---

### **3. 替代字典，使代码更易读**

与其：

```python
config["timeout"]
```

不如：

```python
config.timeout
```

阅读体验明显更好。

---

### **4. 从字典快速转成对象**

```python
payload = {"a": 1, "b": 2}
obj = SimpleNamespace(**payload)
print(obj.a)
```

---

## **核心用法**

### **1. 创建对象**

```python
from types import SimpleNamespace

ns = SimpleNamespace(x=10, y=20)
```

---

### **2. 动态添加属性**

```python
ns.z = 30
```

---

### **3. 转回字典**

```python
vars(ns)
# 或
ns.__dict__
```

---

### **4. 打印更友好**

`SimpleNamespace` 的 `__repr__` 非常简洁：

```python
print(ns)
# SimpleNamespace(x=10, y=20, z=30)
```

---

## **总结**

`SimpleNamespace` 是一个**轻便、可读、灵活**的小工具，非常适合：

- Mock 对象（尤其是测试场景）
    
- 快速传参
    
- 轻量数据结构
    
- 替代简单类或字典

