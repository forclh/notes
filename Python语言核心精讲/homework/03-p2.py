# 作业二答案

# 1. while 循环 + if-else
n = 1
result = 0
while n <= 5:
    if n % 2 == 0:
        result += n
    else:
        result -= n
    n += 1
print(result)  # -3

# 2. continue 和 break
num = 1
while num <= 10:
    if num == 3:
        num += 1
        continue
    if num == 7:
        break
    print(num)  # 1, 2, 4, 5, 6
    num += 1

# 3. 循环 else 子句
i = 0
while i < 3:
    print(i)  # 0, 1, 2
    i += 1
else:
    print("end")  # end

# 4. 嵌套条件
x = 15
if x < 10:
    print("A")
elif x < 20:
    if x % 2 == 0:
        print("B")
    else:
        print("C")  # C
else:
    print("D")

# 5. 综合练习
a = 1
b = 0
while a <= 5:
    if a == 3:
        b += 10
    elif a % 2 == 0:
        b += a * 2
    else:
        b += a
    a += 1
print(b)  # 28
