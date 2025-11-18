---
title: 万物皆可 MCP--AI 模型轻松进行 B 站视频搜索
---

项目地址：[https://github.com/34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js)

<strong>功能特点</strong>

- B 站视频搜索
- 支持分页查询
- 返回视频信息（标题、作者、播放量、时长等）
- 基于 MCP 协议的标准化接口

<strong>系统要求</strong>

- Node.js >= 20.12.0

## 效果展示

如下是配置好的效果，在对话框中即可调用这个工具，搜索你想要的内容。

![[DPXCbAXDFo5Wc3xrdg0cX7cmnZc.png]]

## 搭建 mcp server 运行环境

下载仓库代码，解压到某个目录下

![[RFAxb1eemoouVtx5B8AcQZOpnDd.png]]

进入解压后的目录，输入 powershell 打开命令行工具

![[BNhUb8Ca4of9jdxuLhicO08gnad.png]]

在命令行分别执行以下命令，以下是命令说明（node 需要自行安装，网络教程很多，也可以让 AI 帮忙）

```
# 检查node的版本，要求Node.js >= 20.12.0
node -v
# 依赖包安装
npm i
# 构建项目，会在项目目录下生成dist\index.js文件
npm run build
```

![[ZPaNbbCyaoqlJoxD9YbceIbNnjg.png]]

查询项目目录复制好，如下我的项目目录是“D:\coding\mcp-server\bilibili-mcp-js”

![[S4Cwbe07PohxqxxuzI7cs2YcnAb.png]]

## 配置 Mcp 客户端

打开 Cherry Studio 新建一个 mcp 服务，按如下进行配置

需要将“D:\coding\mcp-server\bilibili-mcp-js”自行替换为你自己的项目目录。

![[YdnebbBCGoPF52xa0yfcglmonLe.png]]
