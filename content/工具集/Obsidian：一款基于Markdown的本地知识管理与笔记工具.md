---
title: Obsidian--一款基于 Markdown 的本地知识管理与笔记工具
category: 工具分享
tags:
  - 知识管理
---

## 前言

如果你喜欢 <strong>Typora 的极简写作</strong>，又曾被 <strong>Notion 的组织能力</strong> 吸引，那么你一定会对 <strong>Obsidian</strong> 产生兴趣。
它是一款以 <strong>本地 Markdown 文件</strong> 为核心的知识管理工具，不依赖云端，兼具安全、可定制与高效特性。无论是开发者、知识工作者还是内容创作者，都能在其中构建属于自己的“第二大脑”。

## 特点
1. **本地存储**：数据自主掌控，不受服务器故障影响。所有笔记保存于本地，可自由同步、备份、迁移，不受平台限制。
2. **兼容性强，生态开放**：文件格式标准，都以标准 `.md` 文件形式存储。
3. **双向链接+图谱**：笔记关联自然，助力灵感追溯。
4. **插件生态**：功能丰富且可自定义扩展。内置插件市场，支持从任务管理到知识图谱的多种功能，可按需安装，完全自定义工作流。
5. **轻量高效**：启动快、编辑流畅，多场景适用。不依赖网络，渲染速度快，体验干净流畅。
6. <strong>同步方式多样</strong>：支持 windows、安卓、iOS 等客户端，你可以选择 OneDrive、iCloud、Git 等方式同步资料，也可便携存储于 U 盘。
# 使用 git 实现自动同步
使用git插件自动同步，好处是不用切换页面就可以推送。可是并不太稳定。
手动使用git命令实现，需要手动写commit
最终使用了quartz自带的npx命令，自动帮你生成commit并推送。

## 发布成网站

选方案，先选社区活跃的开源框架，这样bug少功能全，更省心省事。简单看了下quartz4是符合这个条件就。
[[美观好用：Quartz+Cloudflare Pages快速obsidian笔记发布]]

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

## 图片自动上传插件
复制图片是自动上传r2中

需要启动picgo本地服务器，如果是cf-r2配置还得为这个服务器安装插件
https://github.com/JYbill/picgo-plugin-cloudflare-r2?tab=readme-ov-file