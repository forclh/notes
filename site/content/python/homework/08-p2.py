# 第二题：综合预测题
# 题目：说出下面代码的打印结果


class Animal:
    kingdom = "Animalia"

    def __init__(self, name):
        self.name = name


class Dog(Animal):
    count = 0

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        Dog.count += 1

    def bark(self):
        return f"{self.name} says Woof!"


dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(type(dog1))
print(type(Dog))
print(isinstance(dog1, Animal))
print(isinstance(dog1, (int, Dog)))
print(issubclass(Dog, object))
print(dog1.__class__.__name__)
print(Dog.__base__.__name__)
print(hasattr(dog1, "kingdom"))
print(getattr(dog1, "age"))
print(getattr(dog2, "color", "brown"))
setattr(dog1, "color", "golden")
print(dog1.color)
print("bark" in dir(dog1))
print(vars(dog2))
delattr(dog1, "color")
print(hasattr(dog1, "color"))
print(Dog.count)

# 打印结果：
# <class '__main__.Dog'>
# <class 'type'>
# True
# True
# True
# Dog
# Animal
# True
# 3
# brown
# golden
# True
# {'name': 'Max', 'age': 5}
# False
# 2
