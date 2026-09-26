---
permalink: python/mv8kys
chapter: 00
title: Python语言核心精讲
type: MOC
tags:
  - python
---

# Python语言核心精讲

## 学习路径

| 章节 | 笔记                                              | 主题                                                                                               |
| ---- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| 01   | [[01-必看导言]]                                   | 导言                                                                                               |
| 02   | [[02-Python环境安装]]                             | 环境搭建、pyenv、VSCode                                                                            |
| 03   | [[03-Python基本语法]]                             | 类型、运算符、流程控制                                                                             |
| 04   | [[04-容器类型]]                                   | list / tuple / dict / set                                                                          |
| 05   | [[05-函数]]                                       | 参数、返回值、文档字符串                                                                           |
| 06   | [[06-作用域]]                                     | LEGB、global、nonlocal、闭包                                                                       |
| 07   | [[07-lambda表达式]]                               | lambda、高阶函数、sorted/map/filter/reduce                                                         |
| 08   | [[08-类和对象]]                                   | 类定义、`__init__`、实例/类属性、方法、继承、MRO、访问控制、`type`/`isinstance`/`getattr` 等       |
| 09   | [[09-对象的类型]]                                 | `type()` 动态建类、MRO、私有成员、对象/类/`type`/`object`/`function` 关系、成员查找顺序            |
| 10   | [[10-对象的创建过程]]                             | `__new__` / `__init__` 协作、单例模式、对象池、返回不同类型对象                                    |
| 11   | [[11-可调用对象]]                                 | `callable()`、`__call__`、可配置函数对象、状态保持回调                                             |
| 12   | [[12-元类]]                                       | `type` 与 `class` 语法糖、自定义元类、元类查找顺序、元类三钩子                                     |
| 13   | [[13-装饰器]]                                     | 装饰器语法、functools.wraps                                                                        |
| 14   | [[14-魔术方法]]                                   | `__str__`/`__repr__`、比较、算术、容器协议、类型转换、属性拦截、`__del__`                          |
| 15   | [[15-描述符]]                                     | 描述符协议、数据/非数据描述符、访问顺序、`__set_name__`、`@property` 原理、惰性计算/类型检查       |
| 16   | [[16-异常处理]]                                   | `try`/`except`/`else`/`finally`、异常层次结构、`raise`、自定义异常、异常链                         |
| 17   | [[17-迭代器与生成器]]                             | 迭代器协议、可迭代对象、消费者、`range`、推导式、生成器与 `yield`、`yield from`、`send`、itertools |
| 18   | [[18-上下文管理器]]                               | `with` 执行流程、`__enter__`/`__exit__`、异常抑制、`@contextmanager`、多上下文管理器               |
| 19   | [[19-ABC]]                                        | 抽象类、`@abstractmethod`、抽象属性、接口约束、插件/数据源应用场景                                 |
| 20   | [[20-类型标注]]                                   | 变量/函数标注、`Optional`/`Union`、容器类型、`Self`、泛型、`Callable`、`TypedDict`、`type: ignore` |
| 21   | [[21-模块化]]                                     | 模块/包/成员、`__all__`、`__init__.py`、相对导入、搜索路径、循环导入                            |
| 22   | [[22-标准库]]                                     | 官方文档导航、树形目录展示、Markdown 合并作业                                                    |
| 23   | [[23-第三方库]]                                   | pip、镜像源、版本约束、requirements、venv、AI 聊天工具实战                                       |
| 24   | [[24-事件循环]]                                   | 同步 vs 异步、事件循环、`run_forever`、`call_soon`/`call_later`、队列调度预测                    |

## 按标签浏览

- 课件：`#课件`
- 主题索引：`#list` `#dict` `#set` `#tuple` · `#函数` `#作用域` `#闭包` · `#lambda` `#高阶函数` · `#类` `#对象` `#继承` `#MRO` `#元类` `#__new__` `#单例模式` `#可调用对象` `#__call__` `#metaclass` `#魔术方法` `#__str__` `#__getitem__` `#描述符` `#property` · `#装饰器` `#wraps` · `#异常处理` `#try` `#except` `#raise` `#异常链` · `#迭代器` `#可迭代对象` `#生成器` `#yield` `#推导式` `#itertools` · `#上下文管理器` `#with` `#contextmanager` · `#ABC` `#抽象类` `#abstractmethod` · `#类型标注` `#typing` `#泛型` `#TypedDict` `#Callable`
- 工具链：`#pyenv` `#VSCode`
- 工程化：`#模块化` `#模块` `#包` `#导入` `#__init__` `#__all__` `#相对导入` `#循环导入` · `#标准库` `#os` `#re` · `#第三方库` `#pip` `#虚拟环境` `#venv` `#依赖管理` `#dotenv` · `#异步` `#事件循环` `#asyncio` `#call_soon`
