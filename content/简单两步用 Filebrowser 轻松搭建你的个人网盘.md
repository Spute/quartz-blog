---
title: 用 Filebrowser 轻松搭建你的个人网盘
publish: "true"
tags:
  - 开源软件
  - 文件传输
category: 工具分享
---

## 前言

把一台闲置的旧电脑重新利用起来，其实很简单——把它变成你的**私人网盘**。只要部署在家里，全家所有设备都能随时访问：上传下载文件、浏览照片、在线观看本地电影、听歌、在线编辑文档，全都能做到。这一切，只需要 **Filebrowser**。

**Filebrowser** 是一款开源、轻量、易用的网页版文件管理器。无需复杂配置、无需高性能设备，下载即可运行。它能让你的旧电脑瞬间变成一个迷你版 **NAS** ——也就是家里的“超级硬盘”，速度快、访问方便、数据完全掌握在你自己手里。

你可以用它来：
- 局域网内共享文件
- 快速搭建一个属于自己的私人网盘（几乎是最简单的自建方案）

无论是家里在线看视频、随时访问工作资料，还是保存隐私敏感文件，都能免费、安全、稳定地实现。只需一个旧电脑 + Filebrowser，你的家庭私有云就这样搭建好了。

## 特点
### **🌟 1. 零安装，马上能用**
- 下载一个程序，双击就能打开网页网盘。
- 不需要数据库、不需要配置环境，小白也能搭建。
### **🌟 2. 对设备要求很低**
- 老电脑、废旧 NAS、树莓派都能跑。
- 占内存少，比 Nextcloud、可道云更轻量。
### **🌟 3. 文件就是硬盘上的文件**
- 直接显示硬盘里的真实文件夹，不会乱改你的目录结构。
- 网页看到的内容就是硬盘里的内容。
### **🌟 4. 浏览速度快**
- 打开装很多照片的文件夹也不会卡。
- 适合低性能设备。
## **核心功能**
- **文件管理齐全**：上传、下载、重命名、移动、删除、拖拽上传全都有。
- **在线预览**：图片、视频、音频、PDF、代码文件都能直接看，文本还能在线编辑。
- **支持多用户**：可以给家人设不同账号，不互相看到对方文件。
- **安全分享文件**：生成下载链接，可设置密码和有效期。
## 使用步骤
 我这边以windows 系统为例，3步完成部署

1. **下载 Filebrowser**
    - 进入 GitHub 发布页`https://github.com/filebrowser/filebrowser/releases`
    - 找到 **Windows 版本（AMD64）** 并下载
    - 如果嫌 GitHub 下载慢，也可以直接用我准备好的蓝奏云链接：  
        `https://wwfx.lanzouu.com/iqcZC3bo8fif`
2. **运行 Filebrowser**
    - 将下载的压缩包解压，直接双击运行里面的 `filebrowser.exe`。
    - **注意文件共享范围**
        - Filebrowser 会默认共享当前目录的所有内容。
        - 如果你只想共享某个特定文件夹，只需要把 `filebrowser.exe` 移动到那个目录再运行。
    - **数据库文件说明**
        - 首次运行后会自动生成 `filebrowser.db`（用于存储账号密码等信息）。
        - 若你忘记密码，删除 `filebrowser.db` 后再次运行即可重置为一个新的数据库。
![[Pasted image 20251120165303.png]]
3. 会出现命令窗口，找到初始账号和密码。同一家庭网络下，用手机或者 ipad 都可以通过电脑的 IP 访问这个网盘服务。

![[U1ATblVJDoJvTTxA9hxcKLsGnFg.png]]
修改语言，更新初识密码
![[Pasted image 20251120165004.png]]

## 更多参考文档
<strong>官网文档：</strong>[https://www.filebrowser.cn/](https://www.filebrowser.cn/)
<strong>GitHub 地址：</strong>[filebrowser/filebrowser: Web File Browser (](https://github.com/filebrowser/filebrowser)[github.com](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2F)[)](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Ffilebrowser%2Ffilebrowser)
<strong>Docker Hub 地址：</strong>[filebrowser/filebrowser - Docker Image | Docker Hub](https://hub.docker.com/r/filebrowser/filebrowser)
