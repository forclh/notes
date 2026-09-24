---
chapter: 19
title: 19 ABC（抽象类）
course: Python语言核心精讲
tags:
  - python
  - 课件
  - ABC
  - 抽象类
  - abstractmethod
  - 接口
  - 继承
---
抽象类是**不能被实例化**的类，用于定义子类**必须实现**的接口。Python 通过 `abc` 模块提供抽象类的支持。

```python
from abc import ABC, abstractmethod


class Animal(ABC):  # 继承 ABC，表示这是一个抽象类
    @abstractmethod
    def speak(self):
        """子类必须实现这个方法"""
        pass


# animal = Animal()  # TypeError: 不能实例化抽象类


class Dog(Animal):
    def speak(self):  # 必须实现抽象方法
        print("Woof!")


dog = Dog()
dog.speak()  # Woof!
```

## 定义抽象类

使用 `abc` 模块中的 `ABC` 类和 `@abstractmethod` 装饰器：

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        """计算面积"""
        pass

    @abstractmethod
    def perimeter(self):
        """计算周长"""
        pass

    def describe(self):
        """普通方法，子类可直接使用"""
        print(f"这是一个图形，面积: {self.area()}, 周长: {self.perimeter()}")
```

**要点：**

- 继承 `ABC` 表示这是一个抽象类
- `@abstractmethod` 标记的方法**必须**在子类中实现
- 抽象类可以包含普通方法（有默认实现）
- 抽象类**不能**被实例化

---

## 抽象属性

除了抽象方法，还可以定义抽象属性：

```python
from abc import ABC, abstractmethod


class Employee(ABC):
    @property
    @abstractmethod
    def salary(self):
        """子类必须实现 salary 属性"""
        pass


class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self._monthly_salary = monthly_salary

    @property
    def salary(self):
        return self._monthly_salary


emp = FullTimeEmployee(10000)
print(emp.salary)  # 10000
```

**注意：** `@property` 和 `@abstractmethod` 的顺序**不能颠倒**。

---

## 子类必须实现所有抽象方法

如果子类没有实现所有抽象方法，它仍然是抽象类，不能被实例化：

```python
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    # 忘记实现 perimeter 方法


# rect = Rectangle(3, 4)  # TypeError: 不能实例化抽象类 Rectangle
```

---

## 实际应用场景

抽象类常用于定义**插件接口**或**框架扩展点**：

```python
from abc import ABC, abstractmethod


class DataSource(ABC):
    """数据源抽象基类，所有数据源必须实现这些接口"""

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def close(self):
        pass


class MySQLSource(DataSource):
    def connect(self):
        print("连接 MySQL")

    def read(self):
        return "MySQL 数据"

    def close(self):
        print("关闭 MySQL 连接")


class MongoDBSource(DataSource):
    def connect(self):
        print("连接 MongoDB")

    def read(self):
        return "MongoDB 数据"

    def close(self):
        print("关闭 MongoDB 连接")


def process_data(source: DataSource):
    """统一处理数据，不关心具体数据源"""
    source.connect()
    data = source.read()
    print(f"读取到: {data}")
    source.close()


# 使用不同的数据源
process_data(MySQLSource())
process_data(MongoDBSource())
```

**要点：** `process_data` 只依赖抽象接口，不关心具体实现——新增数据源时只需继承 `DataSource` 并实现三个方法，处理逻辑完全不用改动。

---

## 作业（使用AI）

### 一、实现抽象缓存类

编写一个抽象基类 `Cache`，定义缓存的基本接口，然后实现 `MemoryCache` 和 `FileCache`：

```python
from abc import ABC, abstractmethod


class Cache(ABC):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass


# 实现 MemoryCache（使用字典存储）
# 实现 FileCache（使用文件存储）
```

### 二、实现抽象序列类

编写一个抽象基类 `Sequence`，然后实现 `ListSequence` 和 `LinkedListSequence`：

```python
from abc import ABC, abstractmethod


class Sequence(ABC):
    @abstractmethod
    def append(self, item):
        pass

    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    def is_empty(self):
        return self.length() == 0


# 实现 ListSequence（基于 Python 列表）
# 实现 LinkedListSequence（基于链表）
```

### 三、思考题

下面代码的输出是什么？为什么？

```python
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def foo(self):
        pass

    def bar(self):
        print("A.bar")


class B(A):
    def foo(self):
        print("B.foo")


class C(B):
    pass


c = C()
c.foo()
c.bar()
```

如果改成下面的代码，会发生什么？

```python
class D(A):
    pass


d = D()
```

---

## 参考答案

> 作业源文件位于 `homework/` 目录，下方通过 Obsidian 嵌入直接展示代码。
> 第三题为思考题，答案文件中附有输出分析与原因推导。

```python
import json
import os
from abc import ABC, abstractmethod


class Cache(ABC):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass


class MemoryCache(Cache):
    def __init__(self):
        self._data = {}

    def get(self, key):
        return self._data.get(key)

    def set(self, key, value):
        self._data[key] = value

    def delete(self, key):
        if key in self._data:
            del self._data[key]


class FileCache(Cache):
    def __init__(self, directory="cache"):
        self._directory = directory
        os.makedirs(directory, exist_ok=True)

    def _get_path(self, key):
        return os.path.join(self._directory, f"{key}.json")

    def get(self, key):
        path = self._get_path(key)
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def set(self, key, value):
        path = self._get_path(key)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(value, f)

    def delete(self, key):
        path = self._get_path(key)
        if os.path.exists(path):
            os.remove(path)


# 使用
memory_cache = MemoryCache()
memory_cache.set("name", "Alice")
print(memory_cache.get("name"))  # Alice
memory_cache.delete("name")
print(memory_cache.get("name"))  # None

file_cache = FileCache()
file_cache.set("name", "Bob")
print(file_cache.get("name"))  # Bob
file_cache.delete("name")
print(file_cache.get("name"))  # None
```

```python
from abc import ABC, abstractmethod


class Sequence(ABC):
    @abstractmethod
    def append(self, item):
        pass

    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    def is_empty(self):
        return self.length() == 0


class ListSequence(Sequence):
    def __init__(self):
        self._data = []

    def append(self, item):
        self._data.append(item)

    def get(self, index):
        return self._data[index]

    def length(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListSequence(Sequence):
    def __init__(self):
        self._head = None
        self._size = 0

    def append(self, item):
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        current = self._head
        for _ in range(index):
            current = current.next
        return current.value

    def length(self):
        return self._size

    def __iter__(self):
        current = self._head
        while current:
            yield current.value
            current = current.next


# 使用
list_seq = ListSequence()
list_seq.append(1)
list_seq.append(2)
list_seq.append(3)
print(list_seq.get(1))  # 2
print(list_seq.length())  # 3
print(list(list_seq))  # [1, 2, 3]
print(list_seq.is_empty())  # False

linked_seq = LinkedListSequence()
linked_seq.append("a")
linked_seq.append("b")
linked_seq.append("c")
print(linked_seq.get(1))  # b
print(linked_seq.length())  # 3
print(list(linked_seq))  # ['a', 'b', 'c']
print(linked_seq.is_empty())  # False
```

```python
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def foo(self):
        pass

    def bar(self):
        print("A.bar")


class B(A):
    def foo(self):
        print("B.foo")


class C(B):
    pass


c = C()
c.foo()
c.bar()

# 输出：
# B.foo
# A.bar
#
# 原因：
# - C 继承自 B，B 已经实现了抽象方法 foo，所以 C 不需要再实现。
# - C 没有自己的 foo 和 bar 方法，因此调用时会沿着 MRO 向上查找：
#   - c.foo() -> B.foo() -> 输出 "B.foo"
#   - c.bar() -> A.bar() -> 输出 "A.bar"


# 第二问：
# class D(A):
#     pass
#
# d = D()
#
# 运行结果：TypeError: Can't instantiate abstract class D with abstract method foo
# 原因：D 继承自 A，但没有实现抽象方法 foo，因此 D 仍然是抽象类，不能被实例化。
```
