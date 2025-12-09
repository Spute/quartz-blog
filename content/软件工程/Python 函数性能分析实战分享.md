---
title: Python 函数性能分析实战分享
publish: "true"
category: 文章写作
date: 2025-12-08
alias: " 44rna4lbhivf1eu5b4oh"
tags:
  - 软件工程
  - python
---
## 前言 

在日常开发中，我们经常会遇到接口或函数响应慢的问题。简单的可以使用print打印执行时间，但是在复杂业务系统中，单次请求可能触发几十甚至上百次函数调用。要想精准找出性能瓶颈，**函数性能分析**就显得非常重要。
本文将结合实际案例，分享一种简单可行的 Python 性能分析方案。

---
## 工具选择

Python 内置的 `cProfile` 模块，是分析函数性能的利器：

- **轻量级**：无需额外安装第三方库
    
- **精确**：统计每个函数的调用次数和耗时
    
- **可扩展**：可配合 `pstats`、`io` 输出分析结果

结合 `functools.wraps`，我们可以写一个装饰器，对目标函数进行性能分析，而不影响原有逻辑。

---

## 性能分析装饰器实现

下面是一个实用的装饰器示例：

```python
import cProfile, pstats, io, os
from functools import wraps

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def profile_func(func):
    """
    用于装饰函数，对其进行性能分析
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()

        result = func(*args, **kwargs)

        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats("cumtime")

        # 只打印项目目录下执行的代码行（过滤掉第三方包）
        ps.print_stats(PROJECT_ROOT)

        print("\n===== Profile Output =====")
        print(s.getvalue())
        print("===== End Profile Output =====\n")

        return result
    return wrapper
```

使用方法：

```python
@profile_func
def install(request):
    # 业务逻辑
    ...
```
或者直接在console调用：
```
profile_func(install)(request)
```
调用 `install` 函数后，控制台会输出性能分析报告。

---

## 四、分析报告解读

示例输出：

```text
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1    0.000    0.000    7.112    7.112 /views.py:2553(install)
1    0.000    0.000    5.334    5.334 /models.py:243(update_wib_status_by_sn)
20/1 0.001    0.000    5.015    5.015 /models.py:271(get_wib_sn)
22    0.001    0.000    3.956    0.180 /models.py:2556(belong_to_product_type)
12731 0.006    0.000    0.022    0.000 /models.py:2538(regex_match)
```

### 关键字段解释

| 列名                          | 含义                              |
| --------------------------- | ------------------------------- |
| `ncalls`                    | 函数被调用次数，`20/1` 表示函数内部循环调用了 20 次 |
| `tottime`                   | 函数自身执行时间（不含子函数调用）               |
| `percall`                   | 自身耗时的平均值(tottime/ncalls)        |
| `cumtime`                   | 函数累积耗时（包含子函数调用）                 |
| `percall`                   | 累积耗时平均值 (cumtime/ncalls)        |
| `filename:lineno(function)` | 函数所在文件和行号                       |

### 如何定位瓶颈

1. **cumtime 高** → 优先优化。示例：`update_wib_status_by_sn` 5.334s
        
2. **调用次数高但耗时低** → 可以暂时忽略。示例：`regex_match` 调用 12731 次，总耗时 0.022s
        
3. **循环/递归调用导致累积耗时高** → 可考虑批量处理或缓存。示例：`get_wib_sn` 被调用 20 次，总耗时 5s
    
---
## 总结

性能分析不仅是解决慢接口的手段，也是提升代码质量的必备技能。掌握了分析方法，你就能**精准定位问题，做到有的放矢地优化**。