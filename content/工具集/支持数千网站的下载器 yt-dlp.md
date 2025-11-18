---
title: 支持数千网站的下载器 yt-dlp
---

# 支持数千网站的命令行下载器 yt-dlp，Bilibili、抖音、TikTok、X

## 前言

<strong>yt-dlp 能轻松应对数千个其它网站——Bilibili、抖音、TikTok、X、PornHub 等等。</strong>

10w 星标的项目，yt-dlp 是一个功能丰富的命令行音频/视频下载器，支持数千个网站。

- 项目地址： [https://github.com/yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)
- 支持的网站： [https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

PS: 不支持 YouTube 的原因是，因为它的反爬机制已升级到前所未有的高度，动态签名（PO Token）的实时算法让原有的内置 JavaScript 解释器彻底失效。开发者们尝试了各种修复方法，但每一次补丁都像在漏水的船上临时加固，最终还是必须引入真正的 JavaScript 运行环境作为根本解决方案。

之前介绍的 buzz 工具的视频链接一键提取文字的功能底层使用的就是这个下载器

![[ZQLMbykWOo5wOJxwqfScUQnfnub.png]]

## 使用方法

在项目主页找到如下内容，根据电脑系统下载对应的文件

![[ZU5sbNsaEo7ZKZxPtHGcHXeJn5b.jpeg]]

也可以使用我直接下载好的：

我以 windows 为例，找到刚刚下载的文件，在文件栏输入“powershell”，按下回车键，就会在 yt-dlp 下载器所在的目录打开一个 powershell 命令行。

![[NNcEbUKvzoCOB0xQpoJc2MSynBb.png]]

然后在命令行按如下图输入“yt-dlp”+ 空格 + 下载链接，注意下载链接要用引号。

![[X63HbcuF9oNFJcxjY0ccZeeGnVg.png]]

![[RW1kbcfMKoxZDhxXcMcckwednGh.png]]

好的，这是一篇基于您提供的官方页面撰写的软件推荐文，采用朴素风格，并清晰地分为“软件介绍”和“功能介绍”两部分。

---

# <strong>开源免费！支持全球数千个视频网站的下载神器 - Seal</strong>

## 前言

如果你经常需要在手机上将在线视频保存下来离线观看，Seal 会是一个非常可靠且强大的选择。

<strong>Seal</strong> 是一款专门为手机设计的视频下载应用它的核心基于大名鼎鼎的开源命令行工具 <strong>yt-dlp</strong>，这意味着它继承了 yt-dlp 的强大兼容性，支持从<strong>全球数千个视频网站</strong>下载内容。

它将原本需要在电脑上通过命令完成的复杂操作，简化成了在手机上轻点触摸就能完成的事。应用<strong>完全免费、开源</strong>，让视频下载变得<strong>“即开即用，简单好用”。</strong>

以下是我测试 B 站视频下载，3 步搞定。

![[TRbUbsXi9oaO4vx1he3c4dj0nzf.png]]

> <strong>注意事项：</strong>
>
> - 请仅在合法、合理的范围内使用，例如开发、测试或学习目的。
> - 建议提前了解相关平台的使用条款，避免违规操作。

## <strong>功能介绍</strong>

Seal 的功能既全面又实用，能满足大多数用户的下载需求：

- <strong>广泛的平台支持</strong>：凭借 yt-dlp 的支撑，无论是主流视频网站还是众多小众平台，Seal 基本都能应对。支持的网站可以查看： [https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)
- <strong>音视频分离下载</strong>：你可以选择下载完整的视频，或者仅提取高质量的音频文件，非常适合保存音乐或播客。
- <strong>丰富的媒体资源</strong>：除了视频本身，它还能帮你下载视频的封面、字幕，并将这些元数据（如专辑信息）自动嵌入到文件中，管理起来更方便。
- <strong>高效的下载体验</strong>：应用内置了强大的 aria2 下载器，支持多线程下载，能有效提升下载速度。
- <strong>便捷的链接获取</strong>：应用右下角有一个剪贴板按钮，能智能识别并抓取你复制的视频链接，即使链接和文字混在一起也能准确提取。
- <strong>播放列表下载</strong>：支持整个播放列表或合集一键下载，省去逐个操作的麻烦。
- <strong>为高级用户准备</strong>：如果你熟悉 yt-dlp 的命令行参数，还可以在 Seal 中自定义命令模板，实现更精细的控制。
- <strong>持续更新</strong>：应用内内置了 yt-dlp 的更新功能，可以随时跟进以支持最新的网站变化。

## 安装使用

github 项目地址：[https://github.com/JunkFood02/Seal](https://github.com/JunkFood02/Seal)

Github releases 下载地址：[https://github.com/JunkFood02/Seal/releases/latest](https://github.com/JunkFood02/Seal/releases/latest)

F-Droid 下载地址: [https://f-droid.org/packages/com.junkfood.seal/](https://f-droid.org/packages/com.junkfood.seal/)

也可以使用我下载好安装包：

夸克网盘链接：[https://pan.quark.cn/s/364ce78a8f33](https://pan.quark.cn/s/364ce78a8f33)

蓝奏云网盘：[https://wwfx.lanzouu.com/i8jpA39cvnfe](https://wwfx.lanzouu.com/i8jpA39cvnfe) 密码:crhz

使用起来也很简单，复制视频链接，粘贴到软件中，即可直接下载。
