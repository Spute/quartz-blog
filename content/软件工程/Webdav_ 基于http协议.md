---
title: Webdav-- 基于 http 协议
---

# webdav 协议

是什么？

基于 http 协议的拓展更多的请求方法。

WebDAV （Web-based Distributed Authoring and Versioning） 一种基于 HTTP 1.1 协议的通信协议。它扩展了 HTTP 1.1，在 GET、POST、HEAD 等几个 HTTP 标准方法以外添加了一些新的方法，使应用程序可对 Web Server 直接读写，并支持写文件锁定(Locking)及解锁(Unlock)，还可以支持文件的版本控制。

上传下载，类似 anyshare 软件的功能。

使用场景：

CMS 系统的实现

部分网盘软件支持 WebDAV 协议，如坚果。。。等

# webdav 服务端

选择 python 开发的 wsgidav 项目。

# webdav 客户端

支持 webdav 协议的客户端。

- 安卓端

mixplorer：安卓端。支持 webdav 协议。允许作为客户端，也可以作为一个 webdav 服务器。开启 webdav server 后可以正常使用，可是过段时间会自动终止掉。
