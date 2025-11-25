## 前言
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

[[Obsidian：一款基于Markdown的本地知识管理与笔记工具]]

````markdown
---
title: 自动生成文章 permalink 的方案
permalink: auto-slug-placeholder
date: <% tp.date.now("YYYY-MM-DD") %>
tags: [Obsidian, Templater, permalink, SEO, 博客]
---

# 📝 自动生成文章 permalink 方案

## 1️⃣ 背景与原因
- 在笔记或博客系统中，希望每篇文章有一个**固定的 URL**，即使标题修改，也不影响访问。
- 中文标题可以自由修改，但不希望 URL 随之变化。
- 希望自动化生成，减少手动操作。

## 2️⃣ 痛点
1. **标题可改，URL 需稳定**  
   - 如果直接用标题生成 URL，一旦改标题，原链接就失效。
2. **中文标题直接作为 URL**  
   - 中文 URL 会被编码，链接冗长，不利于复制和 SEO。
3. **重复和冲突问题**  
   - 多篇文章标题可能重复，需要确保 URL 唯一。
4. **手动维护工作量大**  
   - 每篇文章都手动生成 slug，不方便且容易出错。

## 3️⃣ 需求
- 自动生成并写入 YAML 元数据字段 `permalink`  
- permalink 永久固定，不随标题变化  
- 支持中文标题，但 URL 可读性和 SEO 优化  
- 避免重复 slug  
- 自动化执行，最好通过 Obsidian 插件完成

## 4️⃣ 解决方案

### 方案设计
1. **独立 slug 字段**  
   - 在 YAML 元数据中新增 `permalink` 字段  
   - slug/permalink 与标题分离，首次生成后不再修改

2. **Slug 生成规则**（可选）
   - **随机短码**（稳，最短 URL，不会重复）  
     例：`/p/f9a3b2`  
   - **拼音/英文 slug**（SEO 友好）  
     例：`/p/zi-dong-sheng-cheng-lu-you`  
   - **英文自定义 slug**（用户手动输入）

3. **保证唯一性**
   - 数据库或本地系统中检查重复，如果重复，自动加后缀  
     例：`my-article` → `my-article-1`

---

## 5️⃣ Obsidian 实现方案

### 使用插件
- **Templater**：自定义模板和脚本，首次创建文章时自动生成 permalink  
- **MetaEdit（可选）**：批量修改 YAML 元数据

### Templater 示例脚本

#### A. 随机短码方案
```javascript
<%*
// 如果已存在 permalink，则不覆盖
if (!tp.frontmatter.permalink) {
    // 生成 6 位随机字母数字 ID
    let id = Math.random().toString(36).substr(2, 6)
    tp.frontmatter.permalink = id
}
%>
````

#### B. 标题转拼音方案（SEO 优化）

```javascript
<%*
const pinyin = require("pinyin"); // Node 环境支持
if (!tp.frontmatter.permalink) {
    let title = tp.frontmatter.title || tp.file.title
    let slug = pinyin(title, {style: pinyin.STYLE_NORMAL}).flat().join("-")
    tp.frontmatter.permalink = slug
}
%>
```

### 使用方法

1. 新建笔记 → 执行模板 → 自动生成 `permalink`
    
2. 以后修改 `title` → permalink 不变
    
3. 可直接使用 `permalink` 构建文章 URL
    

---

## 总结

- **核心原则**：permalink 永久固定、独立于标题
    
- **实现方式**：Obsidian + Templater 插件
    
- **可选生成规则**：
    
    - 随机短码 → 稳定、最短
        
    - 拼音/英文 slug → SEO 友好
        
- **优势**：
    
    - 保证 URL 永远不变
        
    - 减少手动操作
        
    - 支持中文标题，显示不受影响
        

> 这样，Obsidian 笔记既能自由修改标题，又能保持每篇文章永久的固定 URL，非常适合个人知识库、博客或长期内容管理。

```

---

我可以帮你再写一份 **直接可用的 Templater 模板**，每次新建笔记就自动生成 `permalink`，无需手动执行。  

你希望这个模板用 **随机 ID** 还是 **标题转拼音** 的方式生成 permalink？
```