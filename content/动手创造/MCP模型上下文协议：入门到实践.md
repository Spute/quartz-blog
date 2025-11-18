---
title: MCP 模型上下文协议--入门到实践
---

# 前言

今天看到一个，是使用 MCP 让 Claude 可以直接控制 Blender 的案例，被震惊到了。

使用提示词就能创建漂亮的 3D 场景，如下视频，是一个“低多边形龙守护宝藏”场景的演示。

MCP 隐隐成为一个趋势。随着更多企业（如 Spring AI、Cursor）的实践应用，MCP 或将成为 AI 工具集成领域的潜在标准。

# 是什么？

你可以把 MCP 想象成 AI 领域的 type c 接口，它能让不同的 AI 大模型与外部工具和数据源轻松连接。

![[MOPDbh9Z5o1XSsxVlXocwE7Ynof.png]]

它是一种开放协议，是对 AI 大模型与外部系统集成的标准化。

由 Anthropic 于 2024 年推出协议，借鉴微软语言服务器协议（LSP）的设计理念，目标是<strong>构建一个“AI 原生”的通用接口，简化 LLM 与外部资源的交互流程</strong>。其核心价值在于构建开放、可扩展的智能体交互框架。

## 特点

- 统一协议，MCP 就像一个统一的接口，他只需要一次整合就能支持多个服务
- 第二点是动态发现，AI 模型能够自动识别可用的工具，不用去提前规划好后写死每一个接口
- 双向通讯，相对于传统的 API 只能用从客户端向服务端发起请求的限制，就是 MP 支持类似 websocket 的实时双向通讯，适用于更多的场景。

## 出现的背景是什么？是为了解决什么问题？

随着 AI 技术发展，智能体（Agent）需要频繁访问外部工具。传统 AI 集成方式存在以下问题，于是有了 MCP：

- <strong>数据孤岛与重复开发</strong>：每个新数据源的接入需单独开发连接器，导致开发成本高、扩展性差。
- <strong>复杂性与兼容性问题</strong>：传统 API（如 OpenAPI、GraphQL）需为不同服务编写定制代码，且不同服务接口差异大，增加了集成复杂度。
- <strong>动态交互需求不足</strong>：现有协议（如 Function Calling）多为一次性调用，缺乏实时双向通信能力，难以支持复杂场景的上下文感知。

## 与旧有方案对比，有什么优势和劣势？

<strong>优势</strong>

- <strong>开发效率提升</strong>：传统 API 需为每个服务单独开发，而 MCP 通过单一协议集成多个工具，减少重复劳动。
- <strong>动态性与灵活性</strong>：相比静态集成的 OpenAPI，MCP 支持实时上下文更新和工具动态发现，更适应复杂场景。
- <strong>生态扩展性</strong>：MCP 服务器可独立部署，开发者通过扩展服务器即可接入新功能，无需修改核心代码。
- <strong>降低技术门槛</strong>：非开发者可通过配置而非编程实现工具集成，例如通过 MCP 服务器连接日历和邮件服务。

<strong>劣势</strong>

- <strong>生态依赖性强</strong>：主流 LLM 服务商（如 OpenAI、Grok）尚未全面支持 MCP，协议普及需依赖行业协作。
- <strong>性能与复杂性争议</strong>：部分开发者认为 MCP 可能增加协议层复杂度，实际性能优化可能不及紧密耦合的系统。
- <strong>定制化限制</strong>：在需要高度特定功能或严格控制的场景中，MCP 的通用性可能导致灵活性不足。

## <strong>通讯类型：</strong>

- <strong>STDIO（标准输入/输出）</strong>：<strong>通过子进程方式调用处理脚本</strong>，通过标准输入（stdin）和标准输出（stdout）与其通信。
- <strong>SSE（Server-Sent Events）</strong>：SSE（Server-Sent Events）是基于 HTTP 长连接实现的一种服务器主动推送机制。客户端发起一个 HTTP 请求，<strong>服务器保持连接不关闭</strong>，并不断向客户端 <strong>以文本格式推送事件数据</strong>，像 <strong>广播</strong>，服务器不断往外推送数据，客户端只能被动接收。

## 资料

mpc 官网：[https://modelcontextprotocol.io/introduction](https://modelcontextprotocol.io/introduction)

最大的 mcp 托管网站：https://smithery.ai/

托管网站：https://mcp.so/ MCP.so 是国内开发者 idoubi 创建的 MCP（模型上下文协议）服务器导航与托管平台。 MCP.so 收录了超过 3000 个 MCP 服务器。

Cherry-studio：[https://docs.cherry-ai.com/advanced-basic/mcp](https://docs.cherry-ai.com/advanced-basic/mcp)

# MCP 核心架构

- MCP 主机（MCP Hosts）：发起请求的 LLM 应用程序（例如 Claude Desktop、IDE 或 AI 工具）。
- MCP 客户端（MCP Clients）：在主机程序内部，与 MCP server 保持连接。
- MCP 服务器（MCP Servers）：为 MCP client 提供上下文、工具和 prompt 信息。
- 本地资源（Local Resources）：本地计算机中可供 MCP server 安全访问的资源（例如文件、数据库）。
- 远程资源（Remote Resources）：MCP server 可以连接到的远程资源（例如通过 API）。

![[XoN3bFfy6o4nrXxj89lc6jb3nQe.png]]

## 交互流程

MCP client 充当 LLM 和 MCP server 之间的桥梁，MCP client 的工作流程如下：

1. MCP client 首先从 MCP server 获取可用的工具列表。
2. 将用户的查询连同<strong>工具描述</strong>通过 function calling 一起发送给 LLM。
3. LLM 决定是否需要使用工具以及使用哪些工具。
4. 如果需要使用工具，MCP client 会通过 MCP server 执行相应的工具调用。
5. 工具调用的结果会被发送回 LLM。
6. LLM 基于所有信息生成自然语言响应。
7. 最后将响应展示给用户。

![[PScjbApK4ojTxDxznhdcqCqxntd.png]]

## 构建 MCP Server

MCP Server 是 MCP 架构中的关键组件，它可以提供 3 种主要类型的功能：

- 资源（Resources）：类似文件的数据，可以被客户端读取，如 API 响应或文件内容。
- 工具（Tools）：可以被 LLM 调用的函数（需要用户批准）。
- 提示（Prompts）：预先编写的模板，帮助用户完成特定任务。

这些功能使 MCP server 能够为 AI 应用提供丰富的上下文信息和操作能力，从而增强 LLM 的实用性和灵活性。

AI 应用的开发更多的是需要编写的不同的 MCP Server，因为 MCP Client 相对固定，且有很多现成的工具实现了这一部分。，不同的业务场景需要使用不同的工具和资源，意味着需要开发出各种各样的 MCP server，来为大模型提供工具和资源。

因此了解 MCP Server 的开发流程很有价值。

# 实践：最小的 MCP Server 样例

学习新东西，最好先从最小且必要的开始。以下就是 mcp 的 python SDK 中 Quickstart 的样例：

## 安装环境

推荐使用 uv 来进行 python 项目管理

```
# 安装uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 创建名为“mcp-server-demo”的项目
uv init mcp-server-demo

# 进入项目根目录
cd mcp-server-demo

# 创建虚拟环境venv
uv venv

# 进入项目虚拟环境
source .venv/bin/activate

# 安装项目依赖包
uv add "mcp[cli]"
```

## 新增 server 代码文件

创建 server.py 文件，添加以下代码。

代码来源：[https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file)

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

## 调试

为了调试，运行以下命令，使用 MCP Inspector 来运行 MCP 服务器。

MCP Insepector 会提供一个直观的调试页面，

```
mcp dev server.py
```

运行成功后会输出类似： MCP Inspector is up and running at [http://127.0.0.1](http://127.0.0.1:6274) ，浏览器访问地址这个地址，可以看到如下页面，然后依次点开：Connect》Tools，即可查看到当前 mcp server 拥有的一个名为“add”的工具。

![[TPPZboc1eofyJTxCczecUhX2nYg.png]]

# 打包发布 MCP Server

前面我们打造了一个 mcp server。经过测试可以在本地运行。但这只能给自己使用，如果想要供其他人使用，就需要把这个 mcp 服务打包发布到 pypi 网站（一个托管 python 软件包的网站）。

以下是相关的流程：

### 准备 pypi 的 api token

登录<u>ht</u><u>tps://pypi.org/manage/account</u> 获取 API token。如果没账号需要先注册，然后在邮箱激活，添加 2FA 双因素验证后，才能创建 API Token。这一步是必须的，因为现在发布 pypi 已经禁止使用账号密码了，只能使用 api token 了。

### 构建项目

在项目根目录下使用“uv build”命令打包项目。执行成功后会多出一个 dist 文件夹。里面放的就是打包好的项目。

![[Jee2bMoSXoqtTGx0aepcoo1on6d.png]]

### 发布项目

然后使用“uv publish dist/*”命令发布项目，过程会需要验证身份，因为使用的 api token，所以用户名使用“__token__”密码使用前面获取的 api token。

![[KLCzb2A30oxTCOxjjsYcVxfSnQe.png]]

### 查看项目

发布成功后，登录 pypi 账号即可查看，刚刚发布的项目有了，在搜索栏也能搜的到了。

![[Lwshbb8x7oScJvxZgDTc0CxnnRd.png]]

![[LMDobzFpcoOaMPxaa5mc4tgZnjh.png]]

### <strong>创建 Tools 技巧</strong>

- 提供清晰、描述性的名称和说明
- 使用详细的 JSON Schema 定义参数
- 在工具描述中包含示例，告诉模型应如何使用它们
- 实施适当的错误处理和验证
- 对长时间操作使用进度报告
- 保持工具操作集中且原子化
- 记录预期返回结果
- 实施适当的超时
- 考虑对资源密集型操作进行速率限制
- 用于调试和监控的日志工具使用情况

参考：[https://www.cnblogs.com/ryanzheng/p/18803768](https://www.cnblogs.com/ryanzheng/p/18803768)
