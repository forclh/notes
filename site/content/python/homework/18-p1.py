import time
from contextlib import contextmanager


@contextmanager
def timer(name):
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name} 耗时: {elapsed:.4f} 秒")


# 使用
with timer("数据处理"):
    time.sleep(1)
    print("处理完成")
# 处理完成
# 数据处理 耗时: 1.0012 秒
