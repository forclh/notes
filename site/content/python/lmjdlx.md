---
chapter: 18
title: 上下文管理器
course: Python语言核心精讲
tags:
  - python
  - 课件
  - 上下文管理器
  - with
  - __enter__
  - __exit__
  - contextmanager
  - contextlib
---

# 上下文管理器

## with 语句的执行流程

```python
with 表达式 as 变量名:
    代码块

# 等效于
变量名 = 表达式.__enter__()
try:
    代码块
except Exception as e:
    stopPropagation = 变量名.__exit__(type(e), e, e.__traceback__)
    if not stopPropagation:
        raise
else:
    变量名.__exit__(None, None, None)
```

带 `__enter__` 和 `__exit__` 方法的对象叫做**上下文管理器（Context Manager）**。

- **上下文管理器**是支持 `with` 语句的对象
- **必须同时实现**两个方法，否则 `with` 会报错

## 基本用法

```python
# 文件操作 —— 自动关闭文件
with open("data.txt", "r") as f:
    content = f.read()
    # 离开 with 块时，文件自动关闭

# 等价于
f = open("data.txt", "r")
try:
    content = f.read()
except Exception as e:
    stopPropagation = f.__exit__(type(e), e, e.__traceback__)
    if not stopPropagation:
        raise
else:
    f.__exit__(None, None, None)
```

## 自定义上下文管理器

实现 `__enter__` 和 `__exit__` 方法：

```python
class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        self.connected = False

    def __enter__(self):
        """进入 with 块时调用，返回的对象赋值给 as 后的变量"""
        print(f"连接到数据库: {self.host}")
        self.connected = True
        return self  # 返回自身，供 with 块使用

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        离开 with 块时调用
        exc_type: 异常类型（无异常时为 None）
        exc_val: 异常值
        exc_tb: 异常追踪信息
        返回 True 表示异常已处理，不再向上传播
        """
        print(f"关闭数据库连接: {self.host}")
        self.connected = False
        return False  # 返回 False，不处理异常，让异常继续传播

    def query(self, sql):
        if not self.connected:
            raise RuntimeError("未连接到数据库")
        print(f"执行查询: {sql}")
        return ["result1", "result2"]


# 使用上下文管理器
with DatabaseConnection("localhost") as conn:
    print(f"连接状态: {conn.connected}")  # True
    results = conn.query("SELECT * FROM users")
    print(results)

# 离开 with 块后
print(f"连接状态: {conn.connected}")  # False
```

**要点：**

- `__enter__` 的返回值会赋给 `as` 后的变量，通常返回 `self`
- `__exit__` 返回 `True` 表示异常已被处理（抑制），返回 `False`/`None` 表示异常继续向上传播
- 无论 with 块是否抛出异常，`__exit__` 都会被调用，适合做资源清理

## 异常处理

`__exit__` 方法可以处理或记录异常：

```python
class SuppressError:
    """忽略指定类型的异常"""

    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, self.exception_types):
            print(f"捕获并忽略异常: {exc_type.__name__}: {exc_val}")
            return True  # 返回 True，异常被处理，不再传播
        return False  # 不处理其他异常


# 使用
with SuppressError(ZeroDivisionError):
    result = 1 / 0  # 不会报错
    print("这行不会执行")

print("程序继续执行")  # 正常执行
```

---

## 使用 @contextmanager 装饰器

对于简单的上下文管理器，可以使用 `contextlib` 模块的 `@contextmanager` 装饰器，用生成器函数实现：

```python
from contextlib import contextmanager


@contextmanager
def managed_resource(name):
    """用生成器实现上下文管理器"""
    print(f"获取资源: {name}")
    resource = {"name": name, "status": "active"}
    try:
        yield resource  # yield 之前的代码等价于 __enter__
    finally:
        print(f"释放资源: {name}")  # yield 之后的代码等价于 __exit__


# 使用
with managed_resource("database") as res:
    print(f"使用资源: {res}")
# 获取资源: database
# 使用资源: {'name': 'database', 'status': 'active'}
# 释放资源: database
```

**带异常处理的版本：**

```python
from contextlib import contextmanager


@contextmanager
def safe_file_write(file_path):
    """安全写入文件：先写入临时文件，成功后再替换原文件"""
    temp_path = file_path + ".tmp"
    try:
        f = open(temp_path, "w")
        yield f
        f.close()
        # 写入成功，替换原文件
        import os
        os.replace(temp_path, file_path)
        print("写入成功")
    except Exception as e:
        # 写入失败，清理临时文件
        f.close()
        import os
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print(f"写入失败: {e}")
        raise  # 重新抛出异常


# 使用
with safe_file_write("data.txt") as f:
    f.write("Hello, World!\n")
```

**要点：** `yield` 之前的代码等价于 `__enter__`，`yield` 之后的代码（通常在 `finally` 中）等价于 `__exit__`；`yield` 的值就是 `as` 后变量接收的对象。

---

## 多个上下文管理器

可以同时使用多个 `with`：

```python
# 嵌套写法
with open("input.txt", "r") as fin:
    with open("output.txt", "w") as fout:
        fout.write(fin.read().upper())

# 简化写法（Python 3.1+）
with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
    fout.write(fin.read().upper())
```

---

## 作业（使用AI）

### 一、实现代码块计时

```python
from contextlib import contextmanager

# 使用
with timer("数据处理"):
    import time
    time.sleep(1)
    print("处理完成")
# 处理完成
# 数据处理 耗时: 1.0012 秒
```

### 二、实现上下文管理器

编写一个 `TempDirectory` 上下文管理器，进入时创建临时目录，退出时自动删除：

```python
with TempDirectory() as tmp_dir:
    print(f"临时目录: {tmp_dir}")
    # 可以在这个目录中创建文件
    # 离开 with 块时，目录及其内容自动删除

print("临时目录已清理")
```

**提示：** 使用 `tempfile` 模块创建临时目录，使用 `shutil.rmtree` 删除目录。

### ~~三、实现重试装饰器（结合上下文管理器思想）~~

~~编写一个上下文管理器 `retry`，在发生指定异常时自动重试：~~

==这道题有问题，上下文管理器无法实现retry功能，retry需要使用装饰器实现，见参考答案中的 `18-p3.py` 与 `18-p3-1.py`==

### 四、思考题

下面代码的输出是什么？为什么？

```python
from contextlib import contextmanager


@contextmanager
def demo():
    print("进入")
    yield
    print("正常退出")


with demo():
    print("执行中")
    raise ValueError("出错了")
    print("这行不会执行")
```

如果改成下面的代码，输出会有什么不同？

```python
@contextmanager
def demo():
    print("进入")
    try:
        yield
    except Exception as e:
        print(f"捕获异常: {e}")
    finally:
        print("清理")


with demo():
    print("执行中")
    raise ValueError("出错了")
```

---

## 参考答案

> 作业源文件位于 `homework/` 目录，下方通过 Obsidian 嵌入直接展示代码。
> 第三题原题设计有误：上下文管理器无法实现 retry（上下文只能进入一次），`18-p3.py` 解释了原因，`18-p3-1.py` 给出装饰器版的正确实现。
> 第四题为思考题，未提供答案文件，请结合「with 语句的执行流程」与「@contextmanager」两节自行推导。

```python
import time
from contextlib import contextmanager


@contextmanager
def timer(name):
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name} 耗时: {elapsed:.4f} 秒")


# 使用
with timer("数据处理"):
    time.sleep(1)
    print("处理完成")
# 处理完成
# 数据处理 耗时: 1.0012 秒
```

```python
import os
import shutil
import tempfile
import time


class TempDirectory:
    def __enter__(self):
        self.path = tempfile.mkdtemp()
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(self.path)
        return False


# 使用
with TempDirectory() as tmp_dir:
    print(f"临时目录: {tmp_dir}")
    # 可以在这个目录中创建文件
    with open(os.path.join(tmp_dir, "test.txt"), "w") as f:
        f.write("hello")
        time.sleep(1)
    # 离开 with 块时，目录及其内容自动删除

print("临时目录已清理")
```

```python
# 以下代码无法正确运行！！！！
# 因为上下文只能进入一次，使用上下文实现retry不是一个合适的选择，更合适的选择是使用装饰器，参考 p3-1.py
# 很抱歉，这道题出的有毛病


# from contextlib import contextmanager


# @contextmanager
# def retry(max_attempts=3, exceptions=(Exception,)):
#     attempt = 0
#     while attempt < max_attempts:
#         try:
#             yield
#             return  # 成功，直接返回
#         except exceptions as e:
#             attempt += 1
#             if attempt >= max_attempts:
#                 raise  # 超过最大重试次数，重新抛出异常
#             print(f"第 {attempt} 次尝试失败: {e}，准备重试...")


# # 使用
# attempt_count = 0


# def unstable_function():
#     global attempt_count
#     attempt_count += 1
#     if attempt_count < 3:
#         raise ConnectionError("连接失败")
#     return "成功"


# with retry(max_attempts=3, exceptions=(ConnectionError,)):
#     result = unstable_function()
#     print(result)  # 成功（前两次失败自动重试）
```

```python
def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_attempts:
                attempt += 1
                try:
                    return func(*args, **kwargs)
                except:
                    if attempt == max_attempts:
                        raise
                    print(f"第{attempt}次失败，重试中...")

        return wrapper

    return decorator


# 使用
attempt_count = 0


@retry(3)
def unstable_function():
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ConnectionError("连接失败")
    return "成功"


print(unstable_function())
```
