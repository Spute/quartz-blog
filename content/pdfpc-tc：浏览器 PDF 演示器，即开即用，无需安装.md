---
title: pdfpc-tc：浏览器 PDF 演示器，即开即用，无需安装
publish: "true"
category: 文章写作
date: 2025-11-28
permalink: " sxr3tatbq5mcdumcpjo7"
---
## 前言

在学校、单位或会议场景中，许多用户需要展示教学课件或项目演示。传统方式通常使用 LaTeX + Beamer 或 Typst + Touying 制作 PDF，再配合 Pympress 或 pdfpc 放映器播放。然而，这些放映工具存在不少痛点：性能不佳，翻页时容易卡顿；Windows 下安装复杂；在公共电脑上使用需要额外安装，操作繁琐。对于希望轻量、快速、跨平台播放 PDF 的用户，这些问题极大影响了演示体验。
如今有个开源项目可以很好地解决这个问题：
项目地址 [https://github.com/Master-Hash/pdfpc-ts](https://github.com/Master-Hash/pdfpc-ts)  
体验地址 [https://pdfpc.hash.moe/](https://pdfpc.hash.moe/)  
视频演示 [https://assets.hash.moe/pdfpc-ts-demo.mp4](https://assets.hash.moe/pdfpc-ts-demo.mp4)
![[Pasted image 20251128170945.png]]

## 核心特点

- **浏览器播放，无需安装**：基于 SolidJS，直接在浏览器中实现完整放映效果，免去安装和配置烦恼。
    
- **双窗口模式**：主窗口查看备注，弹出窗口拖拽到大屏幕上播放，实现专业演示模式。
    
- **高性能 PDF 渲染**：采用 PDFium 渲染器，性能和渲染效果优于传统 Pympress 或 pdfpc 的 poppler，翻页流畅，视觉体验更佳。
