---
alias: " hyh0v1dcr1503fa8v0nd"
date: 2026-03-02
title: python抓包工具：mitmproxy
publish: "true"
category: 实践记录
tags:
---

## 前言

之前受一个博主推荐，就关注这个 python 的抓包工具。最近有个需求，才想起拿来用一下。

## 概念

是什么？

MITM 代表 Man-in-the-Middle（中间人攻击），是一种网络攻击形式，在这种攻击中，攻击者能够拦截和截取双方之间的通信。MITM 攻击通常发生在受害者与目标之间的通信路径中，并允许攻击者窃听、篡改或伪造通信。

## 安装 mitmproxy

相关文档：[https://docs.mitmproxy.org/stable/overview/installation/](https://docs.mitmproxy.org/stable/overview/installation/)

- 使用 pip 安装。[https://docs.mitmproxy.org/stable/overview/installation/](https://docs.mitmproxy.org/stable/overview/installation/)
- 使用仓库源安装的方式，参考：[CONTRIBUTING.md](https://github.com/mitmproxy/mitmproxy/blob/main/CONTRIBUTING.md) 。

```
venv/bin/pip install -e ".[dev]"
```

## 支持 https 请求

- mitmproxy CA 证书在首次启动 mitmproxy 时生成后位于~/.mitmproxy 中。`cat ~/.mitmproxy/mitmproxy-ca-cert.pem`
- 只需要 mitmproxy 配置正确的证书就行。客户端（如 curl、requests）不需指定证书。
- 如果 mitmproxy 未自动生成证书。可以将 mitmproxy 证书安装到系统信任存储中，你主要需要使用 .crt 或 .pem 格式的证书文件。具体来说：

```
# 1. 复制 mitmproxy-ca-cert.pem 到证书目录
sudo cp ~/.mitmproxy/mitmproxy-ca-cert.pem /usr/local/share/ca-certificates/mitmproxy-ca-cert.crt

# 2. 更新系统证书存储
sudo update-ca-certificates
```

- 其中 mitmproxy-ca-cert.pem 是主要需要的文件，包含 PEM 格式的 CA 证书。

## 案例：抓取 requests 请求

- 必须使用 verify 去信任 mitmproxy 使用的证书

```
import os
import requests
# 设置代理配置
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}
# 方式 1: 在 requests 中直接使用代理
response = requests.get('https://baidu.com', proxies=proxies,verify='/home/news_yu/.mitmproxy/mitmproxy-ca-cert.pem')
```

## 案例：mitmproxy 抓微信公众号

- 安装 mitmproxy
- 使用 mitmweb 命令启动 web 服务
- 设置系统代理
- 引导下载 CA 证书
- 安装 CA 证书到 windows 系统中
- 在微信桌面端打开微信公众号文章
- 在 mitmweb 页面查看抓包数据

~~按理说我啥都可以抓取到了，包含微信视频号的视频。~~
因为公众号有web端，是基于浏览器的，对代理证书要求不高。相对的一些桌面应用（如微信）并不信任mitmproxy的代理证书，就会导致无法抓取。。。

## 抓取浏览器包
使用mitmweb命令启动web界面
![[Pasted image 20260312134803.png]]
配置电脑代理，这里的端口要与mitmweb监听的一致。
默认8080为代理端口，8081为web客户端端口
![[Pasted image 20260312125240.png]]

只能抓取http，无对https请求进行抓取

### 安装mitproxy证书
![[Pasted image 20260312135053.png]]

安装mitproxy证书是提示 If you can see this, traffic is not passing through mitmproxy.

异常描述  
当浏览器访问http://mitm.it/出现If you can see this, traffic is not passing through mitmproxy. 时证明它没有检测到当前操作经过了mitmproxy。

可能因为以下原因：  
1、未启动mitmproxy -> 直接在命令行输入mitmproxy启动代理  
2、没有配置系统或浏览器的代理，mitmproxy和fiddler有所区别，不能在不配置代理的情况下完成监听  
3、端口冲突。使用mitmproxy -p 端口号启用指定端口的监听  
4、**可能因为一些杂七杂八的浏览器配置所影响，使用无痕模式试试(本次就出现了这情况，研究半天发现无痕模式和Safari可正常访问)**  
5、可以装一个SwitchyOmega插件，省事一键使用系统代理或选择自己配置的浏览器代理

### window安装代理证书

windows 系统安装说明：

- 1.双击下载的文件，开始导入证书  
    ![](https://img2023.cnblogs.com/blog/1070438/202212/1070438-20221215131317913-252040091.png)
    
- 2.选择一个证书文件存储位置（本地计算机），然后下一步  
    ![](https://img2023.cnblogs.com/blog/1070438/202212/1070438-20221215131332691-2049713967.png)
    
- 3.输入密码界面，直接留空白，下一步  
    ![](https://img2023.cnblogs.com/blog/1070438/202212/1070438-20221215131353948-1601395598.png)
    
- 4.选择“将所有证书放置在以下存储”，然后单击“浏览”，然后选择“受信任的根证书颁发机构”。下一步  
    ![](https://img2023.cnblogs.com/blog/1070438/202212/1070438-20221215131445935-1066422729.png)
    
- 5.点完成  
    ![](https://img2023.cnblogs.com/blog/1070438/202212/1070438-20221215131459012-402011518.png)
    
- 6.导入成功点确定  
    ![](https://img2023.cnblogs.com/blog/1070438/202212/1070438-20221215131558207-440042328.png)

## 爬取小程序

PC 微信抓包 SSL Pinning 记录

在用 mitmproxy 抓 PC 微信时，HTTPS 请求无法被解析。日志显示多次 TLS 握手失败，如 `Certificate verify failed`，连接随即断开。分析原因，微信客户端启用了 **SSL Pinning**，即内部校验服务器证书指纹。mitmproxy 替换证书后，指纹不匹配，客户端主动断开连接。结果是代理虽能接管连接，但无法解密 HTTPS 流量，也看不到具体 HTTP 请求。
结论：遇到 TLS 快速断开且无 HTTP 内容，几乎可以确定是 SSL Pinning 导致抓包失败。后续分析需考虑绕过该机制或从小程序、网页接口入手。

mitmproxy 适用于抓取和调试 HTTP/HTTPS 接口，如浏览器请求、API 调试、爬虫分析等场景。它通过中间人代理解析流量，支持修改请求与响应。但其前提是**流量必须经过代理且客户端信任代理证书**；若程序绕过系统代理、使用 HTTP/3 或启用 SSL Pinning，则可能无法抓取或解密流量。

目前没有找到合适的方法

## 资料

- [https://www.mitmproxy.org/](https://www.mitmproxy.org/)
- [https://github.com/mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)
