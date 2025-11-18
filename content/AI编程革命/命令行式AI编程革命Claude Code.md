---
title: 命令行式 AI 编程革命 Claude Code
---

## 是什么

Claude Code 是一个由 Anthropic 开发的<strong>基于终端的 AI 编码工具</strong>，基于 Claude 4 Sonnet 模型。它通过<strong>命令行界面（CLI）</strong>运行，允许开发者通过自然语言命令处理编码任务、Git 工作流和调试。它更适合需要深度项目上下文和复杂任务的场景，例如跨前端和后端的集成增强或自动化重复任务。

对应的 Cursor 是一个<strong>AI 代码编辑器</strong>，基于 Visual Studio Code（VS Code），通过实时代码建议、上下文感知的自动补全和项目索引增强开发者生产力。

<strong>Claude Code 特点是“问答式批量改写”，Cursor 则偏向“写代码时的随时辅助”</strong>

## 环境准备

### 安装 Node.js（如已安装可跳过）

可参考[ 驱动 AI 项目：Node.js 版本管理利器 NVM 安装指南](https://iixchzsb7i.feishu.cn/wiki/P8skwk5yjiUIHDkNaI1cRIbJnDf)

### 安装 Claude Code

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

### 添加到 VS Code

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
