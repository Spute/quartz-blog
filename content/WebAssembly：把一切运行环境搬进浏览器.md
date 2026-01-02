---
title: WebAssembly：把一切运行环境搬进浏览器
publish: "false"
category: 文章写作
date: 2025-12-23
alias: " ia9a9nvp1g4k9ol964yy"
tags:
  - 资源分享
---
## 前言
这几年明显能感觉到，浏览器的边界在被不断推远。  
它早就不只是“看网页”的工具了，而是在一点点吞掉原本属于本地环境的能力。

从最早的在线 IDE、在线文档，到现在借助 **WebAssembly（WASM）**，  
越来越多“需要装环境、配依赖、跑本地”的事情，开始直接在浏览器里完成。

最近我发现了一个很酷的开源项目——**Shift**（基于 WebAssembly 的在线代码编辑器）。  
打开网页，就能直接运行 **Python、Lua、Ruby、Bash、Scheme，甚至是 C**。  
没有虚拟机，没有 Docker，没有环境冲突——点开即用。

### 🧠 项目亮点

✅ **基于 WebAssembly**：把多种语言 runtime 编译到浏览器，让它们都能在网页环境里独立运行；  
✅ **多语言支持**：Python、Lua、Ruby、Scheme（chibi-scheme）、Bash、C（picoc）等常见语言全覆盖；  
✅ **即写即跑**：编辑器自带终端交互，随时输入标准输入，点击 RUN 即可运行；  
✅ **分享友好**：写好的代码一键生成分享链接，不用截图或导出；  
✅ **零依赖零安装**：用户无需配置环境，一切都在浏览器里搞定。

### 🚀 使用体验简述
在线示例网站: [https://shift.js.org/](https://shift.js.org/)
项目地址：[https://github.com/hubenchang0515/shift](https://github.com/hubenchang0515/shift)

📌 在右下角选择你要运行的语言  
📌 在编辑区写代码  
📌 底部输入框是标准输入（stdin）  
📌 **RUN / Ctrl + S** 执行代码  
📌 **CLEAR / Ctrl + L** 清空终端  
📌 **SHARE** 生成代码分享链接

例如 Python、Lua、Ruby 各种入门示例都有 Demo，随便打开就能试。

![[Pasted image 20251223183813.png | 700]]

---
## 最后的话

这一刻会让人强烈地意识到：  
**浏览器正在变成一个跨平台、零安装的通用运行时。**  
而 WebAssembly，正在把“万物皆可 Web 化”这件事，真正落到实处。

未来的开发环境、教学工具、脚本运行器——  
可能不再需要“装软件”，只需打开一个网页。
