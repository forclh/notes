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
