---
title: 万物皆可 MCP--AI 操作浏览器
---

基于 playwright 工具，让 AI 方便地操作浏览器，支持导航、截屏、点击输入等功能。这也是 manus 的核心能力之一。今天我一起来在自己电脑本地实现一下。

项目地址：[https://github.com/executeautomation/mcp-playwright?tab=readme-ov-file](https://github.com/executeautomation/mcp-playwright?tab=readme-ov-file)

## 效果演示

如下是使用阿里的千问大模型使用这个 mcp 浏览器工具的效果。我是进行了两次对话，第一次打开了浏览器，但是并没有导航到我要求的 B 站。重试一遍后才成功导航到 B 站了。这个看起来并不稳定，可能和模型能力有关，后面有时间我再尝试使用 claude 试试，毕竟 mcp 就 anthropic 公司推出的，他家的 claude 大模型理论上对 mcp 的支持是最好的。

![[XwHhbBCgzo3NmUxqquEcYJKknxh.gif]]

## 配置步骤

1. 使用如下命令全局安装这 mcp 服务包 `npm install -g @executeautomation/playwright-mcp-server`
2. 在 CherryStudio 客户端配置 mcp 服务

![[MVqCb4k0AoAKgUxWvR0cOgSenkf.png]]

- 命令：npx
- 参数：

  - -y
  - @executeautomation/playwright-mcp-server
