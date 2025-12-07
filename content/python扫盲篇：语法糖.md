---
title: python扫盲篇：语法糖
publish: "true"
category: 文章写作
date: 2025-12-07
alias: " il955rvy03e6a04fakp3"
tags:
  - 软件工程
  - python
---
# 前言
- 简洁是python的一大特点，所以才会有“**人生苦短，我用python**”。作为动态语言的python相对于静态语言（如：java、go），支持更丰富的语法糖。
- 语法糖是python代码简洁的一个重要原因。因此了解python语法糖很有必要。
- 一方面可以看懂他人写得语法糖代码，另一方面可以使用语法糖，编写功能相同，但更加简洁的代码。
# 语法糖是什么？
是一种代码编写的简便方法，同时又不改变代码的功能。
# 常用的语法糖
以下是 Python 中常见的一些语法糖：

1. **列表推导式**（List Comprehensions）：一种用于创建列表的简洁语法。例如：
   ```python
   squares = [x**2 for x in range(10)]
   ```

2. **字典推导式**（Dictionary Comprehensions）：一种用于创建字典的简洁语法。例如：
   ```python
   squares_dict = {x: x**2 for x in range(10)}
   ```

3. **集合推导式**（Set Comprehensions）：一种用于创建集合的简洁语法。例如：
   ```python
   squares_set = {x**2 for x in range(10)}
   ```

4. **生成器表达式**（Generator Expressions）：类似于列表推导式，但是返回一个生成器对象而不是列表。例如：
   ```python
   squares_generator = (x**2 for x in range(10))
   ```

5. **条件表达式**（Conditional Expressions）：也称为三元运算符，一种简洁的条件语句。例如：
   ```python
   x = 10
   result = "positive" if x > 0 else "negative"
   ```

6. **with 语句**：用于简化资源管理的语法糖，可以自动释放资源。例如：
   ```python
   with open('file.txt', 'r') as f:
       data = f.read()
   ```

7. **@decorator语法糖**：用于简化装饰器的使用。例如：
   ```python
   @decorator
   def func():
       pass
   ```

8. **f-string 格式化字符串**：一种用于格式化字符串的简洁语法。例如：
   ```python
   name = "Alice"
   age = 30
   print(f"My name is {name} and I am {age} years old.")
   ```

# 特点
- 使用语法糖后，代码变得简单、易读。
- 总有与语法糖的代码等效的普通代码。

## 等效代码
- 语法糖所代表的功能可以通过等效的普通代码来实现。语法糖的存在主要是为了让代码更加简洁、易读和优雅，而不是引入新的功能。
- 了解语法糖的等效代码有助于理解语法糖的工作原理。
- 下面是一些常见的语法糖及其等效的普通代码示例：

1. **列表推导式**：
   ```python
   # 语法糖
   squares = [x**2 for x in range(10)]

   # 等效的普通代码
   squares = []
   for x in range(10):
       squares.append(x**2)
   ```

2. **条件表达式**：
   ```python
   # 语法糖
   result = "positive" if x > 0 else "negative"

   # 等效的普通代码
   if x > 0:
       result = "positive"
   else:
       result = "negative"
   ```

3. **with 语句**：
   ```python
   # 语法糖
   with open('file.txt', 'r') as f:
       data = f.read()

   # 等效的普通代码
   f = open('file.txt', 'r')
   try:
       data = f.read()
   finally:
       f.close()
   ```

4. **装饰器**
```python
# 装饰器定义
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# 装饰器使用
@my_decorator
def say_hello1():
    print("Hello!")
  
# 等效的普通代码
def say_hello():
    print("Hello!")

>>>say_hello = my_decorator(say_hello)
>>>say_hello()
Something is happening before the function is called.
Hello!
Something is happening after the function is called.

>>>say_hello1()
Something is happening before the function is called.
Hello!
Something is happening after the function is called.

```
# 语法糖与魔法方法有啥关联吗？

虽然特殊方法和语法糖是两个不同的概念，但在某些情况下它们会有交叉的应用。例如，Python 中的  **@property** 装饰器就是一种语法糖，用于将类中的方法转换为属性访问，而它的实现则涉及到特殊方法 **get**、 **__set__**  和 **delete**。