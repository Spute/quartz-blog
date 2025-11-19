---
title: Obsidian--一款基于 Markdown 的本地知识管理与笔记工具
---

# 初识

## 前言

如果你喜欢 <strong>Typora 的极简写作</strong>，又曾被 <strong>Notion 的组织能力</strong> 吸引，那么你一定会对 <strong>Obsidian</strong> 产生兴趣。
它是一款以 <strong>本地 Markdown 文件</strong> 为核心的知识管理工具，不依赖云端，兼具安全、可定制与高效特性。无论是开发者、知识工作者还是内容创作者，都能在其中构建属于自己的“第二大脑”。

## 特点

1️⃣ <strong>基于文件，完全掌控</strong>
所有笔记都以标准 `.md` 文件形式保存于本地，可自由同步、备份、迁移，不受平台限制。

2️⃣ <strong>兼容性强，生态开放</strong>
文件格式标准，可与 AI 工具、代码编辑器、Git 等协同使用，灵活度极高。

3️⃣ <strong>性能轻快，离线无忧</strong>
不依赖网络，渲染速度快，体验干净流畅，如同浏览器阅读模式。

4️⃣ <strong>插件丰富，自由扩展</strong>
内置插件市场，支持从任务管理到知识图谱的多种功能，可按需安装，完全自定义工作流。

5️⃣ <strong>主题灵活，轻量定制</strong>
通过主题与 CSS 片段即可轻松调整外观与排版，兼顾美观与性能。

6️⃣ <strong>同步方式多样</strong>
支持 windows、安卓、iOS 等客户端，你可以选择 OneDrive、iCloud、Git 等方式同步资料，也可便携存储于 U 盘。

## Obsidian 插件总览

obsidian 的插件绝对是一个强大的功能，让你可以自由定义自己的写作平台。

### 核心插件

### 第三方插件

# 使用 git 实现自动同步

![[VLQ5b849XoZVyRxiDFTcb1ifnRb.png]]

![[EkxMb0B5mo8H0FxHYmTchDGCnVd.png]]

![[FbNabNmUhopgZIxn5RFcFq3MnHd.png]]

# 美观好用：Quartz+Cloudflare Pages快速博客发布

## 前言

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
## 功能点详细比对：

精力有限，就只对比这 4 种方案了。下面列上我目前体验对比过的全部第三方开源发布方案，供各位参考，也可以持续观察作者后续的开发进展，再择优选择。

- jekyll 方案 1，即我选用的方案。[GitHub - maximevaillancourt/digital-garden-jekyll-template: Start your own digital garden using this Jekyll template ](https://github.com/maximevaillancourt/digital-garden-jekyll-template)
- jekyll 方案 2，[一位印度老哥写的 103](https://github.com/Jekyll-Garden/jekyll-garden.github.io)
- hugo 方案(quartz)，[jackyzha0 (Jacky Zhao) · GitHub 272](https://github.com/jackyzha0)
- logseq 方案，[GitHub - pengx17/logseq-publish: Logseq Publish Action 77](https://github.com/pengx17/logseq-publish)
- zola 方案，[GitHub - ppeetteerrs/obsidian-zola: A no-brainer solution to turning your Obsidian PKM into a Zola site. 41](https://github.com/ppeetteerrs/obsidian-zola)
- perlite 方案，[GitHub - secure-77/Perlite: A webbased markdown viewer optimized for Obsidian 45](https://github.com/secure-77/Perlite)
- gatsby 方案，支持[[横向卷动布局- andy mode]]，但构建时长小时级别，[GitHub - aravindballa/gatsby-theme-andy: A Gatsby theme to build Andy style websites. ](https://github.com/aravindballa/gatsby-theme-andy/)

总之，有钱就选官方服务准没错。其次，综合对比后，我选择了 jekyll 方案 1，如何一步步实现，见下文。

## 参考链接

- [https://forum-zh.obsidian.md/t/topic/8852](https://forum-zh.obsidian.md/t/topic/8852)
- [美观好用：Obsidian+Quartz+Cloudflare Pages 快速博客发布指南 - 毛可多来](https://www.xulihang.work/Quartz/%E7%BE%8E%E8%A7%82%E5%A5%BD%E7%94%A8%EF%BC%9AObsidian+Quartz+Cloudflare-Pages%E5%BF%AB%E9%80%9F%E5%8D%9A%E5%AE%A2%E5%8F%91%E5%B8%83%E6%8C%87%E5%8D%97)

# 基础语法

## <strong>内部嵌入语法</strong>

这是 <strong>Obsidian 的内部嵌入语法</strong>（也叫 <em>wiki 链接嵌入语法</em>），不是标准 Markdown。

### 🧩 语法说明

- `[[...]]` 是 <strong>Obsidian 的内部链接格式</strong>
- 前面加一个 `!` 变成 <strong>嵌入模式（embed）</strong>：可以嵌入图片、PDF、音频、其他笔记内容等

### 📌 示例

`![[图片文件名.jpg]]`
`![[某个笔记.md#某个小节]]`
`![[音频.mp3]]`

### 自定义图片大小

某些主题允许写：

`![[19abee38-838d-4c7f-8c10-be934801c6cb.jpg|300]]`

或：

`![[19abee38-838d-4c7f-8c10-be934801c6cb.jpg|width=300]]`
