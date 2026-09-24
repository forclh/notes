import time


def retry(max_attempts, delay=1):
    """
    失败重试装饰器
    如果函数抛出异常，等待 delay 秒后重试，最多重试 max_attempts 次
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    time.sleep(delay)

        return wrapper

    return decorator


@retry(max_attempts=3, delay=1)
def unstable_function():
    """模拟不稳定的操作"""
    import random

    if random.random() < 0.7:  # 70% 概率失败
        raise ConnectionError("连接失败")
    return "成功"


# 应该能处理失败并重试，最终返回"成功"或抛出最后一次异常
print(unstable_function())
