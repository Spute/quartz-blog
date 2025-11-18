---
title: 万物皆可 MCP--AI 大模型获取时间
---

AI 大模型虽然很强大，但是它的知识是静态，在完成训练后就固定下来了。所以实时获取时间这样看起来很简单的需求它并不能直接完成。

就像下面如下情况（没有使用工具）：

![[WDxBbG8mYooc5bxjnlHcTnhKnxg.png]]

AI 大模型要实现这个功能，就需要利用它的函数调用能力去使用外部工具来获取实时数据。可不同的大模型调用工具的方式、使用的参数存在差异，导致调用工具很麻烦。

于是有了 MCP 出现，它让 AI 大模型调用工具版变得方便统一。

如下就是大模型通过与时间 mcp 服务交互获取当前时间定位案例。

![[KC6nbvuL6oDfSbxl9C3cIinonPc.png]]

只需简单的配置就能让所有 AI 大模型都能调用这个工具。如下图，我以 CherryStudio 这个 AI 助手平台为例，新增 mcp 服务，添加好命令和参数，点击保存即可。

![[StStbbCrUouhzcxlbXdcVbDEn3g.png]]

然后切换到聊天页面，打开 mcp 服务开关，即可让 AI 大模型实时获取当前时间。

![[MRv6bv2SToDwSLxivZtcV7GLnXr.png]]
