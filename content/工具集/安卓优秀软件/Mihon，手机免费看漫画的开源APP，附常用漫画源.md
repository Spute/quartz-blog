---
title: Mihon，手机免费看漫画的开源 APP，附常用漫画源
---

## 前言

这是一款让你自由看线上漫画的好用 APP「Mihon」，完全免费，无广告。

> 本文由[原文](https://ivonblog.com/posts/mihon-manga-reader/)整理而来

## Mihon 特点

- 简洁易用的离线漫画阅读器，支援读取 ComicInfo.xml 分类漫画。
- 自由阅读线上网站的漫画，例如嗶咔漫画、漫画人、E-hentai、Pixiv、Danbooru、Webtoon、腾讯漫画、Toomics、Bilibili 漫画……等等数不清的网站。可下载漫画离线阅读。
- 跨平台，有 Android、iOS、Linux、Windows、macOS、网页版等各种版本。
- 开放原始码，自由软体。只要从官方来源下载就不会有任何病毒。
- 有非常多的分支版 APP，针对不同网站优化。
- 可搭配 MyAnimeList、Bangumi 等网站。

## Mihon 简介

首先简述一下 Mihon 的设计理念，这是一款高度模组化的 APP。

使用者要先下载「Mihon 主程式」。主程式开启预设是什么都没有的，只能读本机漫画图档，类似 Perfect Viewer 那样。漫画可以是包含图档的资料夹，或者.cbz 格式的压缩档。

要看线上漫画的话，你要加入「扩充套件储存库」，再安装「漫画扩充套件」，才可以瀏览各大漫画网站的资源。Mihon 漫画扩充套件的网站正盗版混杂，且大部分都不是 Mihon 官方开发者维护的，请自行確认安全性。

漫画你可以线上阅读，也可以下载到本机离线阅读。

Mihon 提供了一个整合性的界面，方便你存取各大漫画网站的资源。

另外，Mihon 主程式不只官方原版一种，有很多种分支版。如果你觉得原版功能不符合需求，再去试试那些分支版吧！

## 下载 Mihon 主程式

注意：Mihon 是开源免费的 APP，并未在 Google Play 和 App Store 上架，请到 Github 下载。

### 官方版 Mihon

目前官方版 Mihon 仅支援 Android 系统。如果你要在其他系统使用，请看下面「分支版 Mihon」一节。

Mihon 以前叫做 Tachiyomi，最早是 Inorichi 在 2014 年发起的专案，APP 名字来自日文，意思是「在书店站著看免费漫画」。APP 內建许多漫画网站的扩充套件，官方维护著一个专门收录扩充套件的储存库。

然而 2024 年，开发者[收到韩国 Kakao 公司的版权警告](https://tachiyomi.org/news/2024-01-13-goodbye)，说要起诉所有参与该专案的人士，导致他们不再积极维护程式，官方也把漫画扩充套件的储存库给刪了。

所幸开源社群马上有人接手，「Mihon」是 Tachiyomi 开发者另外发起的专案，功能一模一样，只是名字改了而已，可说是 Tachiyomi 的正统继承者。同时，漫画扩充套件的储存库也换其他开发者维护了。

Mihon 这个 APP 名字同样很有趣，日文意思是「漫画试阅本」。现在，Mihon 不再內建扩充套件储存库，变成要使用者自己去找扩充套件来用。

你可以在 [Github](https://github.com/mihonapp/mihon/releases) 取得最新 Android 版的 Mihon APK。需要 Android 7 以上系统才能安装。

### 分支版 Mihon

分支版 (fork) 是 Mihon 社群的一大特色，许多开发者嫌原版 Mihon 功能太少，便推出了自己的修改版。

虽然分支版功能各异，但有些漫画扩充套件是通用的，你可以安装几个比较后再决定要用哪个当主客户端。

现在比较活跃的分支版 Mihon 有以下几个，点选连结下载：

## 安装线上漫画扩充套件来源

透过社群开发的扩充套件，线上阅读漫画，或者下载到本机离线阅读。

1. 初次开启 APP，Mihon 会要求你设定档案储存位置，我个人是把档案放在 `Pictures/Mihon` 资料夹（若该资料夹不存在请自行新增）
2. 论最受欢迎的 Mihon 储存库，最有名的便是 [keiyoushi 的储存库](https://github.com/keiyoushi/extensions-source)。Github 上还有很多中文开发者维护的储存库，请自行搜寻。
3. 点选 APP 的探索 → 扩充套件，点选右上角，扩充套件储存库
4. 加入 keiyoushi 的储存库网址：

```bash
https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.min.json
```

1. 如果扩充功能有问题，请到 [keiyoushi 储存库](https://github.com/keiyoushi/extensions-source/issues)回报。
2. 回到扩充套件页面，下拉重新整理，就能下载漫画网站的扩充套件了。点选右上角「筛选」开启所有语言的网站。

## 阅读本机漫画图档

自行准备漫画图档，放到指定资料夹，再用 Mihon 读取，把 Mihon 当成纯粹的私人漫画阅读器 APP。Mihon 支援读取 ComicInfo.xml，可以用这个来搜寻標籤。

1. 把漫画图档放到 Mihon 资料夹下面的 `/local/` 资料夹。根据 [Mihon 官方文件](https://mihon.app/docs/guides/local-source/)，每本漫画的结构应该如下放置：

```bash
📁 Pictures/Mihon/local
└── 📁 漫画或系列名称
    ├── 📁 第一章或第一集
    │   ├── 图片1.jpg
    │   └── 图片2.jpg
    ├── 📁 第二章或第二集
    │   ├── 图片1.jpg
    │   └── 图片2.jpg
    └── 漫画缩图.jpg
```

1. 漫画页数不一定要全部都用纯图片储存，使用.cbz 或.zip 压缩档也是可以的，这样搬移才不会花太多时间。
2. 新增完成之后，点选 Mihon 的探索 → 本机来源页面，就会看到导入的漫画。
