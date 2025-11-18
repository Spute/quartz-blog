---
title: clash 代理原理梳理
---

## 请求流程图

下面是使用 Clash 模拟访问 Google 的一个完整流程

![[FZFubpNTqoMA1QxF1BGc6PK6noe.png]]

## 知识点

DoH/DoT：可避免 DNS 被污染、被拦截、IP 被劫持等问题

DNS over TLS（<strong>DoT</strong>）和 DNS over HTTPS（<strong>DoH</strong>）是两种<strong>加密 DNS 查询的协议</strong>，用来防止 DNS 被篡改或监听。

## 问题：访问不到代理节点的真实 IP

验证，发现打开代理后，无法连接上代理节点。。。

使用 DoH/DoT 也是不行

![[JRsobFQWBoBxWAxrAGxclV7Vnph.jpg]]

手动添加 hosts(临时办法，因为 Cloudflare 的 ip 会变动)：

```
hosts:
  rack-nerd.520233.best: 104.21.61.101  # 你当前查询到的IP
```

尝试：

- 修改 rule 让代理节点域名直连不行
- 修改对抗 DNS 防污染中域名配置也不行。。。
