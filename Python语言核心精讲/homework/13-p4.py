def cache(func):
    _cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(35))  # 应该快速返回结果，输出: 9227465
