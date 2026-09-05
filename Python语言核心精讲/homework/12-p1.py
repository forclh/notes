class SingletonMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instance:
            ins = super().__call__(*args, **kwds)
            cls._instance[cls] = ins
        return cls._instance[cls]

    pass


class Database(metaclass=SingletonMeta):
    def __init__(self, host):
        self.host = host


db1 = Database("localhost")
db2 = Database("remote")
print(db1 is db2)  # 应该输出 True
print(db1.host)  # 应该输出 localhost


class Player(metaclass=SingletonMeta):
    pass


p1 = Player()
p2 = Player()

print(p1 is p2)
