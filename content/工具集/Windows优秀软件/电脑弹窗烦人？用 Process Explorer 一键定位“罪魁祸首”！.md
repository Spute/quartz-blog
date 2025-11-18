---
title: 电脑弹窗烦人？用 Process Explorer 一键定位“罪魁祸首”！
---

## 前言

电脑上总是弹广告弹窗，关掉了后，过段时间又出来了，好烦！怎么办？

使用<strong>Process Explorer</strong>工具可以轻松帮你办到。它可以帮你找到是哪个程序打开了弹窗，找到它后你就能精准卸载这个“罪魁祸首”。

<strong>Process Explorer</strong> 来自大名鼎鼎的 Sysinternals（这家公司后来被微软收购），它可显示有关打开或加载了哪些句柄和 DLL 进程的信息，也就是<strong>哪个程序打开了哪些特定的文件或目录</strong>。

## 安装使用

官网下载地址：[https://learn.microsoft.com/zh-cn/sysinternals/downloads/process-explorer](https://learn.microsoft.com/zh-cn/sysinternals/downloads/process-explorer)

或者使用我已经下好的

解压后只需运行<em>进程资源管理器</em> (procexp.exe)，即可打开软件（无需安装）

然后点击<strong>十字准星</strong>的图标，拖拽到任何窗口（包括广告弹窗），即可找到打开这个窗口的程序，然后点击 ❌ 把它终止掉。

![[GWsKbkzxYodHG8x5VQ5c9HUwnee.png]]

如下是我拖拽到浏览器窗口，显示的页面，可以看到 chrome 进程被标蓝了，成功找到了窗口打开者

![[TwEmba2tPolbbTxteJncQ57nnih.png]]

## 文件删除不了，定位哪个进程占用了

通过名称搜索“Filter by name”
