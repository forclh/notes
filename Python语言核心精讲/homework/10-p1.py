# 作业一答案：单例模式
# 通过重写 __new__，确保一个类只存在一个实例


class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, dsn="default"):
        # __new__ 返回已存在的实例时，__init__ 仍会被调用
        # 如需避免重复初始化，可增加初始化守卫
        if getattr(self, "_initialized", False):
            return
        self.dsn = dsn
        self._initialized = True


# 测试
conn1 = Database("prod")
conn2 = Database("dev")

print(conn1 is conn2)  # True，说明是同一个实例
print(conn1.dsn)  # prod，第一次初始化的值被保留
print(conn2.dsn)  # prod
