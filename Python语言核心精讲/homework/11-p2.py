# 第二题：思考题

# 题目：下面代码的输出是什么？为什么？


class A:
    def __call__(self):
        print("A called")


class B(A):
    def __call__(self):
        print("B called")
        super().__call__()


b = B()
b()

# 输出结果：
# B called
# A called

# 原因：
# 1. b() 会调用 B.__call__(b)
# 2. B.__call__ 先打印 "B called"
# 3. 然后通过 super().__call__() 调用父类 A 的 __call__ 方法
# 4. A.__call__ 打印 "A called"
