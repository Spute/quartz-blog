---
title: 万物皆可 MCP--claude 桌面端 MCP
---

# Claude 桌面端 MCP 安装配置

claude 作为一个强大的 AI 大模型，每日有一定免费额度，其桌面端也支持 MCP，免费用户即可使用。今天教大家如何薅下羊毛。

## 配置步骤

1. 下载安装桌面软件，下载地址：https://claude.ai/download
2. 打开 mcp 配置文件，如下步骤操作

![[JuvHbaUaeoJ5ZaxPESzcIN5unbc.gif]]

1. 添加对应的 mcp 服务配置，以 playwright 为例，就需要在以上配置文件中增加以下内容：

```
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@executeautomation/playwright-mcp-server"]
    }
  }
}
```

1. 重启 claude 客户端，注意要退出最小化的后台程序才算退出。

![[ExZcbisknonhpyxZnD5cjZSCnzd.png]]

1. 配置成功后会多出以下两个图标，然后就可以直接对话调用工具了。

![[AT5Nb112goyRr8xKZV4cPeGtndh.png]]

# 复杂任务 Claude 模型也可以胜任

昨天的使用阿里千问调用 playwright 浏览器 MCP 服务时，效果不是很好，有时会执行失败。今天我们换成 claude 这个 AI 模型，来对比一下效果。

之前有提到过 MCP 是由 Anthropic 公司推出的协议，而 Claude 作为 Anthropic 公司的 AI 大模型。今天动手测试一下效果如何。

我使用的是 claude 的桌面应用作为 mcp 客户端，免费的 Claude 账号每日都有一定额度，同时支持 MCP 调用。

## 导航测试

使用与昨天相同的任务描述，第一次就直接成功了，效果如下：

![[DtQRbAouzo4A5gxKBdccSaEznjc.gif]]

## 进阶测试：搜索 + 截图

为测试它的能力上限，我提高了任务难度，在导航的基础上，要求在搜索栏搜索，并将结果截图保存。这可以是多步骤任务，惊喜的是 claude 都顺利完成了。牛批！

![[Sd2VblPmvoCrERxyyD1cwPYrnDh.gif]]

## 小结

使用 claude 操作工具的效果明显强于其他 AI 模型，即使复杂的多步任务，它也可以顺利完成。为什么不同 AI 模型在调用 MCP 工具的效果会存在差异，主要的影响因素是什么？我的猜测可能是：

- AI 模型的能力。主要与其理解能力和训练数据相关
- MCP 工具的适配性。playwright 工具是一个国外开源项目，可能它对国内的模型支持不够好。后面研究一下如何手撸一个 mcp 理解一下它是如何工作的。
