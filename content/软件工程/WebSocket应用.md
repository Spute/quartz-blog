---
title: WebSocket 应用
---

## 什么是 WebSocket

- 目标是提供一种服务器与浏览器间的双向通讯协议，而不是通过创建多个 http 连接进行轮询的方式实现。

## 应用场景

浏览器想订阅数据，但这类数据不知道服务器什么能准备好。此时需要服务器准备好后，主动推送给浏览器。

- 直播发弹幕。（弹幕就是这类浏览器需要订阅的数据）
- 多人游戏
- 浏览器需要下载一个大文件，服务端需要准备一定时间，准备好后服务器主动推送给浏览器

## 数据流

- Sec-WebSocket-Version：13
- [RFC 标准](https://www.rfc-editor.org/rfc/rfc6455)

## ws 握手

浏览器发起请求：

1 GET /chat HTTP/1.1

2 Host: server.example.com

3 Upgrade: websocket

4 Connection: Upgrade

5 Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==

6 Sec-WebSocket-Protocol: chat, superchat

7 Sec-WebSocket-Version: 13

8 Origin: [http://example.com](http://example.com)

熟悉 HTTP 的一眼就可以看出这段类似 HTTP 协议的握手请求中，多了 Upgrade、Connection、Sec-WebSocket-Key、Sec-WebSocket-Protocol、Sec-WebSocket-Version 几个属性。

```bash
1 Upgrade: websocket
2 Connection: Upgrade
这几个属性就是 WebSocket 的核心了，Upgrade：websocket属性通知 Apache 、 Nginx 等服务器，此次发起的请求要用 WebSocket 协议，而不是http。

1 Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==
2 Sec-WebSocket-Protocol: chat, superchat
3 Sec-WebSocket-Version: 13
Sec-WebSocket-Key 字段，它由客户端生成并发给服务端，用于证明服务端接收到的是一个可受信的连接握手，可以帮助服务端排除自身接收到的由非 WebSocket 客户端发起的连接，该值是一串随机经过 base64 编码的字符串。即该字段用于验证服务器端是否采用WebSocket 协议。
```

收到请求后，服务端做一次响应：

1 [http://www.liuxue1.com/](http://www.liuxue1.com/) 1.1 101 Switching Protocols

2 Upgrade: websocket

3 Connection: Upgrade

4 Sec-WebSocket-Accept: HSmrc0sMlYUkAGmm5OPpG2HaGWk=

5 Sec-WebSocket-Protocol: chat

响应里面重要的是 Sec-WebSocket-Accept ，服务端通过从客户端请求头中读取 Sec-WebSocket-Key 与一串全局唯一的标识字符串(俗称魔串)“258EAFA5-E914-47DA- 95CA-C5AB0DC85B11”做拼接，生成长度为 160 位的 SHA-1 字符串，然后进行 base64 编码。作为 Sec-WebSocket-Accept 的值回传给客户端。

此时成功建立了 WebSocket 连接，Upgrade：websocket 字段也标志着这里开始就是 HTTP 最后负责的区域了，通知客户端服务端已切换为 WebSocket 协议。至此，HTTP 已经完成它所有工作了，接下来就是完全按照 WebSocket 协议进行了。

## django 实现 WebSocket
