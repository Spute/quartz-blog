---
title: scrcpy--显示和控制你的 Android 设备
---

## 是什么

这个应用程序可以镜像通过 USB 或 TCP/IP 连接的 Android 设备（视频和音频），并允许使用电脑键盘和鼠标进行控制。它不需要 root 权限或在设备上安装应用程序。它适用于 Linux、Windows 和 macOS。

- 项目地址：[https://github.com/Genymobile/scrcpy](https://github.com/Genymobile/scrcpy)

## 步骤

### 手机设置

- 打开开发者模式。（方法参考：[https://developer.android.com/studio/debug/dev-options?hl=zh-cn#enable](https://developer.android.com/studio/debug/dev-options?hl=zh-cn#enable)）。以我用的一加手机为例，

```
<strong>1.解锁开发者选项</strong>
打开 设置->关于手机，点击“版本号”十次

<strong>2.打开ADB开关</strong>
进入 设置-系统-开发者选项，打开“USB 调试”开关

<strong>3.授权、允许USB调试</strong>
使用数据线连接你的电脑和手机
手机会弹出授权窗口，记得点击允许哦
```

> [!TIP]
> ADB 全名 Andorid Debug Bridge，中文：Android 调试桥，是一种功能多样的命令行工具，可让您与设备进行通信。adb 命令可用于执行各种设备操作（例如安装和调试应用），并提供对 Unix shell（可用来在设备上运行各种命令）的访问权限。

### 获取 scrcpy 应用

选择合适的平台下载应用安装包

- <u>Linux</u>
- <u>Windows</u> (read <u>how to run</u>)
  Windows (如何运行)
- <u>macOS</u>

### 建立连接

下载完成后解压文件，然后双击以下文件：

![[NUtqb5RThorTIbxW9xZcXhUQnFg.png]]

- 将电脑和设备，使用数据线连接起来
- 打开 cmd 页面后，输入命令即可建立链接：`scrcpy --video-codec=h265 --max-size=1920 --max-fps=60 --no-audio --keyboard=uhid`

![[N4enbmkZdo5fCxx19nEcSGYunLg.png]]

## 无线连接步骤

无线连接可以支持更长的通讯距离，也不会受实体线的限制，虽然会增加一些延迟，但更方便，推荐使用这种方式。开始前的准备：

- 电脑端下载好 scrcpy 程序
- 打开手机端的开发者选项（网上有相关教程）
- 连接前需要保证两个设备处于同一局域网中。

以下是相关的操作步骤，实测有效。

### 首次连接

1. <strong>手机端</strong>：开启“无线调试”，记下<strong>配对 IP:端口 / 配对码</strong>和<strong>调试 IP:端口</strong>。
2. <strong>电脑端（PowerShell，进入 scrcpy 目录）</strong>：运行 `adb pair <配对IP:端口>`，按提示输入<strong>配对码</strong>完成配对。
3. <strong>电脑端</strong>：运行 `adb connect <调试IP:端口>`（注意与“配对端口”不同）。
4. <strong>电脑端</strong>：运行 `./scrcpy.exe` 启动投屏。
5. <strong>电脑端</strong>：直接关闭 scrcpy 窗口结束画面，运行 `adb disconnect` 断开无线连接。
6. <strong>手机端（建议）</strong>：关闭“无线调试”以提升安全性。

### 后续使用:

1. 无需配对, 直接连接并启动远程控制.
2. 注意 ip:port 可能会重新随机生成
3. 退出时: 直接关闭控制画面, 然后在 PowerShell 内运行 ` adb disconnect` 关闭 adb 调试的无线远程连接.
4. 关闭手机上的无线调试功能. 非必须, 但是建议关闭.

### 效果

以下是使用首次连接的过程。亲测后发现 adb 配对的 IP 端口号与 adb 是不一样的，这个要注意以下。

![[AG39bJRCdohSrAxEZtIcg1NZn1g.png]]
