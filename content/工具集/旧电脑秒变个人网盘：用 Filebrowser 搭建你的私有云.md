---
title: 旧电脑秒变个人网盘--用 Filebrowser 搭建你的私有云
---

## 前言

旧电脑再利用，让它成为个人网盘，部署在家里，让各种设备都可以上传下载文件、浏览图片、在线观看影视、在线听歌、在线编辑文件，给朋友分享文件等等。使用 Filebrowser 可以帮你实现。

Filebrowser 是一款配置要求低、运行速度快、页面友好的个人网盘和网页版文件管理器。

<strong>官网：</strong>[Welcome - File Browser](https://link.juejin.cn?target=https%3A%2F%2Ffilebrowser.org%2F)

<strong>GitHub 地址：</strong>[filebrowser/filebrowser: Web File Browser (](https://github.com/filebrowser/filebrowser)[github.com](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2F)[)](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Ffilebrowser%2Ffilebrowser)

<strong>Docker Hub 地址：</strong>[filebrowser/filebrowser - Docker Image | Docker Hub](https://hub.docker.com/r/filebrowser/filebrowser)

<strong>文档：</strong>[https://www.filebrowser.cn/](https://www.filebrowser.cn/)

## 特点

相比百度网盘和多数 NAS 产品，Filebrowser 具备以下优势：

1. <strong>免安装，开箱即用</strong>

   - 仅需下载一个可执行文件（如 Windows 下的 `filebrowser.exe`），直接运行即可。
   - 用 Go 语言编写，运行速度仅次于 C 语言，小巧高效。
   - 无需 LNMP 环境或数据库，低门槛上手。
   - 也可用 Docker 快速部署。
2. <strong>对硬件要求低</strong>

   - 适合低性能设备（如 ARM 架构路由器、矿渣 NAS、树莓派等），1GB 内存即可流畅运行。
   - 与需要完整 Web 服务器环境的 Nextcloud、可道云相比，占用资源更少。
3. <strong>直接操作硬盘，保持原目录结构</strong>

   - 可访问系统根目录，所见即所得。
   - 不会因数据库或服务器目录限制破坏硬盘原有结构，也避免网页显示与硬盘内容不一致的情况。
4. <strong>访问速度快，无冗余压缩</strong>

   - 可通过命令行关闭图片压缩功能，直接读取图片 EXIF 缩略图。
   - 浏览 5000 张图片的文件夹仅需约 2 秒，不会因生成缩略图卡死。
   - 相比 Nextcloud、可道云等动辄后台压缩图片的方案，对低配设备更友好。

<strong>硬件与运行环境建议</strong>

- <strong>硬件可选</strong>：Windows/ macOS/ Linux 主机、小型 Linux 服务器、树莓派、支持刷机的路由器、二手 NAS 硬件等。
- <strong>推荐配置</strong>：AMD64 架构，2GB 以上内存更佳；长期运行建议选低功耗设备（如 ARM64），以降低 24 小时开机的电费成本。

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
