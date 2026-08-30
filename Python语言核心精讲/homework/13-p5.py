def to_dict(cls):
    def to_dict_method(self):
        return self.__dict__

    cls.to_dict = to_dict_method
    return cls


@to_dict
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(3, 4)
print(p.to_dict())  # 输出: {'x': 3, 'y': 4}
