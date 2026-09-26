---
chapter: 15
title: 15 描述符
tags:
  - python
  - 课件
  - 描述符
  - __get__
  - __set__
  - property
  - __set_name__
---
## 问题

```python
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = radius**2 * math.pi
        self.diameter = radius * 2


c = Circle(5)
print(c.radius, c.area, c.diameter)  # 没问题

# 出现问题
# 1. 不符合逻辑的赋值
c.radius = -10

# 2. 数据不一致
c.radius = 10
print(c.radius, c.area, c.diameter)  # 数据不一致
```

## 描述符协议

### 认识术语

描述符协议规定，只要一个类，实现了 `__get__`、`__set__`、`__delete__` 任意一个实例方法：

- 该类称之为**描述符类**
- 该类的对象称之为**描述符对象**，也可以简称为**描述符**
  - 如果描述符类实现了 `__set__`、`__delete__` 任意一个，它的对象又称之为**数据型描述符**（Data Descriptor）
  - 如果描述符类只实现了 `__get__`，它的对象又称为**非数据型描述符**（Non-Data Descriptor）
- 描述符对象只有是**类属性**时才有意义，所以描述符通常又称为**属性描述符**

```python
# 描述符类
class MyDescriptor:
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


class MyClass:
    my_attr = MyDescriptor()  # 描述符、属性描述符、数据描述符
```

### 访问顺序

当访问实例成员时，按照以下优先级查找成员：

1. **数据型描述符**（类属性）
2. 实例属性（`instance.__dict__`）
3. 类属性（普通）
4. 父类...

```python
# 描述符类
class MyDescriptor:
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


class MyClass:
    my_attr = MyDescriptor()  # 描述符、属性描述符、数据描述符

    def __init__(self, value):
        self.my_attr = value  # 赋值的是类属性


ins = MyClass(10)
print(ins.__dict__)  # 不包含 my_attr
print(ins.my_attr)  # 访问的是类属性
```

### 读写删操作

描述符会拦截对它的读、写、删操作：

```python
# 描述符类
class MyDescriptor:
    def __get__(self, instance, owner):
        print("__get__ called")
        pass

    def __set__(self, instance, value):
        print("__set__ called")
        pass

    def __delete__(self, instance):
        print("__delete__ called")
        pass


class MyClass:
    my_attr1 = MyDescriptor()  # 描述符、属性描述符、数据描述符
    my_attr2 = MyDescriptor()  # 描述符、属性描述符、数据描述符


ins = MyClass()
ins.my_attr1  # MyDescriptor.__get__(MyClass.my_attr, ins, MyClass)
ins.my_attr1 = 10  # MyDescriptor.__set__(MyClass.my_attr, ins, 10)
del ins.my_attr1  # MyDescriptor.__delete__(MyClass.my_attr, ins)


MyClass.my_attr2  # MyDescriptor.__get__(MyClass.my_attr, None, MyClass)
MyClass.my_attr2 = 20  # 直接覆盖 my_attr2，my_attr2 不再是描述符了
del MyClass.my_attr2  # 直接删除 my_attr2 属性，my_attr2 不再存在
```

**最佳实践：**

1. 绝大部分时候都使用**数据型描述符**
2. 对描述符的访问，永远通过实例去访问

### 钩子函数

目前，描述符类中仅提供了一个钩子函数 `__set_name__`

> Python3.6 版本加入

```python
# 描述符类
class MyDescriptor:
    def __set_name__(self, owner, name):
        print(f"__set_name__ called with owner={owner}, name={name}")

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


class MyClass:
    # 这里会触发 __set_name__
    # 时间点：完成赋值后
    # 作用：让描述符知道自己被赋值给了哪个类的哪个属性
    my_attr1 = MyDescriptor()
    my_attr2 = MyDescriptor()
```

## 解决最初的问题

```python
import math


class RadiusDescriptor:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("半径不能为负数")
        instance._radius = value

    def __get__(self, instance, owner):
        return instance._radius

    def __delete__(self, instance):
        raise AttributeError("radius 不能被删除")


class AreaDescriptor:

    def __get__(self, instance, owner):
        return instance.radius**2 * math.pi

    def __set__(self, instance, value):
        raise AttributeError("area 是只读属性，不能设置")

    def __delete__(self, instance):
        raise AttributeError("area 不能被删除")


class DiameterDescriptor:

    def __get__(self, instance, owner):
        return instance.radius * 2

    def __set__(self, instance, value):
        raise AttributeError("diameter 是只读属性，不能设置")

    def __delete__(self, instance):
        raise AttributeError("diameter 不能被删除")


class Circle:
    radius = RadiusDescriptor()
    area = AreaDescriptor()
    diameter = DiameterDescriptor()

    def __init__(self, radius):
        self.radius = radius


c1 = Circle(5)  # 没问题
print(c1.radius)  # 输出 5
print(c1.area)  # 输出 78.53981633974483
print(c1.diameter)  # 输出 10
c1.radius = 10  # 没问题
print(c1.radius)  # 输出 10
print(c1.area)  # 输出 314.1592653589793
print(c1.diameter)  # 输出 20

c1.area = 100  # 报错
print(c1.area)
```

---

## @property 装饰器

`@property` 可以将方法变成**属性**，访问时像访问普通属性一样，不需要加括号：

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """获取半径"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """设置半径，带验证"""
        if value < 0:
            raise ValueError("半径不能为负数")
        self._radius = value

    @radius.deleter
    def radius(self):
        """删除半径"""
        print("删除半径")
        del self._radius

    @property
    def area(self):
        """计算面积（只读属性）"""
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        """计算直径（只读属性）"""
        return self._radius * 2


c = Circle(5)
print(c.radius)     # 5 —— 调用 getter
print(c.area)       # 78.54... —— 自动计算
print(c.diameter)   # 10

c.radius = 10       # 调用 setter
print(c.area)       # 314.15...

# c.area = 100      # AttributeError! area 没有 setter
# c.radius = -5     # ValueError! 半径不能为负数

# del c.radius      # 调用 deleter
# print(c.radius)   # AttributeError!
```

**关键点：**

- `@property` 将方法变成**只读属性**
- `@属性名.setter` 定义可写属性（必须和 property 同名）
- `@属性名.deleter` 定义可删除属性

---

### 深入：手写 `@property`

`@property` 本质上就是一个**数据型描述符**。下面用描述符协议手动实现一个等价的 `MyProperty`，帮助理解 `@property` 背后的机制：

```python
import math


class MyProperty:
    def __init__(self, get_func=None, set_func=None, delete_func=None):
        self.get_func = get_func
        self.set_func = set_func
        self.delete_func = delete_func

    def __get__(self, instance, owner):
        if self.get_func is None:
            raise AttributeError("属性不可读")
        return self.get_func(instance)

    def __set__(self, instance, value):
        if self.set_func is None:
            raise AttributeError("属性不可写")
        self.set_func(instance, value)

    def __delete__(self, instance):
        if self.delete_func is None:
            raise AttributeError("属性不可删除")
        self.delete_func(instance)

    def setter(self, func):
        self.set_func = func
        return self

    def deleter(self, func):
        self.delete_func = func
        return self


class Circle:

    @MyProperty
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能是负数")
        self._radius = value

    @radius.deleter
    def radius(self):
        raise AttributeError("不能删除半径属性")

    @MyProperty
    def area(self):
        return math.pi * self.radius**2

    @MyProperty
    def circumference(self):
        return 2 * math.pi * self.radius

    @MyProperty
    def diameter(self):
        return 2 * self.radius

    def __init__(self, radius=5):
        self.radius = radius


c = Circle(5)
print(c.radius, c.area, c.circumference, c.diameter)
c.radius = 10
print(c.radius, c.area, c.circumference, c.diameter)
```

**要点：** `MyProperty` 是一个数据型描述符（实现了 `__set__` / `__delete__`），`@MyProperty` 装饰器把被装饰函数作为 `get_func` 传入；`.setter` / `.deleter` 返回 `self`，从而支持链式叠加。`@property` 的工作方式与此完全一致——它就是一个可配置的数据型描述符。

---

## 应用场景

### 1. 惰性计算

```python
class LazyProperty:
    """惰性加载属性：只在第一次访问时计算"""

    def __init__(self, func):
        # 装饰发生在类定义时：@LazyProperty 等价于 data = LazyProperty(data)
        # func 是被装饰的原函数，name 记录属性名 "data"
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        # instance: 发起访问的实例（如 loader）；通过类访问（DataLoader.data）时为 None
        if instance is None:
            return self
        # 只在第一次访问时真正执行原函数（相当于 self.data(loader)）
        value = self.func(instance)
        # 将结果写入实例字典 loader.__dict__['data']，实现缓存
        setattr(instance, self.name, value)
        return value
        # 缓存能生效的关键：LazyProperty 是"非数据描述符"，属性查找时
        # 实例字典优先级高于非数据描述符。第二次访问直接命中实例字典，
        # __get__ 不再被调用。
        # 注意：不能加 __set__，否则变成数据描述符（优先级高于实例字典），
        # setattr 写入的值会被描述符挡住，缓存失效。


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    @LazyProperty
    def data(self):
        print(f"正在加载文件: {self.file_path}")
        # 模拟耗时操作
        return [1, 2, 3, 4, 5]


loader = DataLoader("data.txt")
print(loader.data)  # 第一次访问：实例字典没有 data，触发 __get__，执行加载
                    # 正在加载文件: data.txt
                    # [1, 2, 3, 4, 5]
print(loader.data)  # 第二次访问：直接命中实例字典缓存，__get__ 不再被调用
                    # [1, 2, 3, 4, 5] —— 不再加载，直接从属性读取
```

### 2. 类型检查

```python
class Typed:
    """强制类型检查的描述符"""

    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} 必须是 {self.expected_type.__name__} 类型，"
                f"而不是 {type(value).__name__}"
            )
        instance.__dict__[self.name] = value


class Student:
    name = Typed(str)
    age = Typed(int)
    score = Typed(float)

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student("Alice", 20, 85.5)
# s.age = "20"      # TypeError! age 必须是 int 类型，而不是 str
```

---

## 作业（可使用 AI）

### 一、实现只读属性

编写一个类 `ImmutablePoint`，创建后不能修改坐标：

```python
p = ImmutablePoint(3, 4)
print(p.x)      # 3
print(p.y)      # 4

# p.x = 10      # AttributeError! 不能修改只读属性
```

**提示：** 使用 `@property` 但不提供 setter。

### 二、实现范围验证

编写一个 `Temperature` 类，温度必须在 -273.15（绝对零度）到 1000 之间：

```python
t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0（只读属性，自动计算）
print(t.kelvin)       # 298.15（只读属性，自动计算）

# t.celsius = -300    # ValueError! 温度不能低于绝对零度
```

### 三、实现类属性计数器

编写一个描述符，记录某个类属性被访问和修改的次数：

```python
class AccessCounter:
    # 你的代码
    pass


class MyClass:
    value = AccessCounter(10)  # 初始值为 10


obj = MyClass()
print(obj.value)      # 10
print(obj.value)      # 10
obj.value = 20
print(obj.value)      # 20

# 查看访问和修改次数
print(AccessCounter.get_access_count())   # 3（被访问了 3 次）
print(AccessCounter.get_modify_count())   # 1（被修改了 1 次）
```

### 四、思考题

下面代码的输出是什么？为什么？

```python
class Descriptor:
    def __get__(self, instance, owner):
        print(f"__get__ called, instance={instance}, owner={owner}")
        return 42

    def __set__(self, instance, value):
        print(f"__set__ called, instance={instance}, value={value}")


class A:
    x = Descriptor()


a = A()
# __get__ called, instance=<__main__.A object at 0x0000018E0E2F86E0>, owner=<class '__main__.A'>
# 42
print(a.x)
# __set__ called, instance=<__main__.A object at 0x0000018E0E2F86E0>, value=100
a.x = 100
a.__dict__["x"] = "instance"
# __get__ called, instance=<__main__.A object at 0x0000018E0E2F86E0>, owner=<class '__main__.A'>
42
print(a.x)
# {'x': 'instance'}
print(a.__dict__)
```

---

## 参考答案

> 第四题为思考题，未提供答案，请结合「访问顺序」一节自行推导。

```python
class ImmutablePoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


p = ImmutablePoint(3, 4)
print(p.x)  # 3
print(p.y)  # 4

# p.x = 10      # AttributeError! 不能修改只读属性
```

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        if value > 1000:
            raise ValueError("温度不能超过1000")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @property
    def kelvin(self):
        return self._celsius + 273.15


t = Temperature(25)
print(t.celsius)  # 25
print(t.fahrenheit)  # 77.0（只读属性，自动计算）
print(t.kelvin)  # 298.15（只读属性，自动计算）

# t.celsius = -300    # ValueError! 温度不能低于绝对零度
```

```python
class AccessCounter:
    _access_count = 0
    _modify_count = 0

    def __init__(self, init_value):
        self._value = init_value

    def __get__(self, instance, owner):
        AccessCounter._access_count += 1
        return self._value

    def __set__(self, instance, value):
        AccessCounter._modify_count += 1
        self._value = value

    @classmethod
    def get_access_count(cls):
        return cls._access_count

    @classmethod
    def get_modify_count(cls):
        return cls._modify_count


class MyClass:
    value = AccessCounter(10)  # 初始值为 10


obj = MyClass()
print(obj.value)  # 10
print(obj.value)  # 10
obj.value = 20
print(obj.value)  # 20

# 查看访问和修改次数
print(AccessCounter.get_access_count())  # 3（被访问了 3 次）
print(AccessCounter.get_modify_count())  # 1（被修改了 1 次）
```
