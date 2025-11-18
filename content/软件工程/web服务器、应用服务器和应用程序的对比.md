---
title: web 服务器、应用服务器和应用程序的对比
---

# 举几个例子？

web 服务器：Nginx、Apache

应用服务器：Tomcat、Node.js、uWSGI、Gunicorn。

应用程序：由 Flask、Django 框架编写的程序

# 作用分别是？

Web 服务器： 它主要负责处理来自客户端（通常是浏览器）的 HTTP 请求，并返回相应的 HTTP 响应。Web 服务器的作用是处理静态内容，如 HTML、CSS 和图像文件。

应用服务器： 应用服务器位于 Web 服务器和应用程序之间，主要用于处理动态内容和业务逻辑。它接收从 Web 服务器传递过来的请求，然后与应用程序交互，执行必要的操作，最后将结果返回给 Web 服务器。

应用程序：这是实际执行特定任务或提供特定服务的软件。

# 三者为啥会拆分开来？

拆分的目的是为了解耦，不同部分发挥不同的作用，相互独立，减少调整的影响。

应用程序主要是实现业务功能，改动可能性最大。应用服务器与 web 服务器就相对少改进。

# WSGI、uWSGI 和 uwsgi 是什么？

- WSGI 是一种 Python Web 服务器网关接口。它定义了 Web 服务器如何与应用程序进行通信的规范。比如：uWSGI 服务与 django 应用程序的通讯。
- uwsgi 是一种通信协议，uwsgi 协议定义了 Web 服务器和应用服务器之间的通信协议。如：nginx 与 uWSGI
- uWSGI 是一种 Web 服务器，它支持多种编程语言，包括 Python。它可以与多种 Web 服务器配合使用，如 Nginx、Apache 等。用于连接 Python Web 应用程序和 Web 服务器。

## 他们之间的联系是？

uWSGI 服务器可以使用 uwsgi 协议来与 Web 服务器进行通信；并实现 WSGI 规范，连接 Python Web 应用程序。

## 可以让客户端的请求直接由应用服务器处理吗？接入 Web 服务器的意义是？

- 在开发模式下，如：python manage.py runserver 命令就是让应用程序与客户端直接连接
- 性能和负载均衡： Web 服务器可以处理大量的并发请求；具备负载均衡的能力，可以将请求分发到不同应用服务器上。
- 安全性： Web 服务器可以提供一层额外的安全性，通过配置防火墙、SSL 证书等来保护应用程序免受攻击。反向代理：隐藏应用服务器的实际位置，提高系统的安全性，并允许更灵活的架构设计。
- 具备路径分发功能，可以将请求分发到不同的后端服务或应用程序，简化域名管理和统一访问入口

## 那应用服务器是否可以省略，让 web 服务器直接转发到应用程序？如果可以接入应用服务器的意义是什么？

1. 稳定性：应用服务器可以将请求转发给多个应用程序实例，从而提高稳定性和可靠性。当一个应用程序实例崩溃或出现问题时，其他实例可以继续处理请求，从而保证服务的可用性。
2. 性能：uWSGI 服务器是一个高性能的应用服务器，可以快速处理请求，并支持多种高级功能，如负载均衡、自动扩容等。
3. 扩展性：uWSGI 服务器支持多种编程语言和框架，如 Python、Django、Flask 等，可以轻松扩展到更多的应用程序。
   web 服务器与应用服务器都具备负载均衡，不同的是处于不同层面的负载均衡，可以进行不同颗粒度的负载均衡控制，分担服务器压力防止单个服务器负载。

## HTTPS 协议可以在哪些地方实现？

HTTPS 的实现通常在 Web 服务器层面进行，因为它涉及到加密通信和处理 SSL/TLS 协议。替换其他两者不太现实，因为它们各自有不同的职责和功能。

# django 的 runserver 与 shell 命令

runserver 与使用 wsgi.py 的区别？

runserver 会多启动一个 httpd 的开发服务器，类似于简化版的 uWSGI 服务器

以下是 runserver 简化版：

```
from django.core.management.commands.runserver import Command as RunserverCommand

class Command(RunserverCommand):

    help = "Starts a lightweight Web server for development."

    def handle(self, *args, **options):

        # 调用 django.setup() 方法

        django.setup()

        # 获取主机和端口

        addr = options['addr']

        port = options['port']

        # 启动开发服务器

        from django.core.servers.basehttp import run

        run(addr, int(port), self.inner_run)

    def inner_run(self, *args, **kwargs):

        # 处理请求的内部方法

        # 这里会调用 Django 的 WSGI 应用来处理请求

        from django.core.wsgi import get_wsgi_application

        application = get_wsgi_application()

        server_address = (kwargs['host'], kwargs['port'])

        httpd = self.get_httpd(application, server_address)

        httpd.serve_forever()

    def get_httpd(self, application, server_address):

        from django.core.servers.basehttp import WSGIServer

        return WSGIServer(server_address, application)
```

# shell 和 runserver 的区别？

runserver 命令不仅仅是调用 django.setup() 方法来配置 Django 环境，它还负责启动一个开发服务器，处理 HTTP 请求并返回响应。

shell 只会调用 django.setup()方法
