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
