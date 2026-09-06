import math
from functools import total_ordering


@total_ordering
class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("分母不能为0")

        # 处理负数：统一符号到分子
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # 约分
        g = math.gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (
            self.numerator == other.numerator and self.denominator == other.denominator
        )

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = (
            self.numerator * other.denominator + other.numerator * self.denominator
        )
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = (
            self.numerator * other.denominator - other.numerator * self.denominator
        )
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Fraction(new_num, new_den)

    def __float__(self):
        return self.numerator / self.denominator


f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print(f1 + f2)  # 5/6
print(f1 - f2)  # 1/6
print(f1 * f2)  # 1/6
print(f1 / f2)  # 3/2
print(f1 == f2)  # False
print(f1 > f2)  # True
print(float(f1))  # 0.5
print(str(f1))  # "1/2"
print(repr(f1))  # "Fraction(1, 2)"
