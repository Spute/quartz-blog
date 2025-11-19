---
title: python 简介和安装
---

## Python 简介

Python（英式发音：/ˈpaɪθən/；美式发音：/ˈpaɪθɑːn/）是由荷兰人吉多·范罗苏姆（Guido von Rossum）发明的一种编程语言，是目前世界上最受欢迎和拥有最多用户的编程语言。<strong>Python 强调代码的可读性和语法的简洁性</strong>，相较于 C、C++、Java 这些同样影响深远的编程语言，Python 让使用者能够用更少的代码表达自己的意图。

下面是几个权威的编程语言排行榜给出的 Python 语言的排名：
- TIOBE Index 提供
![[Epx2b4EW2oJkMoxT2alcKUEHn9x.png]]
- IEEE Spectrum 提供。
![[Utw3bm2hgo0w9GxM6WlcLiK4npe.png]]
可以看出 python 语言在各大榜单都稳居第一。且 2025 相对于去年占比有明显上升趋势。
### Python 编年史
下面是 Python 语言发展过程中的一些重要时间点：
1. 1989 年 12 月：吉多·范罗苏姆决心开发一个新的脚本语言及其解释器来打发无聊的圣诞节，新语言将作为 ABC 语言的继承者，主要用来替代 Unix shell 和 C 语言实现系统管理。由于吉多本人是 BBC 电视剧《Monty Python's Flying Circus》的忠实粉丝，所以他选择了 Python 这个词作为新语言的名字。
2. 1991 年 02 月：吉多·范罗苏姆在 alt.sources 新闻组上发布了 Python 解释器的最初代码，标记为版本 0.9.0。
3. 1994 年 01 月：Python 1.0 发布，梦开始的地方。
4. 2000 年 10 月：Python 2.0 发布，Python 的整个开发过程更加透明，生态圈开始慢慢形成。
5. 2008 年 12 月：Python 3.0 发布，引入了诸多现代编程语言的新特性，但并不完全向下兼容。
6. 2011 年 04 月：pip 首次发布，Python 语言有了自己的包管理工具。
7. 2018 年 07 月：吉多·范罗苏姆宣布从“终身仁慈独裁者”（开源项目社区出现争议时拥有最终决定权的人）的职位上“永久休假”。
8. 2020 年 01 月：在 Python 2 和 Python 3 共存了 11 年之后，官方停止了对 Python 2 的更新和维护，希望用户尽快切换到 Python 3。
9. 目前：Python 在大模型（GPT-3、GPT-4、BERT 等）、计算机视觉（图像识别、目标检测、图像生成等）、智能推荐（YouTube、Netflix、字节跳动等）、自动驾驶（Waymo、Apollo 等）、语音识别、数据科学、量化交易、自动化测试、自动化运维等领域都得到了广泛的应用，Python 语言的生态圈也是相当繁荣。

> <strong>说明</strong>：大多数软件的版本号一般分为三段，形如 A.B.C，其中 A 表示大版本号，当软件整体重写升级或出现不向后兼容的改变时，才会增加 A；B 表示功能更新，出现新功能时增加 B；C 表示小的改动（例如：修复了某个 Bug），只要有修改就增加 C。
### Python 优缺点

Python 语言的优点很多，简单为大家列出几点。

1. <strong>简单优雅</strong>，跟其他很多编程语言相比，Python 更容易上手。
2. 能用更少的代码做更多的事情，提升开发效率。
3. 开放源代码，拥有强大的社区和生态圈。
4. <strong>能够做的事情非常多</strong>，有极强的适应性。
5. <strong>胶水语言</strong>，能够黏合其他语言开发的东西。
6. 解释型语言，更容易跨平台，能够在多种操作系统上运行。

Python 最主要的缺点是执行效率低（解释型语言的通病），如果更看重代码的执行效率，C、C++ 或 Go 可能是你更好的选择。

## 安装 Python 环境

工欲善其事，必先利其器。想要开始你的 Python 编程之旅，首先得在计算机上安装 Python 环境，简单的说就是安装运行 Python 程序需要的 Python 解释器。我们推荐大家安装官方的 Python 3 解释器，它是用 C 语言编写的，我们通常也称之为 CPython，它可能是你目前最好的选择。

首先，我们需要从官方网站的[下载页面](https://www.python.org/downloads/)找到下载链接，点击“Download”按钮进入下载页面后，需要根据自己的操作系统选择合适的 Python 3 安装程序，如下图所示。

<strong>3.12 和 3.13</strong>版本都处于“bugfix”阶段（也称为维护模式或稳定版本），这个阶段的 python 版本接受错误修复和安全修复，仍会发布新的二进制版本。版本成熟，修复问题且较为稳定，推荐选择这两个中的一个。

![[JkGcbFk2coZeRUxFmiTc4Gbjn3z.png]]

点记上面的下载后，会跳到 [https://www.python.org/downloads/release/python-31210/](https://www.python.org/downloads/release/python-31210/)，下拉找到下面页面。强烈建议使用<strong>安装程序</strong>，如下图，点击下载。

![[RQEybGG1voJ8SVxR6VGcjFADngA.png]]

### Windows 环境
#### 自动安装
首先，<strong>一定要记得勾选“Add python.exe to PATH”选项</strong>，它会帮助我们将 Python 解释器添加到 Windows 系统的 PATH 环境变量中（不理解没关系，勾上就对了）；其次，“Use admin privileges when installing py.exe”是为了在安装过程中获得管理员权限，建议勾选。点击“install Now”即可完成安装
![[RZhSb6HqOoY2k1x0ikBczgXrncg.png]]

#### 自定义安装（可选）

选择“Customize Installation”，使用自定义安装的模式，这是专业人士的选择，而你就（假装）是那个专业人士，不建议使用“Install Now”（默认安装）。

接下来，安装向导会提示你勾选需要的“Optional Features”（可选特性），这里咱们可以直接全选。值得一提的是其中的第 2 项，它是 Python 的包管理工具 pip，可以帮助我们安装三方库和三方工具，所以一定要记得勾选它，然后点击“Next”进入下一环节。

![[Dfnrb11AZoz3Kyxh2V6cHFk2ndh.png]]

接下来是对“Advanced Options”（高级选项）的选择，这里我们建议大家只勾选“Add Python to environment variables”和“Precompile standard library”这两个选项，前者会帮助我们自动配置好环境变量，后者会预编译标准库（生成 `.pyc` 文件），这样在使用时就无需临时编译了。

下面的“Customize install location”（自定义安装路径）强烈建议修改为自定义的路径，这个路径中不应该包含中文、空格或其他特殊字符，注意这一点会为你将来减少很多不必要的麻烦。设置完成后，点击“Install”开始安装。

![[YEBrbfBSnozQCExXBWtc5wMWnsg.png]]

安装成功会出现如下图所示的画面，安装成功的关键词是“successful”，如果安装失败，这里的单词会变成“failed”。

#### 验证

安装完成后可以打开 Windows 的“命令行提示符”或 PowerShell，然后输入 `python --version` 或 `python -V` 来检查安装是否成功，这个命令是查看 Python 解释器的版本号。如果看到如下所示的画面，那么恭喜你，Python 环境已经安装成功了。这里我们建议再检查一下 Python 的包管理工具 pip 是否可用，对应的命令是 `pip --version` 或 `pip -V`。

![[XBmobzxnqoGdDhxdF7IcLfKfnsg.png]]
