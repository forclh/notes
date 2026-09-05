# 第一题：实现一个计数器类


class Counter:
    def __init__(self, start):
        self.start = start
        self.value = start

    def __call__(self):
        self.value += 1
        return self.value

    def reset(self):
        self.value = self.start

    def get(self):
        return self.value


# ============ 测试代码 ============

c = Counter(10)
print(c())  # 11
c()  # 12
print(c.get())  # 12
c.reset()
print(c.get())  # 10
