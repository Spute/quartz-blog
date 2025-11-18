---
title: MediaCrawler--一款开源、强大的多平台自媒体数据采集工具
---

## 是什么

一个功能强大的多平台自媒体数据采集工具，支持<strong>小红书、抖音、快手、B 站、微博、贴吧、知乎</strong>等主流平台的公开信息抓取。

项目地址：[https://github.com/NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler)

### 技术原理

- 核心技术：基于 <u>Playwright</u> 浏览器自动化框架登录保存登录态
- 无需 JS 逆向：利用保留登录态的浏览器上下文环境，通过 JS 表达式获取签名参数
- 优势特点：无需逆向复杂的加密算法，大幅降低技术门槛

## 功能特性

## 使用步骤

### 运行程序

依次执行以下命令（需要预先安装好 uv 工具），如下是在 windows 的 powershell 中运行的示例。使用的是以搜索的方法爬取小红书的评论。

```
# 查看 uv 工具的版本，确认已安装
uv --version

# 克隆 MediaCrawler 项目代码仓库
git clone https://github.com/NanmiCoder/MediaCrawler.git

# 进入项目目录
cd .\MediaCrawler\

# 安装项目所需依赖（根据 pyproject.toml）
uv sync

# 安装 Playwright 所需的浏览器等运行环境
uv run playwright install

# 运行主程序，平台为小红书（xhs），使用二维码登录，执行搜索任务
uv run main.py --platform xhs --lt qrcode --type search
```

- 执行最后一条命令后，出现以下情况，扫码登录小红书账号

![[N14WbKLH8oU5RpxxgDxc17Bgnpb.png]]

- 登录成功后会自动下载数据

![[UjM0bL4COojO2Bxc8hncMzbWnT9.png]]

### 查看爬取的数据

![[D8l0bBQ05oyRpTxyz2ucRsomnxq.png]]
