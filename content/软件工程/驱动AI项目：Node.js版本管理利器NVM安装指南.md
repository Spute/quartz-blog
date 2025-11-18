---
title: 驱动 AI 项目--Node.js 版本管理利器 NVM 安装指南
---

## 前言

Node.js 已成为现代开发不可或缺的环境，其安装的必要性远超工具本身。从构建前端项目、运行后端服务，到如今蓬勃发展的 AI 辅助开发领域，Node.js 都是核心基石。<strong>无论是 Claude Code、Cursor Editor 还是众多 MCP（Model Context Protocol）服务，都依赖 Node.js 进行安装、部署和运行</strong>。它提供了庞大的 npm 生态系统，使开发者能快速集成开源库与工具，从而高效构建和连接复杂的应用与服务。因此，正确管理 Node.js 版本是保障开发环境统一、项目稳定运行的关键前提。

NVM (Node Version Manager) 是一款 Node.js 版本管理工具。它允许您在系统上安装多个 Node.js 版本，并通过命令轻松切换，从而无缝改变终端中所指向的 `node` 命令的实际路径。这在同时维护多个需要不同 Node.js 版本的项目时尤为高效，让您无需反复下载和卸载，即可满足各项目的运行环境要求。

## windows 安装 nvm

### 下载安装脚本

- 链接：[https://github.com/coreybutler/nvm-windows/releases/tag/1.2.2](https://github.com/coreybutler/nvm-windows/releases/tag/1.2.2)

<strong>可下载以下版本：</strong>

- nvm-noinstall.zip：绿色免安装版，但使用时需要手动配置环境变量等。
- nvm-setup.zip：安装版，对新手更友好，<strong>推荐使用</strong>

![[WpcybF5ayoeR98xbVGucTZs1nRg.png]]

### 运行安装脚本

运行下载好的程序，一步步点击“下一步”安装即可。

安装器会在系统环境变量的 `Path` 中，进行环境变量配置，并指定 node 的安装目录

```
C:\Users\你的用户名\AppData\Roaming\nvm
C:\Program Files\nodejs
```

然后打开 powershell 命令行，输入 nvm version 验证一下，输出 nvm 的版本表示安装成功

![[GCrVbldnLoIO91xXzUAc75eZnwg.png]]

### 安装一个 node 版本

分别执行以下命令

```
nvm list available        # 查看可安装的远程版本
nvm install 22.18.0       # 安装 Node.js 指定版本(推荐使用LTS长期支持版本）
nvm use 22.18.0           # 切换到该版本
```

效果如下：

![[EUnGbFdXOo5nsrxvarhcodwznnb.png]]

## Mac 先安装 NVM

在 Mac OS 苹果系统的安装代码为

```
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"

# Download and install Node.js:
nvm install 22

# Verify the Node.js version:
node -v # Should print "v22.18.0".
nvm current # Should print "v22.18.0".

# Verify npm version:
npm -v # Should print "10.9.3".
```

## 常用 nvm 命令

```bash
nvm list available        # 查看可安装的远程版本
nvm install 20.18.0       # 安装 Node.js 指定版本
nvm use 20.18.0           # 切换到该版本
nvm ls                    # 查看已安装的版本
nvm uninstall 20.18.0     # 卸载指定版本
```

## 常见问题 & 解决方案
