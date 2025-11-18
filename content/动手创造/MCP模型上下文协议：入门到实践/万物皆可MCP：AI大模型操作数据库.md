---
title: 万物皆可 MCP--AI 大模型操作数据库
---

数据的重要性不言而喻，数据库作为数据持久化存储的成熟方案，已然成为软件应用的核心构成部分。

MCP 作为可以让 AI 大模型快速集成各种工具的连接协议。让 AI 大模型具备操作数据库的能力必然是不能缺失的。这节我们以 sqlite 数据库为例，演示如何使用 MCP 协议让大模型操作数据库，你会发现这个过程是如此简单方便。

除了 sqlite 数据库，还有 MySQL，PostgreSQL 等数据库拥有对应的 MCP 服务器，想要进一步研究可以在以下两个 MCP server 导航网站查找相关配置。

- https://mcp.so/
- https://smithery.ai/

## 配置步骤

我们选择的是支持 MCP 的 AI 客户端 CherryStudio，找到配置页面，按如下图配置即可。

这里解释一下配置中参数的相关含义：

- 第一个行表示的是这个 mcp 服务的安装包名，是固定的
- 第 2 和 3 行是起到的是指定 sqlite 数据库的作用，其中第二行的参数名，保持固定；第三行是 sqlite 数据库文档的路径，这部分可根据个人情况进行修改

```
mcp-server-sqlite
--db-path
D:\coding\test.db
```

![[O948bdcQHotnQBxSLo7cKZ1Pnsh.png]]

## 效果展示

如下是配置好后，在对话页面让大模型查询和往数据库中写入数据的示例

![[ItZ8bI33Woz2rkxQ8qQcJ5eBndh.png]]
