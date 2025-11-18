---
title: HTTP 请求生命周期
---

# 前沿

- 客户端：浏览器，app
- 中间设备：
- 服务端：

  - 网关：根据客户端请求的 api 转发到不同的 webserver 进程
  - 代理服务器：具有节省 IP 资源、缓存、内容过滤、访问控制管理等功能。一般是基于 HTTP 协议的代理所以处于 ISO 网络七层模型的应用层。
  - webserver：如：uwsgi
  - worker_process: web application
  - servlet(类似 django 的 view)

# 网关

- 前提：这里的“网关”均指 TCP/IP 协议下的网关，也是最常用的网关。
- 那么网关到底是什么呢？网关实质上是一个网络<strong>通向其他网络的 IP 地址</strong>。比如有网络 A 和网络 B，网络 A 的 IP 地址范围为“192.168.1.1 ~ 192.168.1.254”，子网掩码为 255.255.255.0；网络 B 的 IP 地址范围为“192.168.2.1 ~ 192.168.2.254”，子网掩码为 255.255.255.0。在没有路由器的情况下，两个网络之间是不能进行 TCP/IP 通信的，即使是两个网络连接在同一台交换机（或集线器）上，TCP/IP 协议也会根据子网掩码（255.255.255.0）与主机的 IP 地址作 “与” 运算的结果不同判定两个网络中的主机处在不同的网络里。而要实现这两个网络之间的通信，则必须通过网关。如果网络 A 中的主机发现数据包的目的主机不在本地网络中，就把数据包转发给它自己的网关，再由网关转发给网络 B 的网关，网络 B 的网关再转发给网络 B 的某个主机。这就是网络 A 向网络 B 转发数据包的过程。
- 所以说，只有设置好网关的 IP 地址，TCP/IP 协议才能实现不同网络之间的相互通信。那么这个 IP 地址是哪台机器的 IP 地址呢？网关的 IP 地址是具有路由功能的设备的 IP 地址，
- 具有路由功能的设备有

  - 路由器
  - 启用了路由协议的服务器（实质上相当于一台路由器）
  - 代理服务器（也相当于一台路由器）。

# <strong> uwsgi</strong>

- 而 uWSGI 是实现了 uwsgi 和 WSGI 两种协议的 Web 服务器.
- `uWSGI` 服务器自己实现了基于 `uwsgi` 协议的 `server` 部分，我们只需要在 `uwsgi` 的配置文件中指定 `application` 的地址，`uWSGI` 就能直接和应用框架中的 `WSGI application` 通信。
- WSGI，全称 Web Server Gateway Interface，一种通讯协议，是为 Web 服务器和 Web 应用程序或框架之间的一种简单而通用的接口协议。
- 网关。网关的作用就是在协议之间进行转换
- web 服务器无法直接与 Django 应用框架通信，需要使用 uWSGI 服务
- uWSGI 是一种 WSGI 实现。在这个教程中，我们将设置 uWSGI，让它创建一个 Unix socket，并且通过 WSGI 协议提供响应到 web 服务器
- uWSGI 项目是一个旨在构建一个全栈的托管服务。使用通用的 API 和通用的配置风格来实现应用服务器 (对于各种编程语言和协议，如 python 应用，perl 应用，ruby 应用)，代理，进程管理器和监控器。
- uwsgi 与 manage.py runserver 的对比。

  - 两者都能实现将 http request 装换为 python，如 http 的请求头转换成 python 的 k-v 字典
  - 前者专注于生产环境，后者被用于开发环境
  - uWSGI 服务具备 manage.py 缺失的功能
    - 进程管理：可以启用多个应用服务实例，利用服务器的多核资源
    - 监控功能：日志更完善
    - 设计和维护都考虑到了安全性

# web 服务器

## Django

- process_view()
- process_exception()
- process_template_response()
- 启动 app 函数 django.setup()
- authentication 触发的时期是

  - django 原生认证机制和 DRF 的认证机制有何不同
- CSRF

  - 基于会话机制
- django 的 View 类与 DRF 的 APIView 类

  - 重写了 as_view()方法

<table>
<tr>
<td>类型<br/></td><td>django的View类<br/></td><td>DRF的APIView类<br/></td><td>备注<br/></td></tr>
<tr>
<td>as_view方法<br/></td><td><br/></td><td><br/></td><td><br/></td></tr>
<tr>
<td>csrf豁免<br/></td><td><br/></td><td>是<br/></td><td><br/></td></tr>
</table>

- WSGIRequest 与 HttpRequest，实例化 WSGIRequest 时初始化数据
