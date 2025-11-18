---
title: AI 语音工具合集
---

# 微软 edge-tts 文本转语音网站

一款免费的文本转语音工具，提供语音合成服务，支持多种语言，包括中文、英语、日语、韩语、法语、德语、西班牙语、阿拉伯语等 74 种语言，318 种声音。

背后使用的应该是基于微软 edge-tts，效果还挺好的，在这个网站上可以方便的使用。

- 网站地址：[https://d1tools.com/tools/ai-tts/](https://d1tools.com/tools/ai-tts/)

![[PVptbiBoeoq3d2xGDM6c5fDZnGb.png]]

- [谁是最强开源 TTS？8 款主流开源 TTS 大测评](https://waytoagi.feishu.cn/wiki/E5aGwN9PSie8i3kwBvgcAXoPnDf)

# 微软 edge-tts 文本转语音桌面应用

今天给大家分享一个提高创作效率的文本转语音工具。它是完全免费，在本地电脑即可使用的开源工具。

你可用它快速生成旁白，无需耗费时间精力亲自配音，节省人力成本。做知识科普、故事讲述类账号，能把文字稿一键转语音，搭配画面，轻松产出内容，大幅提升创作效率 。

- 项目地址：[https://github.com/smallnew666/edge-tts-ui/tree/main](https://github.com/smallnew666/edge-tts-ui/tree/main)
- window 工具下载地址：[https://github.com/smallnew666/edge-tts-ui/releases/tag/edge-tts](https://github.com/smallnew666/edge-tts-ui/releases/tag/edge-tts)

## 步骤：

1. 点击下载链接，下载 exe 文件

![[Q7rSbFCGHofr7ZxdpOxcjZa3nzb.png]]

1. 然后双击下载后的 tts.exe 文件即可打开这个软件。会出现如下页面：
   1. 输入你需要转成语音的文字，支持插入停顿
   2. 点击下拉框选择内置音色
   3. 点击生成，等待生成完成，生成完成后支持试听
   4. 可以点击打开文件位置查找上一步生成的音频文件用于合成视频

![[XUGebEdmaoHVnExbW2OctdymnAe.png]]

# 音频转录工具 Buzz，支持 B 站/油管链接一键转录

今天将 buzz 更新到最新版 1.2.0 版本后，发现支持了音频链接直接转录的功能，太好用了。这里记录一下使用方法和一些相关功能。

## 是什么

支持在个人电脑上进行离线转录和翻译音频。由 OpenAI 的 [Whisper](https://github.com/openai/whisper) 提供支持。

下载地址：[https://github.com/chidiwilliams/buzz/releases](https://github.com/chidiwilliams/buzz/releases)

工具文档：[https://chidiwilliams.github.io/buzz/zh/docs](https://chidiwilliams.github.io/buzz/zh/docs)

支持简体中文的方法（默认只支持繁体中文）：https://wulu.zone/posts/whisper-cn

## 功能

- 导入音频和视频文件，并将转录内容导出为 TXT、SRT 和 VTT 格式（[演示](https://www.loom.com/share/cf263b099ac3481082bb56d19b7c87fe)）
- 从电脑麦克风转录和翻译为文本（资源密集型，可能无法实时完成，[演示](https://www.loom.com/share/564b753eb4d44b55b985b8abd26b55f7)）
- 支持 [Whisper](https://github.com/openai/whisper#available-models-and-languages)、 [Whisper.cpp](https://github.com/ggerganov/whisper.cpp)、[Faster Whisper](https://github.com/guillaumekln/faster-whisper)、 [Whisper 兼容的 Hugging Face 模型](https://huggingface.co/models?other=whisper) 和 [OpenAI Whisper API](https://platform.openai.com/docs/api-reference/introduction)
- [命令行界面](https://chidiwilliams.github.io/buzz/zh/docs#%E5%91%BD%E4%BB%A4%E8%A1%8C%E7%95%8C%E9%9D%A2)
- 支持 Mac、Windows 和 Linux

## 演示

导出简体中文操作：

![[RUBebSB7nor0gTx7aOgcwBaInfO.png]]

效果如下，在没有独立显卡情况下也可以较快完成转录：

![[SEDobOS19oxBjsxy1pNcrLLvnLe.png]]

Buzz 是在 whisper 内核上加上了图形界面，对无编程基础用户更友好。

<u>Whisper</u>是 OpenAI 推出的一种开源语音识别模型，能够自动识别多种语言，将音频转换文字。

## 链接一键转录

成功安装后，打开软件，按如下操作。如下是 YouTube 的链接视频。

![[N6Hibsd55oScW7xappfcHrM1nth.png]]

## 模型选择

模型越大耗时越长

![[LQc8bRzQKorFcwxlrsTc5lajnLb.png]]

模型越大占用的空间也更大

![[MDfkbhk5Pohe2ExRsYJcPBO3nLg.png]]

同时模型越大转录的效果也更好

![[J4CubgP8LoA9USxZEsXcLjXHnVb.png]]

使用大模型转录过程占用的 CPU 资源也越大

![[Ovwcb98cSoBaLmxUg5GctdVunIe.png]]

以下是 whisper 的模型对比表

![[BzBgby4uDoH7evxb1F7cWQIRnZg.png]]

测试下来，日常使用 base 或 small 模型比较合适，效果不错占用的资源和时间消耗更能接受。
