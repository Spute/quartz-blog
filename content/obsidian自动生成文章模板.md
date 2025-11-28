---
title:
publish: "true"
category: 文章写作
data: 2025-11-25
permalink: " rungx96dkxc1viaoe6h1"
---
## 前言

背景与原因
- 在笔记或博客系统中，希望每篇文章有一个**固定的 URL**，即使标题修改，也不影响访问。
- 中文标题可以自由修改，但不希望 URL 随之变化。
- 希望自动化生成，减少手动操作。
Obsidian 笔记既能自由修改标题，又能保持每篇文章永久的固定 URL，非常适合个人知识库、博客或长期内容管理。


生成一个permalink 
生成创建时间

quartz文章写作
- `permalink`：页面的自定义 URL，即使文件路径更改也保持不变。
- `date`：笔记发布的日期字符串，通常使用 `YYYY-MM-DD` 格式。


在 Obsidian 窗口里，按下：  
**Ctrl + Shift + I**  
（或者菜单：`View` → `Toggle developer tools`）


有 Console因为 **Obsidian 是用 Electron 开发的**。

而 Electron =  **Chromium（浏览器内核） + Node.js（后端能力） + 打包成桌面应用**
这是Obsidian 原生就支持运行 JavaScript 代码的原因

 Obsidian 实现方案使用插件
- **Templater**：自定义模板和脚本，自动生成文章 permalink  

[[Obsidian：一款基于Markdown的本地知识管理与笔记工具]]