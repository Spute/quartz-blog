---
title: 用 Filebrowser 轻松搭建你的个人网盘
publish: "true"
tags:
  - 开源软件
  - 文件传输
category: 工具分享
---

## 前言

旧电脑再利用，让它成为个人网盘，部署在家里，让家中各种设备都可以上传下载文件、浏览图片、观看本地影视、本地听歌、在线编辑文件，给朋友分享文件等等。
使用Filebrowser可以帮你实现。

Filebrowser 是一款开源的个人网盘和网页版文件管理器。具备操作简单，要求配置低、运行速度快、页面友好等优点。
相当于你可以用旧电脑快速运行这个软件，搭建一个简易版的NAS（NAS就是放在你家的"超级硬盘"，全家设备都能随时访问，数据完全由你掌控。）

使用场景例如：
1、局域网文件共享
2、自建网盘（同类自建网盘最简单的软件）下载运行即可。

家庭网络上快速观看视频，免费实现，不用花钱购买网盘VIP会员，隐私敏感文件也能安全存储在这个个人网盘中。

<strong>官网：</strong>[Welcome - File Browser](https://link.juejin.cn?target=https%3A%2F%2Ffilebrowser.org%2F)

<strong>GitHub 地址：</strong>[filebrowser/filebrowser: Web File Browser (](https://github.com/filebrowser/filebrowser)[github.com](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2F)[)](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Ffilebrowser%2Ffilebrowser)

<strong>Docker Hub 地址：</strong>[filebrowser/filebrowser - Docker Image | Docker Hub](https://hub.docker.com/r/filebrowser/filebrowser)

<strong>文档：</strong>[https://www.filebrowser.cn/](https://www.filebrowser.cn/)

## 特点

相比百度网盘和多数 NAS 产品，Filebrowser 具备以下优势：

<strong>免安装，开箱即用</strong>

   - 仅需下载一个可执行文件（如 Windows 下的 `filebrowser.exe`），直接运行即可。
   - 用 Go 语言编写，运行速度仅次于 C 语言，小巧高效。
   <strong>对硬件要求低</strong>
   - 适合低性能设备（如 ARM 架构路由器、矿渣 NAS、树莓派等），1GB 内存即可流畅运行。
   - 与需要完整 Web 服务器环境的 Nextcloud、可道云相比，占用资源更少。
<strong>直接操作硬盘，保持原目录结构</strong>

   - 可访问系统根目录，所见即所得。
   - 不会因数据库或服务器目录限制破坏硬盘原有结构，也避免网页显示与硬盘内容不一致的情况。
<strong>访问速度快，无冗余压缩</strong>

   - 可通过命令行关闭图片压缩功能，直接读取图片 EXIF 缩略图。
   - 浏览 5000 张图片的文件夹仅需约 2 秒，不会因生成缩略图卡死。
   - 相比 Nextcloud、可道云等动辄后台压缩图片的方案，对低配设备更友好。

核心功能•开箱即用，下载一个可执行文件直接运行，不需要数据库不需要复杂配置，我在树莓派上5分钟就搭好了•文件管理全能，上传、下载、重命名、移动、复制、删除这些基本操作应有尽有，还支持批量操作和拖拽上传•在线预览编辑，图片、视频、音频、PDF、代码文件都能直接在浏览器里打开，Markdown和文本文件还能在线编辑，不用下载到本地•多用户权限系统，可以创建多个用户，每个用户设置不同的访问目录和权限，家人共用一台NAS也能各管各的文件•文件分享功能，生成分享链接给别人下载文件，可以设置密码和有效期，比QQ传文件方便多了


## 更保密公开链接分享方式（可选）

普通分享：https://rack-nerd.520233.best/cjtFBNYp

保密分享：https://rack-nerd.520233.best/api/public/dl/cjtFBNYp?token={{哈希值}}

![[HLLHb25qtogT3Ax1lY5cpMO9nLd.png]]

ps:每次修改，文件的哈希值（用于校验内容完整性）都会发生变化，

## windows 系统安装使用

1. 在 github 中下载页面 [https://github.com/filebrowser/filebrowser/releases](https://github.com/filebrowser/filebrowser/releases)
2. 选择 window 版本（选择 AMD64 的架构）
3. 下载压缩包，解压后可执行运行 exe 文件，
4. 会出现命令窗口，找到初始账号和密码
5. 同一家庭网络下，用手机或者 ipad 都可以通过电脑的 IP 访问这个网盘服务。

![[U1ATblVJDoJvTTxA9hxcKLsGnFg.png]]
