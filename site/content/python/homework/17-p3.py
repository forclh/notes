def generator():
    print("准备 yield 1")
    yield 1
    print("准备 yield 2")
    yield 2
    print("准备 yield 3")
    yield 3
    print("生成器结束")


g = generator()
print("生成器已创建")
print(next(g))
print("---")
print(next(g))
print("---")
g.close()
print("生成器已关闭")
print(next(g))

# 输出：
# 生成器已创建
# 准备 yield 1
# 1
# ---
# 准备 yield 2
# 2
# ---
# 生成器已关闭
# StopIteration 异常

# 原因：
# 1. `g = generator()` 只是创建生成器对象，不会执行函数体，因此先打印"生成器已创建"
# 2. `next(g)` 启动生成器，执行到第一个 yield，打印"准备 yield 1"并返回 1
# 3. 第二次 `next(g)` 从上次暂停处继续，打印"准备 yield 2"并返回 2
# 4. `g.close()` 关闭生成器，在暂停处抛出 GeneratorExit 异常，生成器终止
# 5. `print("生成器已关闭")` 正常执行
# 6. 再次 `next(g)` 时，由于生成器已关闭，会抛出 StopIteration 异常
