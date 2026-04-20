---
alias: " y82qmevgi20vmp4exmrt"
date: 2025-12-09
title: 命令行式 AI 编程革命 Claude Code
publish: "true"
category: 文章写作
tags:
  - 实践
  - 软件工程
---

## 是什么

Claude Code 是一个由 Anthropic 开发的<strong>基于终端的 AI 编码工具</strong>，基于 Claude 4 Sonnet 模型。它通过<strong>命令行界面（CLI）</strong>运行，允许开发者通过自然语言命令处理编码任务、Git 工作流和调试。它更适合需要深度项目上下文和复杂任务的场景，例如跨前端和后端的集成增强或自动化重复任务。

对应的 Cursor 是一个<strong>AI 代码编辑器</strong>，基于 Visual Studio Code（VS Code），通过实时代码建议、上下文感知的自动补全和项目索引增强开发者生产力。

<strong>Claude Code 特点是“问答式批量改写”，Cursor 则偏向“写代码时的随时辅助”</strong>

## linux安装 Claude Code
- 安装 Node.js（如已安装可跳过）

可参考[ 驱动 AI 项目：Node.js 版本管理利器 NVM 安装指南](https://iixchzsb7i.feishu.cn/wiki/P8skwk5yjiUIHDkNaI1cRIbJnDf)

- 设置国内 npm 镜像（提升安装速度）：

```bash
npm config set registry https://registry.npmmirror.com
```

- 安装（全局安装）：

```bash
npm install -g @anthropic-ai/claude-code
```

- 查看版本：

```bash
# 通过claude命令查询
news_yu@SZ-YUXINWEN-L1:~$ claude --version
1.0.83 (Claude Code)

# 通过npm查询
news_yu@SZ-YUXINWEN-L1:~$ npm list -g
/home/news_yu/.nvm/versions/node/v22.5.1/lib
├── @anthropic-ai/claude-code@1.0.83
```

---

## window下安装Claude Code

详细步骤可参考[官方文档](https://code.claude.com/docs/zh-CN/setup#%E6%A0%87%E5%87%86%E5%AE%89%E8%A3%85)。下面是“本机安装”方式的示例流程。

“本机安装”是官方推荐方案，相比 NPM 安装具有以下优势：

- 自包含的可执行文件
    
- 无需 Node.js 依赖
    
- 自动更新程序更稳定

### 安装git bash
这个工具对git有依赖，所以需要先下载，点击网站 [Git for Windows](https://git-scm.com/downloads/win)，找到对应版本下载（一本电脑都是x64内核），如下图，然后运行安装即可。
![[Pasted image 20251211095708.png]]

### 下载安装Claude Code

以管理员身份打开 PowerShell，执行以下命令并等待完成。当出现 “Installation complete!” 即表示安装成功：

```
irm https://claude.ai/install.ps1 | iex
```

![[Pasted image 20251210174927.png]]

### PowerShell 设置环境变量

安装 Claude Code 后，需要配置模型相关的环境变量。下面是 PowerShell 中查看、设置与持久化环境变量的常用方法。

#### 查看环境变量

查看所有环境变量：

```powershell
Get-ChildItem Env:
```

查看指定变量：

```powershell
$env:PATH
$env:JAVA_HOME
```

#### 设置临时环境变量

仅在当前 PowerShell 会话中有效，关闭窗口后失效。

设置变量：

```powershell
$env:MY_VAR = "hello"
```

追加 PATH：

```powershell
$env:PATH += ";C:\MyTools"
```

---

#### 设置永久环境变量

使用 .NET API 写入用户级环境变量，适用于长期配置：

```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://api.deepseek.com/anthropic", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_AUTH_TOKEN", "<你的密钥>", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_MODEL", "deepseek-chat", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_SMALL_FAST_MODEL", "deepseek-chat", "User")
```

设置完成后需重新打开一个新的 PowerShell 窗口才能生效。

---

### 验证

在新窗口中输入 `claude`，若弹出如下界面则说明安装成功：

![[Pasted image 20251211094108.png]]

## 添加到 VS Code

1. 打开 VSCode
2. 打开集成终端
3. 运行 `claude` - 扩展将自动安装

今后您也可以在任何外部终端中使用 `/ide` 命令连接到 IDE。

## 安装 Kimi K2 × Claude Code

### 注册 Kimi api

首先需要到 Kimi 官网申请一个 API：[https://platform.moonshot.cn/console/api-keys](https://link.zhihu.com/?target=https%3A//platform.moonshot.cn/console/api-keys)

点击新建 [API Key](https://zhida.zhihu.com/search?content_id=260315032&content_type=Article&match_order=1&q=API+Key&zhida_source=entity) 的蓝色按钮，名称随便写，项目选择默认即可。

创建完 API Key 后记得及时复制保存，因为只有在创建的时候才可见，之后是无法查看的。

![[JQ44b5DmcoAT6MxjYVIcrhZUn5c.png]]

### 环境变量配置

用持久化方式，修改环境变量 Anthropic API 的认证 token 和请求 URL，用 kimi 接口替换默认 claude 接口。

执行以下命令：

```bash
echo -e '\n export ANTHROPIC_AUTH_TOKEN=你的API KEY' >> ~/.bashrc
echo -e '\n export ANTHROPIC_BASE_URL=https://api.moonshot.cn/anthropic/' >> ~/.bashrc
source ~/.bashrc
```

命令说明：

- `ANTHROPIC_AUTH_TOKEN`：使用前面生成的 API Key
- `ANTHROPIC_BASE_URL`：固定为 [https://api.moonshot.cn/anthropic/](https://api.moonshot.cn/anthropic/)

### 测试

在命令行输入 claude，发现使用了 kimi 的请求地址，表示配置成功

![[NT9ub3OH1otRjGxav30cBvZgnQc.png]]

## 安装 deepseek v3.1 x Claude code

deepseek3.1 发布了，相对之前有着更强的 Agent 能力：通过 Post-Training 优化，新模型在工具使用与智能体任务中的表现有较大提升。非常适合接入 claude code，同时因为是国内的大模型，可以直接访问，无需挂代理。

<strong>DeepSeek V3.1 + Claude Code，主打够用，便宜，不用梯子；</strong>
[官方文档](https://api-docs.deepseek.com/zh-cn/guides/anthropic_api)

### 注册 deepseek api

登录 deepseek 的开发平台 [https://platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys)，充值个几块钱

创建好后，记得复制生成的 api key，下一步有用

![[GVLXbeMOio9s7HxaPcfcvYebnyb.png]]

### 环境变量配置

```
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
export ANTHROPIC_AUTH_TOKEN="DEEPSEEK_API_KEY"
export ANTHROPIC_MODEL=deepseek-chat
export ANTHROPIC_SMALL_FAST_MODEL=deepseek-chat
```

将上图 DEEPSEEK_API_KEY 替换成自己的复制的 api key。记录保留引号，不然无法正常使用（踩过的坑）

### 测试

![[WqAsbUPo5oP0vfxt0pccIdYxnG8.png]]

## 安装 Any Router x Claude Code(不推荐)

> 最近测试下来，完全使用不了

[Any Router](https://anyrouter.top/register?aff=Mvho) 接入了官方 Claude Code 转发，提供了 Claude 4 等多种模型。现在注册即送 $100 Claude Code 额度，非常划算，按照本文步骤操作即可使用。

### 注册 Any Router

1. 打开链接注册（必须通过此链接领取双倍奖励）：[https://anyrouter.top/register?aff=HBsq](https://anyrouter.top/register?aff=HBsq)
2. 创建 API 令牌

   - 在 API 令牌菜单中创建令牌。
   - <strong>模型限制处选择</strong> `claude-sonnet-4`。
   - 添加完成后，在 “令牌列表” > “查看” 中可见 API Key。

### 环境变量配置

执行以下命令：

```bash
echo -e '\n export ANTHROPIC_AUTH_TOKEN=sk-...' >> ~/.bashrc
echo -e '\n export ANTHROPIC_BASE_URL=https://anyrouter.top' >> ~/.bashrc
source ~/.bashrc
```

- `ANTHROPIC_AUTH_TOKEN`：使用前面生成的 API Key
- `ANTHROPIC_BASE_URL`：固定为 `https://anyrouter.top`

### 使用 Claude Code

- 进入项目目录，执行：

```bash
claude
```

- 根据提示配置，即可开始使用。

![[HPfQbr9dMoQ7q1x4sh5ceEshnsf.png]]

## 硅基流动平台

查看[官方文档](https://docs.siliconflow.cn/cn/usercases/use-siliconcloud-in-ClaudeCode#%E6%96%B9%E5%BC%8F%E4%BA%8C%EF%BC%9A%E6%89%8B%E5%8A%A8%E9%85%8D%E7%BD%AE-claude-code-%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)，找到使用自定义模型的方法，就是修改以下环境变量。
PS：目前 Claude Code 并不支持添加多个自定义模型（Custom Model），每次变更都需要修改。
```
export ANTHROPIC_BASE_URL="https://api.siliconflow.cn/"
export ANTHROPIC_MODEL="moonshotai/Kimi-K2-Instruct-0905"    # 可以自行修改所需模型
export ANTHROPIC_API_KEY="sk-fvnfqknasbbhmbwhsylqqsbmmhcbyganaxukpyuawvobyrex"    # 请替换 API Key
```

我们先在平台创建好api key，然后根据你使用的操作系统，进行环境变量修改
#### 创建api key

登录https://cloud.siliconflow.cn/me/account/ak ，创建保存你的 API Key
![[Pasted image 20251212101829.png]]
#### windows修改环境变量

打开powershell工具，使用 .NET API 写入用户级环境变量，执行以下代码，适用于长期配置：

```powershell
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://api.siliconflow.cn/", "User")
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_MODEL", "Qwen/Qwen3-Coder-30B-A3B-Instruct", "User")
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "替换为你的 API Key", "User")
```


设置完成后需重新打开一个新的 PowerShell 窗口才能生效。

#### Linux修改环境变量

下面给你整理成一段 **通用 Linux 系统设置环境变量的说明**，不加花哨内容，直接能用、能跑：
你可以将以下变量写入 `~/.bashrc`、`~/.zshrc` 或其他 shell 启动文件，让它们在每次登录时自动生效：

```bash
export ANTHROPIC_BASE_URL="https://api.siliconflow.cn/"
export ANTHROPIC_MODEL="moonshotai/Kimi-K2-Instruct-0905"    # 修改为你需要的模型
export ANTHROPIC_API_KEY="sk-xxxxxx"                         # 替换为你的 API Key
```

保存后，执行：

```bash
source ~/.bashrc
# 或者
source ~/.zshrc
```

即可立即生效。

若只想临时设置（仅在当前终端会话内有效），直接在终端输入三行 `export` 即可。

## Claude Code 更新：1.0.51 官方支持 Windows

最近的 Claude Code 更新至 1.0.51，新增对 Windows 系统的支持，并引入多项功能改进，如命令行增强和告警阈值调整。用户可通过社区资源获取更多使用指导。

📺 视频：🧲 Claude Code 更新：1.0.51 官方支持 Windows 🪟_哔哩哔哩_bilibili

📃 日志：[https://youmind.site/F05CLPXvcIoLKp](https://youmind.site/F05CLPXvcIoLKp)

📖 指南：[CC 教程补充](https://gxokrwbnshq.feishu.cn/wiki/COhdwrdxJigYqckl5o3c6vEJnwd)

## 记忆管理

PS: 中文文档翻译为内存管理，误导人

使用不同的位置管理 Claude Code 跨会话的记忆。比如样式指南和工作流程中的常用命令。

所有记忆文件在启动 Claude Code 时都会自动加载到上下文中。

## 常用命令和技巧

完整官方文档：[https://docs.anthropic.com/zh-CN/docs/claude-code/cli-reference](https://docs.anthropic.com/zh-CN/docs/claude-code/cli-reference)

<table>
<tr>
<td>效果<br/></td><td>操作<br/></td><td>备注<br/></td><td><br/></td></tr>
<tr>
<td>换行<br/></td><td>\ + Enter<br/></td><td>在所有终端中有效<br/></td><td><br/></td></tr>
<tr>
<td>编辑上一条消息<br/></td><td>`Esc` + `Esc`<br/><br/></td><td>双击 escape 键修改<br/>或者上下键<br/></td><td><br/></td></tr>
<tr>
<td>清除对话历史<br/></td><td>`/clear`<br/></td><td><br/></td><td><br/></td></tr>
<tr>
<td>压缩对话<br/></td><td>`/compact [instructions]`<br/></td><td>压缩对话，可选择性地提供重点指令<br/></td><td><br/></td></tr>
<tr>
<td>记忆管理<br/></td><td>`/memory`<br/></td><td>编辑 CLAUDE.md 记忆文件<br/></td><td><br/></td></tr>
</table>

## 配置
使用中文回答
```
news_yu@SZ-YUXINWEN-L1:~/coding/fvr_ptp$ cat ~/.claude/CLAUDE.md 
每次请用中文回答我。
```


修改 `~/.claude/settings.json` 配置文件：

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "<ARK-API-KEY>",
    "ANTHROPIC_BASE_URL": "https://ark.cn-beijing.volces.com/api/compatible",
    "ANTHROPIC_MODEL": "doubao-seed-code-preview-latest",
    "API_TIMEOUT_MS": "3000000",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1
  }
}
```
## 问题
### **429 rate limiting**
在使用模型接口时，我遇到了一个典型的 **429 rate limiting** 踩坑问题。最开始以为是请求次数过多，触发了 RPM 限制，但反复检查后发现，请求量并不大。

仔细查看报错信息，其中明确提示 **TPM limit reached**，这才意识到真正触发的是 **每分钟 Token 上限**。在硅基流动平台 L0 用量级别下，TPM 只有 40,000，看起来不少，但实际非常容易用完。

问题的根源在于单次请求的 Token 消耗过高：一次性塞入完整文档、代码或历史对话，再加上模型默认较长的输出，几次连续请求就能在 1 分钟内把 Token 消耗殆尽。即使请求次数不多，也会直接返回 429。

这个问题在批量脚本、循环调用或隐式并发场景中尤其容易出现，看起来只是“一次调用”，实际上短时间内已经累积了大量 Token。

最终的经验是：429 并不一定是“发得太频繁”，更可能是“一次说得太多、连续说得太快”。解决方式包括裁剪上下文、限制输出长度、控制调用节奏，并在必要时等待 60 秒让 TPM 窗口恢复。

**结论：claude code不适合接入硅基流动的api，因为它的TPM太低了，分析稍微大一点的项目时经常触发429报错，导致无法使用。**

### 配置好国内模型api后还是提示登录
在~/.claude.json配置文件中添加如下配置：
```
{"hasCompletedOnboarding": true}
```
如果还是不行，进行如下修改：
```
补充说明一条，如果显示Not logged in, please run /login可能是不小心误设置了。  
/config 指令最后一项看看是不是use custom Api key是不是false,设置为true
```
