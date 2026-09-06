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
