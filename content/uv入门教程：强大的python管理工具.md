---
title: uv入门教程：强大的python管理工具
publish: "true"
category: 文章写作
date: 2026-03-17
alias: " dc9tw9j83xxjivdnbj04"
tags:
---
# 介绍

官网：https://docs.astral.sh/uv/getting-started/

uv 是一个用 Rust 编写的极速 Python 包和项目管理器。

# 安装 uv

windows

```Bash
winget install uv

# powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

macOS、Linux

```Bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

uv 默认读取`pyproject.toml`和`uv.toml`配置文件，读取目录为 项目根目录、uv 配置目录。

uv 安装的 python 版本使用 cpython 源码压缩包，托管在 github [astral-sh/python-build-standalone](https://github.com/astral-sh/python-build-standalone)，不是 python 二进制安装包，查看[环境变量说明](https://docs.astral.sh/uv/reference/environment/#uv_python_install_mirror)。

如果安装缓慢或者失败，可在用户目录下添加 uv 全局配置文件 `uv.toml`文件，使用下面的配置：

```TOML
python-mirror = "https://cnb.cool/astral-sh/python-build-standalone/-/release/download"
```

# 使用 uv

本文档仅记录最常使用的命令功能，包含以下几方面：

```Bash
# 替代原 python 和 pip 的管理功能
uv python [OPTIONS] <COMMAND> # 安装和管理 python
uv venv [OPTIONS] [PATH] # 初始化 venv 虚拟环境，默认目录为 .venv
uv pip [OPTIONS] <COMMAND> # 在虚拟环境中使用 pip 安装依赖

# uv特性，方便管理和迁移项目
uv init # 初始化项目，包括 main.py  pyproject.toml  README.md 三个基础文件
uv add/remove [dependencies] # 管理项目依赖
uv cache clean # 缓存管理
uv tool [command] [options] # 安装和管理 uv 工具
uvx tool # 调用第三方工具
```

## 安装和管理 python 版本：

基本命令

```Bash
$ uv python [OPTIONS] <COMMAND>

Commands:
  list            列出python版本
  install         安装python
  upgrade         升级python版本
  find            查找python版本
  pin             固定python版本到项目 .python-version 文件中
  dir             显示python安装目录
  uninstall       卸载python
  update-shell    更新shell环境变量
```

安装 python

```Bash
uv python install <version> <--default>
# version: python版本，不传则使用默认的最新稳定版
# --default: 设置为默认的python版本，会生成对应的 python.exe 全局快捷方式，不传则只生成 python3.exe python3.14.exe 这两个快捷方式

# 安装之后如果无法被全局命令行识别，执行以下命令更新环境变量
uv python update-shell
```

查看所有 python 版本（包括使用 python 安装包安装的可用版本）

```Bash
uv python list <OPTIONS>
# --all-versions   列出所有python版本
# --only-installed 列出所有已安装版本

$ uv python list
cpython-3.14.2-windows-x86_64-none  C:\Users\user01\AppData\Roaming\uv\python\cpython-3.14.2-windows-x86_64-none\python.exe
cpython-3.14.2-windows-x86_64-none  C:\Users\user01\.local\bin\python3.exe
cpython-3.14.2-windows-x86_64-none  C:\Users\user01\.local\bin\python3.14.exe
cpython-3.14.2-windows-x86_64-none  C:\Users\user01\.local\bin\python.exe
```

卸载 python 版本

```Bash
uv python uninstall <version>
# 如 uv python uninstall 3.10.19
```

  

## venv 虚拟环境管理

基础语法

```Bash
uv venv [OPTIONS] [PATH]
# 常用OPTIONS：
# --python: 指定 python 版本，不指定则为本地最新python版本
# --index-url: 设置默认的 pypi 源
# --index：虚拟环境使用的 pypi 源名称（需要在 uv.toml 或 pyproject.toml  中配置)

# PATH 默认为 .venv
```

![](https://flexivrobotics.feishu.cn/space/api/box/stream/download/asynccode/?code=NjJlMTBiYTI0NTAwNzYzOTEzYzBlMGY5NTcwODdlOTBfZjA0Y1R2eEw2cHdvTVRjSTJNaFhwMEJTR1ZWbjNwaVNfVG9rZW46Smh0V2JwUkdSb0JjSXl4bVFhSmNuUUJHblJjXzE3NzM3MTc1MjM6MTc3MzcyMTEyM19WNA)

  

## 依赖安装与管理

uv 在虚拟环境中，可以用两种方式来管理依赖，此处以 旧版 requirements.txt 和 新版 pyproject.toml 分别进行说明。

注意：

uv安装的Python无全局`pip`命令，`uv pip`仅可在`uv venv`虚拟环境中使用。其他第三方Python工具若需在`cli`执行，也需在该虚拟环境中运行；否则需用`uvx <tool>`调用（例如：`uvx playwright install firefox`）。但这并非唯一调用方式，详见下方[uv 简单教程](https://flexivrobotics.feishu.cn/wiki/DJDiwxZQjiAAlFknKn8ckdbXnbc?larkTabName=space#share-QGfndcnyso5zSDxUn31cQPcQnYc)。

### 旧版 requirements.txt

假定旧版项目中使用 requirements.txt 进行依赖管理，在保持现状不变的情况下，可以使用`uv venv`初始化虚拟环境，然后使用 `uv pip install -r requirements.txt` 进行依赖安装，与原 python + pip 的使用形式保持一致。

```Bash
$ uv venv
$ .venv\Scripts\activate.bat
$ uv pip install -r requirements.txt
```

### 新版 pyproject.toml （推荐）

初始化项目（可选）

```Bash
uv init
```

初始化虚拟环境 venv，与pip不同，uv默认需要使用虚拟环境

```Bash
uv venv
```

添加依赖

```Bash
uv add <dependency_name>
```

移除依赖

```Bash
uv remove <dependency_name>
```

进入虚拟环境

```Plain

.venv\Scripts\activate.bat # windows
source .venv/bin/activate # linux macos
```

### 从 pip 迁移到 uv

可按以下步骤，从 pip + requirements.txt 迁移到 uv + pyproject.toml + uv.lock ：

```Bash
# 1. 初始化uv项目
uv init

# 2. 从 requirements.txt 导入依赖，同时生成 uv.lock 文件
uv add -r requirements.txt

# 3. git克隆之后的项目重新从 pyproject.toml 安装依赖
uv pip install -r pyproject.toml
```

如果有特定平台的依赖，可参考[官方文档](https://docs.astral.sh/uv/guides/migration/pip-to-project/#importing-platform-specific-constraints)

  

## uv 工具调用

`uv tool` = `pip`全局安装的工具，作为 cli 命令使用，例如 `ruff` `playwright` 等。

执行`uv tool run <name>` 可以不安装而直接使用工具，也可以用`uv tool run`的别名`uvx`。执行 `uvx`调用工具时，它们的依赖会被临时安装 与当前项目隔离的虚拟环境，且被视为一次性的。一旦执行`uv cache clean`清空本地缓存，它就失效了，当然重新执行`uvx`还是会被重新创建，存储在缓存目录仅仅是为了加速多次调用。

```Bash
# 使用 ruff 工具
uvx ruff
uvx ruff==0.5.0
# 使用 playwright 安装测试浏览器
uvx playwright install firefox
```

经常使用的工具，可以使用 `uv tool install` 命令安装，它会被安装到 uv 工具目录（如`c:\Users\user01\.local\bin`），除非工具被卸载或环境被删除，否则工具可直接使用，无需虚拟环境或`uvx`执行。

```Bash
# 安装
uv tool install ruff # 最新版本
uv tool install ruff==0.5.0 # 指定版本
uv tool install ruff>=0.3.0,<=0.5.0 # 指定范围安装
uv tool install ruff --python 3.10.19 # 指定python版本安装

# 升级工具
uv tool upgrade ruff # 工具升级时也会保留安装时提供的设置,例如版本范围限制
uv tool upgrade black --upgrade-package click # 升级工具中的某个软件包

# 重装
uv tool upgrade ruff --reinstall # 重装所有包
uv tool upgrade black --reinstall-package click # 重装单个软件包
```

上面提到，uv 安装的 python 是没有全局 pip 命令的，我们可以使用 `uv tool install pip`来安装全局的 pip 工具。

  

## uv缓存管理

基础命令

```Bash
uv cache clean # 清空所有缓存，uvx 工具会失效
```

## 运行py脚本

**不用激活，直接用 uv run（最干净）**

```Plain
uv run python main.py
或者：
uv run pytest
uv run django-admin runserver
```

👉 原理： `uv` 会自动帮你用 `.venv` 里的 Python 运行，不需要你手动进入环境。
