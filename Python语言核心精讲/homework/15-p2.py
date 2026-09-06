class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        if value > 1000:
            raise ValueError("温度不能超过1000")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @property
    def kelvin(self):
        return self._celsius + 273.15


t = Temperature(25)
print(t.celsius)  # 25
print(t.fahrenheit)  # 77.0（只读属性，自动计算）
print(t.kelvin)  # 298.15（只读属性，自动计算）

# t.celsius = -300    # ValueError! 温度不能低于绝对零度
