---
title: termux--Android 下一个高级的终端模拟器
---

# 前言

想在安卓手机上部署一个网页服务器，通过浏览器进行图片查看。找到这个免费开源的项目 termux。

Termux 是一个 Android 高级终端模拟器，开源且不需要 root，支持 apt 管理软件包，安装软件包十分方便，完美支持 Python、 PHP、 Ruby、 Nodejs、 MySQL 等。随着智能设备的普及和性能的不断提升，如今的手机、平板等的硬件标准已达到了初级桌面计算机的硬件标准，用心去打造 DIY 的话完全可以把手机变成一个强大的极客工具。

# 软件基础使用

基本操作还是要学习一下的，可以事半功倍。

Termux 除了支持 `apt` 命令外，还在此基础上封装了 `pkg` 命令，`pkg` 命令向下兼容 `apt` 命令。`apt` 命令大家应该都比较熟悉了，这里直接简单的介绍下 `pkg` 命令:

```bash
pkg search <query>              # 搜索包
pkg install <package>           # 安装包
pkg uninstall <package>         # 卸载包
pkg reinstall <package>         # 重新安装包
pkg update                      # 更新源
pkg upgrade                     # 升级软件包
pkg list-all                    # 列出可供安装的所有包
pkg list-installed              # 列出已经安装的包
pkg show <package>              # 显示某个包的详细信息
pkg files <package>             # 显示某个包的相关文件夹路径
```

> 国光建议大家使用 pkg 命令，因为 pkg 命令每次安装的时候自动执行 apt update 命令，还是比较方便的。

# 基础配置

- 更新 apt 安装源为国内镜像源 `sed -i 's@termux.org/packages/@mirrors.ustc.edu.cn/termux/apt/termux-main@'   $PREFIX/etc/apt/sources.list`
- 更新 apt： `apt update && apt upgrade`
- 允许 termux 访问手机的文件，这个命令会新增一些共享目录。`termux-setup-storage`
- 安装 python
- 安装 git `apt install git openssh`
- 生产 ssh 密钥对 `ssh-keygen -t rsa`
- 开机自启动 sshd，在用户根目录下创建 ` echo "sshd" >> .bashrc`

# 保持 Termux 后台运行

在 Android 手机中运行 Termux，会发现切换到后台运行时，很容易因为系统内存不足而被 `sleep` 甚至杀死。需要对 termux 设置一下：

- 耗电管理》无限制
- 后台自启动

# 内网穿透

部署在内网的 NAS 设备，没有公网 IP，如何将这个内网 IP 对外暴露，让在外的设备能够访问到。有两种方式：

- 一种是端口转发，
- 一种是 VPN 实现点对点链接，创建加密隧道连接内外网，类似建立了一个虚拟专用网络。
- Cloudflare Zero Trust 开通 tunnel：[https://mymuwu.net/?p=1369](https://mymuwu.net/?p=1369)

## WireGuard 协议

WireGuard 协议必须有个服务端，然后多个客户端，服务端必须在公网 IP

Tailscale 是一种基于 WireGuard 的虚拟组网工具，它在用户态实现了 WireGuard 协议。

还有一个完全开源的工具 headscale。好像要自己部署服务端？

- tailscale 实现流程
  - 注册 tailscale：[https://tailscale.com/](https://tailscale.com/)
  - 分别下载 windows、安卓客户端登陆账号
  - 客户端就可以互相访问

## 密码连接

- 开启 sshd 服务：`pkg install openssh 、pkg install openssl`
- 开机启动：`echo "sshd" >> ~/.bashrc`
- 查询用户名：`whoami`
- 修改用户密码：`passwd`
- 查询局域网 ip: `ifconfig`
- 用密码连接：`ssh -p 8022 u0_a633@10.112.0.115`

## ssh 认证连接

1. <strong>-i</strong>后面接的是私钥**：在 SSH 命令中，`-i` 选项后面需要指定你的私钥文件的路径。这是你在本地机器上生成的密钥对中的私钥部分。示例命令为：
   ```bash
   ```

ssh -i ~/.ssh/id_rsa -p 8022 用户名 @IP 地址

```
	

2. <strong>公钥要配置到需要连接的</strong>`sshd`服务**：公钥需要添加到你要连接的SSH服务器上。具体步骤如下：
	- 将生成的公钥（通常位于`~/.ssh/id_rsa.pub`）的内容复制。
	- 在目标服务器（例如Termux中的SSH服务器）上，打开或创建`~/.ssh/authorized_keys`文件，并将公钥粘贴到文件中。
		

这样设置后，你就可以使用私钥通过SSH连接到已配置公钥的服务器，而无需输入密码。

1. 检查Termux的sshd配置，确保开启公钥验证:

```

# 在 Termux 中

cat $PREFIX/etc/ssh/sshd_config

# 确保包含以下设置:

PubkeyAuthentication yes

```

# 常用软件

- vim

- 

# 运行docker

好像root才能运行docker

https://www.reddit.com/r/docker/comments/unghjr/how_do_i_install_docker_on_termux/

```

pkg install root-repo
pkg install docker

```

- 换一种方式可行：proot-distro

- proot-distro 工具安裝Linux發行版

```

# 安装 proot-distro

pkg install proot-distro

# 安装 Ubuntu

proot-distro install ubuntu

# 登录 Ubuntu

proot-distro login ubuntu

# 在 Ubuntu 中安装 Docker

apt update
apt install docker.io

```

qemu 虚拟新 Linux 环境，确实可解。。

但看到 arm64 手机，虚拟 arm64 环境，比虚拟 x86-64 还慢 2 ~ 4 倍

# 相关文档

<strong>文档相关</strong>

- [Termux 官网](https://termux.com/)

- [Github 项目地址](https://github.com/termux/termux-app)

- [官方英文 WiKi 文档](https://wiki.termux.com/wiki/Main_Page)

<strong>下载地址</strong>

- [F-Droid 下载地址](https://f-droid.org/packages/com.termux/)

- [Google Play 下载地址](https://play.google.com/store/apps/details?id=com.termux)

- [酷安 下载地址](https://www.coolapk.com/apk/com.termux)

<strong>第三方教程</strong>

- Termux 高级终端安装使用配置教程：https://www.sqlsec.com/2018/05/termux.html

```
