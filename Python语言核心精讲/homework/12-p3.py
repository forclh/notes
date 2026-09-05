class LogMeta(type):
    def __new__(mcs, name, bases, namespace):
        for key, value in namespace.items():
            if not key.startswith("_") and callable(value):
                namespace[key] = mcs.log_wrapper(value)
        return super().__new__(mcs, name, bases, namespace)

    @staticmethod
    def log_wrapper(func):
        def wrapper(*args, **kwargs):
            print(f"[LOG] 调用 {func.__name__}")
            r = func(*args, **kwargs)
            return r

        return wrapper


class Calculator(metaclass=LogMeta):
    a = 1

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b


calc = Calculator()
print(calc.add(3, 5))
print(calc.sub(10, 4))

# 应该输出：
# [LOG] 调用 add
# 8
# [LOG] 调用 sub
# 6
