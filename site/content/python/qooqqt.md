---
chapter: 24
title: 24 事件循环
tags:
  - python
  - 课件
  - 异步
  - 事件循环
  - asyncio
  - call_soon
---
## 同步代码的问题

```python
import requests

def task1():
  # 任务1
  requests.post(...) # 发送请求，阻塞线程

def task2():
  # 任务2
  pass

task1()	# task1的阻塞导致后续任务白白等待，浪费了CPU资源
task2()
```

## 什么是异步

异步是一种编程模式，当有多个任务需要在**一个线程**上执行时，这种模式可以让任务不会造成线程阻塞

![async_vs_sync](https://resource.duyiedu.com/yuanjin/202605271757205.svg)

## 异步 VS 多线程

运算密集型：多线程

I/O密集型：异步

## Python的事件循环

事件循环是实现异步的基础手段

### AbstractEventLoop类

在`python`中，一个事件循环就是一个`AbstractEventLoop`类的对象

```python
import asyncio

# 创建一个新的事件循环对象
loop = asyncio.new_event_loop()

# 绑定事件循环到当前线程
asyncio.set_event_loop(loop)

# 获取当前线程的事件循环
current_loop = asyncio.get_event_loop()

print("当前事件循环:", current_loop)

# 移除事件循环绑定
asyncio.set_event_loop(None)

# 运行事件循环
# 陷入死循环，除非在循环中终止，否则后续代码永远无法得到运行
current_loop.run_forever()

# 停止事件循环
current_loop.stop()
```

### run_forever方法

```python
def run_forever(self):
    """Run until stop() is called."""
    while True:
        self._run_once()
        if self._stopping:
            break
```

### \_run\_once逻辑

`_run_once`方法的核心，就是调度事件循环中的队列

它要确保每次该方法运行，都能保证ready队列中的所有回调得到执行

![队列.excalidraw](https://resource.duyiedu.com/yuanjin/202605271642589.svg)

> 1. 检查延时队列，加入ready
> 2. 计算等待时间 timeout
>    1. ready有东西，timeout = 0
>    2. 延时队列还有任务，timeout = 延时队列的队首 - 当前时间
>    3. 都没有任务，timeout = None
> 3. 用timeout的时间阻塞线程，等待I/O，期间有任何IO任务到达，马上加入ready
>    1. 如果timeout时间到达后还没有I/O任务，则重新处理一次延时队列
> 4. 复制ready队列
> 5. 执行复制的队列

试一试下面的代码

```python
import inspect
import asyncio

loop = asyncio.new_event_loop()


# 将函数直接放入ready队列
def my_ready_callback():
    print("这是一个直接进入ready队列的回调函数")


loop.call_soon(my_ready_callback)


# 将函数放入延迟队列，1秒后进入ready队列
def my_scheduled_callback():
    print("这是一个延迟1秒后进入ready队列的回调函数")
    loop.stop()  # 停止事件循环


loop.call_later(1, my_scheduled_callback)

loop.run_forever()

print("事件循环已停止")

```

## 作业（可使用AI）

### 一、预测以下代码的输出结果

```python
import asyncio

loop = asyncio.new_event_loop()


def task1():
    print("任务1")


def task2():
    print("任务2")


def task3():
    print("任务3")


loop.call_soon(task1)
print("task1 over")
loop.call_soon(task2)
print("task2 over")
loop.call_soon(task3)
print("task3 over")

loop.run_forever()
print("已结束")
```

### 二、预测以下代码的输出结果

```python
import asyncio

loop = asyncio.new_event_loop()


def delayed():
    print(1)
    loop.call_later(0, lambda: print(2))
    loop.call_soon(lambda: print(3))


def soon():
    print(4)
    loop.call_soon(lambda: print(5))


loop.call_later(0, delayed)
loop.call_soon(soon)


loop.run_forever()
print("done")

```

### 三、预测以下代码的输出结果

```python
import asyncio

loop = asyncio.new_event_loop()


def first():
    print(1)


def second():
    print(2)
    loop.call_soon(lambda: print(3))
    loop.stop()


def third():
    print(4)


loop.call_soon(first)
loop.call_soon(second)
loop.call_soon(third)

loop.run_forever()
print("循环已停止")

```

## 参考答案

> 三题共用同一套调度模型：`call_soon` 把回调放入 ready 队列，`call_later` 放入延时队列；每轮 `_run_once` 先把到期的延时任务移入 ready，再**整体执行本轮 ready 队列的快照**（执行期间新入队的回调要等下一轮）；`run_forever` 每轮结束检查 `_stopping` 标记决定是否退出。

### 一

输出：

```
task1 over
task2 over
task3 over
任务1
任务2
任务3
已结束
```

要点：`call_soon` 只是把回调**放入队列**，不会立刻执行。所以三行 `print("taskX over")` 作为同步代码先全部执行完，`run_forever` 启动后才按入队顺序执行 `任务1~任务3`，最后打印 `已结束`。

### 二

输出：

```
4
1
3
5
2
```

之后程序**挂起**——`done` 永远不会打印。

推理要点：

1. 第一轮：延时队列中的 `delayed`（0 秒到期）移入 ready，ready 快照为 `[soon, delayed]`。执行：`soon` 打印 `4`，把 `5` 放入 ready；`delayed` 打印 `1`，把 `2` 放入延时队列、`3` 放入 ready。
2. 第二轮：延时队列中的 `2` 到期移入 ready，排在已就绪的 `3`、`5` 之后，快照为 `[3, 5, 2]`。依次打印 `3`、`5`、`2`。
3. 第三轮起：ready 与延时队列全空，`timeout = None`，`run_forever` 阻塞等待 I/O——**事件循环不会因为"没有任务"而自动退出**，必须有人调用 `loop.stop()`。这也是本题与第三题的关键区别。

### 三

输出：

```
1
2
4
循环已停止
```

要点：三个回调同轮入队，快照为 `[first, second, third]`。执行快照：`first` 打印 `1`；`second` 打印 `2`，把 `3` 放入 ready 后调用 `loop.stop()`——它只是设置 `_stopping` 标记，**本轮快照会继续执行完**，所以 `third` 打印 `4`；本轮结束后 `run_forever` 检查到 `_stopping` 退出。`3` 留在 ready 队列中，永远没有机会执行。

本题即课堂演示代码：把 `loop.stop()` 换个位置（比如放到 `third` 里），输出就会变成 `1 2 4 3 循环已停止`。
