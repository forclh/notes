def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            t = n
            while t > 0:
                func(*args, **kwargs)
                t -= 1

        return wrapper

    return decorator


@repeat(3)
def say_hello(s):
    print(s)


say_hello(1)  # 输出: 1 1 1
