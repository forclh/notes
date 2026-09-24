# 作业四：素数筛选器（参考答案）

# 获取并验证起始数字
while True:
    start = int(input("请输入起始数字："))
    if start <= 0:
        print("输入无效，请输入一个正整数！")
        continue
    break

# 获取并验证结束数字
while True:
    end = int(input("请输入结束数字："))
    if end <= 0:
        print("输入无效，请输入一个正整数！")
        continue
    if end <= start:
        print(f"结束数字必须大于起始数字 {start}，请重新输入！")
        continue
    break

# 输出结果
print(f"\n{start} 到 {end} 之间的素数有：")

# 使用 while 循环遍历范围内的每个数字
num = start
prime_count = 0

while num <= end:
    if num >= 2:
        # 判断 num 是否为素数
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            if prime_count > 0:
                print(" ", end="")
            print(num, end="")
            prime_count += 1

    num += 1

print()
print(f"共计 {prime_count} 个素数")
