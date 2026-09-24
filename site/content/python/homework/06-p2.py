# 作业二答案：global 与 nonlocal

count = 0


def outer():
    count = 10

    def inner():
        global count
        count += 1
        print(count)  # 1 —— 修改全局变量，0+1=1

    inner()
    print(count)  # 10 —— outer 的局部变量 count，未被修改


outer()
print(count)  # 1 —— 全局变量被 inner 修改为 1
