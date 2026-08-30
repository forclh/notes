# 作业四答案：闭包计数器


def make_multiplier(n):
    """返回一个将参数乘以 n 的函数"""

    def tri(m):
        return m * n

    return tri


# 测试
triple = make_multiplier(3)
print(triple(5))  # 15
print(triple(10))  # 30

double = make_multiplier(2)
print(double(7))  # 14
