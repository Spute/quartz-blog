---
title: 美观好用：Quartz+Cloudflare Pages快速obsidian笔记发布
tags:
  - 网站搭建
category: 文章写作
publish: "true"
data: 2025-11-24
permalink: " 5k25o5wag4xyhrf6wmk4"
---

## 前言
[[Obsidian：一款基于Markdown的本地知识管理与笔记工具]]

找到一个方案 **Quartz 4** —— 一个专为 Obsidian 用户设计的静态 Markdown 框架。
- **无需后端**，可直接部署到 GitHub Pages 或 Vercel。
- **原生支持 Obsidian 的双链语法与目录结构**。
- 只需把笔记放进指定文件夹并提交到仓库，即可**自动构建一个美观、可导航、可全文搜索的个人知识库网站**。
- 拥有成熟的开源社区、结构清晰、样式现代。
- **内置 SEO 与 PWA 支持**，几乎开箱即用。
实验下来发现页面简洁美观，手机端适配也还行。这点相对于飞书云文档好多了，我决定弃用飞书云文档，以后直接在obstain里写内容，然后直接发布到网站。
效果如下：
![[Pasted image 20251118183828.png]]
网站地址：[https://blog.520233.best/](https://blog.520233.best/)

部署方式可以参考以下文章，写点非常详细：
- [美观好用：Obsidian+Quartz+Cloudflare Pages 快速博客发布指南 - 毛可多来](https://www.xulihang.work/Quartz/%E7%BE%8E%E8%A7%82%E5%A5%BD%E7%94%A8%EF%BC%9AObsidian+Quartz+Cloudflare-Pages%E5%BF%AB%E9%80%9F%E5%8D%9A%E5%AE%A2%E5%8F%91%E5%B8%83%E6%8C%87%E5%8D%97)

## PWA实现
### PWA 是什么？

**PWA** 的全称是 **Progressive Web App**，中文可以翻译为“渐进式网络应用”。

你可以把它理解为一个**使用了现代 Web 技术构建的网站，但能提供类似于原生手机 App 的体验**。

它不是一个全新的框架或语言，而是一系列**理念、技术和标准的集合**。

**PWA 的核心特点和优势：**

1. **可靠 (Reliable)**
    
    - **离线工作**：这是 PWA 最显著的特点之一。通过一项叫做 **Service Worker** 的技术，PWA 可以缓存关键的资源和数据。即使用户的网络连接不稳定甚至完全离线，他们依然可以访问核心内容或使用基本功能。
        
    - **快速加载**：Service Worker 可以缓存静态资源（如 HTML、CSS、JS、图片），使得重复访问时速度极快，几乎瞬时加载。
        
2. **快速 (Fast)**
    
    - 无论网络状态如何，都能提供流畅、快速的交互体验。这极大地提升了用户满意度。
        
3. **可安装 (Engaging)**
    
    - **可添加到主屏幕**：用户可以直接在浏览器中将 PWA “安装”到手机或电脑的主屏幕上，就像安装一个原生 App 一样。安装后会有一个独立的图标，点击后会以独立的窗口打开，没有浏览器的地址栏和工具栏，体验更像一个 App。
        
    - **推送通知**：PWA 可以像原生 App 一样向用户发送推送通知，这对于重新吸引用户、传递重要信息非常有效。
## og image链接预览图 / 分享缩略图
全称**OG Image（Open Graph Image）**
我将文章分享到知乎、飞书等其他会有一个分享微缩图。如何控制它

## SEO优化

搜索引擎优化

## 样式自定义

优化一些显示问题，exporter导航树下文章显示，上下间隔不够明显，当文章名称太长时容易区分不开。找到对应scss文件，添加padding属性解决了。

## layout布局排版
quartz会根据屏幕的大小自动调节组件的布局，同时适配电脑端和移动端

| ![[Pasted image 20251123153638.png]] | ![[Pasted image 20251123153713.png]] |
| ------------------------------------ | ------------------------------------ |




---
*内容整理自 Quartz 官方文档，保留原意并优化表述结构。*




## 评论提供商

### Giscus

首先，确保你用于 Quartz 的 [GitHub](https://quartz.zituoguan.com/%E8%AE%BE%E7%BD%AE-GitHub-%E4%BB%93%E5%BA%93) 仓库满足以下要求：

1. **仓库为[公开](https://docs.github.com/en/github/administering-a-repository/managing-repository-settings/setting-repository-visibility#making-a-repository-public)**，否则访客无法查看讨论内容。
2. **已安装 [giscus](https://github.com/apps/giscus) 应用**，否则访客无法评论和点赞。
3. **已启用 Discussions 功能**，可[在仓库设置中开启](https://docs.github.com/en/github/administering-a-repository/managing-repository-settings/enabling-or-disabling-github-discussions-for-a-repository)。

然后，使用 [Giscus 官网](https://giscus.app/#repository) 获取你的 `repoId` 和 `categoryId`。请确保选择 `Announcements` 作为讨论类别。

![](https://quartz.zituoguan.com/images/giscus-repo.png)

![](https://quartz.zituoguan.com/images/giscus-discussion.png)

输入仓库和选择讨论类别后，Giscus 会生成一些 ID，Quartz 配置时需要用到。你无需手动添加脚本，Quartz 会自动处理，但需要在下一步填写这些值！

![](https://quartz.zituoguan.com/images/giscus-results.png)

最后，在 `quartz.layout.ts` 文件中，编辑 `sharedPageComponents` 的 `afterBody` 字段，填入如下配置（将值替换为你自己的）：

quartz.layout.ts

`afterBody: [  Component.Comments({    provider: 'giscus',    options: {      // data-repo      repo: 'jackyzha0/quartz',      // data-repo-id      repoId: 'MDEwOlJlcG9zaXRvcnkzODcyMTMyMDg',      // data-category      category: 'Announcements',      // data-category-id      categoryId: 'DIC_kwDOFxRnmM4B-Xg6',    }  }),],`

### 个性化配置

Quartz 还支持 Giscus 的其他选项，你可以像配置 `repo`、`repoId`、`category`、`categoryId` 一样传递它们。

``type Options = {  provider: "giscus"  options: {    repo: `${string}/${string}`    repoId: string    category: string    categoryId: string     // 自定义主题文件夹的 URL    // 默认 'https://${cfg.baseUrl}/static/giscus'    themeUrl?: string     // 浅色主题 .css 文件名    // 默认 'light'    lightTheme?: string     // 深色主题 .css 文件名    // 默认 'dark'    darkTheme?: string     // 页面与讨论的映射方式    // 默认 'url'    mapping?: "url" | "title" | "og:title" | "specific" | "number" | "pathname"     // 是否严格匹配标题    // 默认 true    strict?: boolean     // 是否启用主帖的表情反应    // 默认 true    reactionsEnabled?: boolean     // 评论输入框相对评论的位置    // 默认 'bottom'    inputPosition?: "top" | "bottom"  }}``

#### 自定义 CSS 主题

Quartz 支持 Giscus 的自定义主题。将 `.css` 文件放在 `quartz/static` 文件夹下，并设置相关配置即可。

例如，你有浅色主题 `light-theme.css`、深色主题 `dark-theme.css`，且你的 Quartz 站点部署在 `https://example.com/`：

`afterBody: [  Component.Comments({    provider: 'giscus',    options: {      // 其他选项       themeUrl: "https://example.com/static/giscus", // 对应 quartz/static/giscus/      lightTheme: "light-theme", // 对应 quartz/static/giscus/light-theme.css      darkTheme: "dark-theme", // 对应 quartz/static/giscus/dark-theme.css    }  }),],`

#### 条件显示评论

Quartz 支持通过 frontmatter 字段 `comments` 控制是否显示评论框。默认所有页面显示评论，如需关闭，在页面 frontmatter 设置 `comments: false`。

`--- title: 此处禁用评论！ comments: false ---`


参考文档：https://quartz.zituoguan.com/features/comments

![[Pasted image 20251123155015.png]]
