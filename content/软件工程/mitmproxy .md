---
title: mitmproxy
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

按理说我啥都可以抓取到了，包含微信视频号的视频。

## 资料

- [https://www.mitmproxy.org/](https://www.mitmproxy.org/)
- [https://github.com/mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)
