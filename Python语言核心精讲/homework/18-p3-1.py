def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_attempts:
                attempt += 1
                try:
                    return func(*args, **kwargs)
                except:
                    if attempt == max_attempts:
                        raise
                    print(f"第{attempt}次失败，重试中...")

        return wrapper

    return decorator


# 使用
attempt_count = 0


@retry(3)
def unstable_function():
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ConnectionError("连接失败")
    return "成功"


print(unstable_function())
