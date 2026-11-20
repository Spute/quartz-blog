---
title: Claude Code 安装 Playwright Browser MCP 笔记
publish: "false"
category: 文章写作
date: 2026-08-02
alias: " eyqlf1zxbyhkrrhl6nti"
tags:
---


# Claude Code 安装 Playwright Browser MCP 笔记

## 环境

- 系统：Windows 10 + WSL Ubuntu
- Claude Code：2.1.220（官方版）
- Node.js：20+

验证 Claude Code：

```bash
claude --version
```

输出示例：

```text
2.1.220 (Claude Code)
```

---

# 1. 安装 Playwright MCP

推荐安装为**全局(User Scope)**。

```bash
claude mcp add -s user playwright npx @playwright/mcp@latest
```

查看是否安装成功：

```bash
claude mcp list
```

正常应看到：

```text
playwright: npx @playwright/mcp@latest - ✔ Connected
```

查看详情：

```bash
claude mcp get playwright
```

确认：

```text
Scope: User
Status: ✔ Connected
```

---

# 2. 安装浏览器

Playwright MCP 本身不会安装浏览器，需要安装 Chromium。

```bash
npx -y playwright install chromium
```

如提示缺少系统依赖：

```bash
npx -y playwright install-deps chromium
```

---

# 3. 验证 Playwright

验证 Playwright 是否能够独立启动浏览器：

```bash
npx -y playwright open https://example.com
```

如果浏览器能够正常打开，则说明：

- Playwright 安装正常
- Chromium 安装正常
- WSL 图形环境正常

---

# 4. 验证 Claude Code

进入 Claude：

```bash
claude
```

输入：

```text
打开 https://example.com，并告诉我网页标题。
```

正常情况下 Claude 会调用 Playwright MCP。

---

# 5. 查看 MCP 状态

```bash
claude mcp list
```

查看某个 MCP：

```bash
claude mcp get playwright
```

删除：

```bash
claude mcp remove playwright
```

---

# 6. Project Scope 与 User Scope

Project Scope：

```text
Scope: Local config (private to you in this project)
```

仅当前项目有效。

User Scope：

```text
Scope: User
```

所有项目均可使用，推荐使用。

---

# 7. 常见问题

## Q1：Claude 提示

```text
浏览器不可用，我用 WebFetch 来获取页面内容。
```

说明：

- Claude 已成功调用 Playwright MCP
- Playwright 浏览器启动失败
- Claude 自动降级到 WebFetch

排查步骤：

1. `claude mcp list`
2. `claude mcp get playwright`
3. `npx -y playwright open https://example.com`

---

## Q2：执行

```bash
npx playwright --version
```

提示：

```text
Need to install playwright
```

属于正常现象。

原因：

- `@playwright/mcp` 与 `playwright` 是两个不同的 npm 包。
- MCP 使用的是 `@playwright/mcp`。
- `npx playwright` 使用的是 `playwright` CLI。

---

## Q3：如何判断是否安装成功？

执行：

```bash
claude mcp list
```

看到：

```text
playwright ... ✔ Connected
```

即可说明：

- MCP 已正确注册
- Claude Code 能够连接到 Playwright MCP

---

# 8. 判断是否为官方 Claude Code

执行：

```bash
claude --version
```

例如：

```text
2.1.220 (Claude Code)
```

说明使用的是官方 Claude Code。

---

# 9. 常用命令汇总

```bash
# 查看版本
claude --version

# 查看 MCP
claude mcp list

# 查看 MCP 详情
claude mcp get playwright

# 安装全局 Playwright MCP
claude mcp add -s user playwright npx @playwright/mcp@latest

# 删除 MCP
claude mcp remove playwright

# 安装 Chromium
npx -y playwright install chromium

# 安装 Linux 依赖
npx -y playwright install-deps chromium

# 测试浏览器
npx -y playwright open https://example.com
```

# Google 429（Too Many Requests）问题笔记

## 现象

打开 Google 页面时出现：

```text
Google
429. That's an error.

We're sorry, but you have sent too many requests to us recently.
Please try again later.
That's all we know.
```

这不是 Playwright 报错，而是 **Google 返回的 HTTP 429（Too Many Requests）**，表示请求被 Google 限流。

---

## 常见原因

- 请求频率过高（短时间大量访问 Google）
- 同一 IP 请求过多（共享出口、VPN、代理、云服务器等）
- 使用 Headless 浏览器，自动化特征明显
- 每次创建新的 Browser Context，没有 Cookie 和浏览历史
- 数据中心 IP（AWS、GCP、Azure 等）风控更严格

---

## 如何确认

```python
response = page.goto(url)
print(response.status)   # 429
```

或查看页面内容：

```python
print(page.content())
```

如果页面内容是 Google 的 429 提示，则说明请求已被 Google 拒绝。

---

## 解决方法

- 降低访问频率，请求之间增加随机等待时间
- 复用 Browser Context，保留 Cookie
- 尝试使用 `headless=False`
- 更换出口 IP 或等待限流解除
- 尽量使用官方或第三方搜索 API，而不是直接抓取 Google 搜索页面

---

## 一句话总结

> **Google 429 = Google 认为你的访问过于频繁或具有自动化特征，因此暂时限制了当前 IP/浏览器的访问，与 Playwright 本身无关。**