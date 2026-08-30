---
chapter: 02
title: Python环境安装
course: Python语言核心精讲
tags:
  - python
  - 课件
  - 环境
  - pyenv
  - VSCode
---

# Python环境搭建

## Python安装包

Python安装包中包含以下核心组件：

- 解释器：默认为`CPython`
- 包管理器：`pip`
- 标准库：`os、sys、urllib、pathlib、...`
- 交互式终端：`REPL`

### Python发行版

Python有很多的发行版，不同的发行版又有很多的版本

- **官方 Python (CPython)**：C 语言原生实现，Python 标准参考版本，带 GIL，生态最全，日常开发默认首选

- **ActivePython**：商业公司打包的 CPython 发行版，企业级稳定适配，预装常用依赖，偏商用场景

- **Anaconda**：面向数据科学的全家桶 CPython，内置海量数据分析、AI 库，体积大，适合数据分析一站式环境
- **Miniconda**：Anaconda 极简精简版，仅保留 Python+conda 包管理器，无多余预装库，轻量灵活
- **Miniforge**：开源免费 conda 发行版，无 Anaconda 商业版权限制，社区维护，替代 Miniconda 首选
- **Mambaforge**：基于 Miniforge，把 conda 替换为极速 mamba 包管理器，安装依赖速度远超原生 conda
- **Cinder**：Meta 自研优化版 CPython，针对长驻服务、低延迟做运行时与 GC 优化，内部业务专用，通用性差
- **Nogil**：Python 官方无 GIL 自由线程版本，去除全局解释器锁，支持多线程真并行，适合多核并发场景
- **PyPy**：带 JIT 即时编译的 Python 解释器，纯 Python 代码运行速度远超 CPython，C 扩展库兼容性一般
- **Jython**：运行在 JVM 虚拟机上的 Python，可无缝调用 Java 类库，无 GIL，不兼容 C 语言扩展包
- **IronPython**：运行在.NET 平台上的 Python，可直接调用 C#/.NET 生态库，多用于 Windows 桌面与.NET 集成
- **GraalPython/GraalPy**：基于 GraalVM 的高性能 Python，自带强 JIT 优化，支持与 Java 等多语言互通
- **Stackless Python**：CPython 分支，自研无栈微协程，支持超高并发轻量任务，适合游戏、高并发服务场景
- **MicroPython**：极简裁剪版 Python，专为单片机、嵌入式 IoT 设备设计，体积小、占用内存极低

### pyenv

建议使用`pyenv`来管理多个`python`版本

### mac 安装 pyenv

mac 建议使用 HomeBrew 安装 pyenv

```shell
# 安装构建python包的前置依赖项
brew install zstd openssl readline xz zlib
# 安装pyenv
brew install pyenv
# 测试
pyenv --version
```

配置镜像源

```shell
# ~/.zshrc
export PYTHON_BUILD_MIRROR_URL="https://mirrors.aliyun.com/python-release/source/"
```

### win 安装 pyenv

以管理员身份打开`powershell`

```shell
# 解决权限问题
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# 运行安装命令
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

重新打开终端

```shell
# 测试
pyenv --version
```

配置镜像源

1. 右键「此电脑」→「属性」→「高级系统设置」→「环境变量」。

![a911aa22f25bf22fc48a83885299fb4f~tplv-a9rns2rl98-pc_smart_face_crop-v1_512_384](https://resource.duyiedu.com/yuanjin/202605111101231.webp)

2. 在**用户变量**（只影响当前用户）或**系统变量**（所有用户）里点「新建」：
   - 变量名：`PYTHON_BUILD_MIRROR_URL`

   - 变量值：填下面任意一个国内源

     ```
     https://mirrors.aliyun.com/python
     https://mirrors.tuna.tsinghua.edu.cn/python/
     https://mirrors.huaweicloud.com/python/
     https://registry.npmmirror.com/-/binary/python/
     ```

全部确定，**关闭旧 PowerShell，新开一个**即可。

### pyenv 使用

```shell
# 查看所有可安装的python版本
pyenv install --list
# 利用管道命令搜索
pyenv install --list | grep "^  3.14"
# 安装特定版本
pyenv install 3.14.1
# 卸载特定版本
pyenv uninstall 3.14.1
# 查看已安装的版本
pyenv versions
# 查看当前正在使用哪个版本
pyenv version

# 切换全局版本
pyenv global 3.14.1
# 切换本地版本
pyenv local 3.14.1
# 切换当前终端版本（临时生效）
pyenv shell 3.14.1
```

## Hello World

1. 新建文本文件，写入内容：`print("Hello, World!")`
2. 将文本文件保存为：`hello.py`
3. 终端进入到文本文件所在目录，运行`python hello.py`

## IDE

- [PyCharm](https://www.jetbrains.com/pycharm/): Python 专属 IDE，开箱即用，专为 Python 设计，官方内置了 python 开发的诸多功能。
- [VSCode](https://code.visualstudio.com/download)： 通用代码编辑器，装插件才支持 Python，全能型。

选择哪个其实无所谓

本课程选择使用`VSCode`，理由：

1. 全栈开发**尽量**统一编辑器，减少心智负担
2. `VSCode`体系对`AI Coding`支持更友好
3. 轻量高效、启动速度快，低配电脑也能流畅使用

### VSCode插件

安装好`VSCode`后，依次安装以下插件

- **Python**
  语法高亮、代码提示、运行调试、虚拟环境识别，**最核心**。
- **Code Runner**
  右键一键运行Python代码，不用敲命令，新手超好用。
- **Black Formatter**
  自动格式化代码，统一代码风格，不用手动排版。
- **Chinese (Simplified)**
  VSCode界面汉化，零基础友好。

### VSCode配置

code runner 配置

```json
"code-runner.executorMap": {
  // ...
  // 这里要填写 python 的绝对路径
  "python": "/Users/yuanjin/.pyenv/shims/python -u",
}
```

自动格式化配置

```json
"editor.formatOnSave": true,
"[python]": {
  "editor.defaultFormatter": "ms-python.black-formatter",
  "editor.tabSize": 4,
  "editor.insertSpaces": true,
}
```

## 作业

1. 搭建好`Python`环境
2. 编写一个`hello.py`文件，打印`Hello World!`，并能运行成功

---

## 参考答案

> 作业源文件位于 `homework/` 目录，下方通过 Obsidian 嵌入直接展示代码。

![[02-hello.py]]
