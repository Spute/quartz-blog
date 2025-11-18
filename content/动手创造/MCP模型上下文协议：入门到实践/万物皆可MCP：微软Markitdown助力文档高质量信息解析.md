---
title: 万物皆可 MCP--微软 Markitdown 助力文档高质量信息解析
---

# 是什么

微软的 MarkItDown MCP 支持将的一系列文档转换为 Markdown 文档格式。

为什么 markdown 格式非常适合大模型？主要是：

- markdown 格式非常简洁明了，同时具备层级结构。
- 一个是因为 markdown 对于 AI 大模型来说是非常容易理解的一种格式，很多提示词使用 markdown 写的就能证明这一点。据说 AI 大模型使用的训练语料中大部分是 markdown 的格式。

项目地址： [https://github.com/microsoft/markitdown](https://github.com/microsoft/markitdown)

mcp 服务地址： [https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp)

以下格式文件都支持转换成 md 格式

![[SYFsbGSo8op1CLxZcyycrs70nRf.png]]

# 效果展示

以下是测试文件

![[V7uObKGiaoZnjzxwIdccsNifnDg.png]]

使用 uri 描述资源地址，我以 file 协议描述为例，让 AI 调用这个工具将这个本地文件转换为 md 格式

![[A9hjbHCx8otyPDxbZKQcQ9J9nth.png]]

# 步骤

使用以下指令先安装好 mcp 服务的本地运行环境。需要先安装 3.10 以上的 Python 版本。

```
# 安装
pip install markitdown-mcp

# 运行
markitdown-mcp --sse --host 127.0.0.1 --port 3001
```

运行成功后的效果如下：

![[DKIFbgOUWo21qpx91StcOLQPnke.png]]

然后在 CherryStudio 新增配置，区别于之前，我这次使用的是 sse 的通讯方式（之前使用的是 stdio）

![[SaRdbPji1o8BxoxgvJec4zU0n7b.png]]
