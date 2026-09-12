def safe_divide(a, b):
    """
    安全除法
    1. 捕获 ZeroDivisionError，返回 0
    2. 捕获 TypeError，打印"参数类型错误"并返回 None
    """
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("参数类型错误")
        return None


print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # 0
print(safe_divide("10", 2))  # 参数类型错误，None
