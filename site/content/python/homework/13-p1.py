import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} 执行时间: {elapsed:.4f} 秒")
        return result

    return wrapper


@timer
def slow_function():
    time.sleep(1)
    return "Done"


slow_function()
# 输出：slow_function 执行时间: 1.0012 秒
