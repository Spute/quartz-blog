---
title: 局域网文件传输神器 LocalSend--比微信 QQ 更快更安全的跨平台传输方案
---

## 前言

很多人都会头疼——如何在电脑和手机之间快速传文件？

提到这个，可能 90% 的人第一反应都是微信文件传输助手。但用过的都知道，微信传文件有局限性，不仅慢，还有大小限制，隐私性也存疑。

推荐文件传输神器<strong>LocalSend</strong>，一款 63K 星标的开源项目，安装即用、跨平台的本地文件传输工具。

不仅完全免费开源，还能实现多设备快速互传，关键的是所有数据只在你的本地网络跑，绝对安全。

项目地址：[https://github.com/localsend/localsend/tree/v1.17.0](https://github.com/localsend/localsend/tree/v1.17.0)

## 核心特点

- <strong>无需联网</strong>：仅需处于同一局域网内，即可高速传输，无需连接公网。
- <strong>全平台支持</strong>：兼容六大主流平台：

  - Windows / macOS / Linux
  - Android / iOS / Fire OS
- <strong>极简操作</strong>
  安装后自动扫描同网络设备，发送文件像"拖拽"一样简单。
- <strong>无限制传输</strong>
  摆脱微信的 200MB 限制，大视频、安装包想传就传。

## 使用步骤

### 安装软件

根据发送端和接收端的平台类型，选择不同的软件安装包。如下是不同平台的支持的安装源。

### 接收端打开接收

接收端打开软件，“开启”接收

![[KLgkbsYmqoewfPx2f3HcRUs3nUe.png]]

### 发送端发送文件

先选择文件（支持一次性上传多个）

#### 附近设备传输

在“附近设备”找到传输对象名称，点击发送就行了。

![[WTjbbSHmnopUTAxZAYacLPFInBh.jpeg]]

#### 使用 IP 传输

点击接收端右上角的“i”图标，查到接收方的 IP

![[LM68bXk8Rou9qexA2GecsIw2nYh.jpg]]

在发送端输入刚刚查看的 IP，点击确认即可

![[ZsjGbPkGFoRLZ5xzTJwcjEPInLc.png]]

### 效果

好的路由器的话，传输速度可以到 20M+/s ,快的飞起

![[C6M4bt1IpoyT30xVvxpcyU3Dnnd.png]]

## 支持通过链接分享（接收端免安装）

分享下 localSend 非常使用的一个功能。

更新的 v1.14.0 后，接收端可以直接通过链接接收文件，无需安装 app 了

对于给陌生设备传文件这事，LocalSend 的<strong>通过链接分享</strong>功能也解决了这个问题，毕竟给陌生设备，尤其不是自己的设备上安装第三方软件这件事情本身，就是不安全和不礼貌的。

实际上是发送端的 LocalSend 开了一个文件服务器，分享到局域网，接收端可以通过浏览器直接下载。

### 操作步骤

添加文件后，选择通过链接分享

![[AnLWb8q5KoFWPixMUpXcYIiDnwh.png]]

复制链接地址

![[V3SDbJ6jGoewLNxwA3mc5QGlnvc.png]]

接收端使用浏览器打开分享地址，即可直接下载：

![[PlwMbW7CKo0c1ExgqoncwB90nUh.jpg]]

## 软件下载地址

- [官网](https://localsend.org/)
- [App Store](https://apps.apple.com/cn/app/localsend/id1661733229)（iPhone、iPad）
- 夸克网盘[搬运](https://pan.quark.cn/s/9cb377d8b320)（Win、macOS、Android）
