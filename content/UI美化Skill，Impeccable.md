---
title:
publish: "false"
category: 文章写作
date: 2026-05-09
alias: " v0c755b0q1r1kp6htvxs"
tags:
---

## 什么是 Impeccable

`impeccable` 是一个用于提升 AI 前端设计质量的 Skill，主要用于 Cursor、Claude Code 等 AI 编程工具。

项目地址：  
[impeccable GitHub](https://github.com/pbakaus/impeccable?utm_source=chatgpt.com)

它的核心目标是：

> 让 AI 生成的 UI 更接近真实产品设计，而不是“AI 模板感页面”。

---

## 它解决的问题

- UI 过度模板化（SaaS 风）
    
- 卡片堆叠感强
    
- 层级混乱
    
- 间距和节奏不合理
    
- 视觉缺乏重点
    
- “AI味”明显
    
---

## 安装方式
### claude code

```bash
npx skills add https://github.com/pbakaus/impeccable --skill impeccable
```

手动导入：

```bash
cp -r dist/claude-code/.claude project
```

---

## 最常用命令

| 命令                     | 作用            |
| ---------------------- | ------------- |
| `/impeccable teach`    | 建立产品与设计上下文    |
| `/impeccable shape`    | 规划页面结构与信息层级   |
| `/impeccable craft`    | 生成页面 UI 与代码   |
| `/impeccable critique` | 分析 UI 问题与设计缺陷 |
| `/impeccable polish`   | 精修视觉细节        |
| `/impeccable bolder`   | 增强视觉张力        |
| `/impeccable distill`  | 简化复杂结构        |

---

## 推荐工作流

```text
/impeccable teach
/impeccable shape
/impeccable craft
/impeccable critique
/impeccable polish
```

---

## 快速使用策略

- 太平 → `bolder`
    
- 太乱 → `distill`
    
- 做新页面 → `shape → craft`
    
- 上线前 → `polish + critique`
    

---

## 核心价值

Impeccable 的本质是：

> 给 AI 一套“专业 UI 设计规则”，让它不再随机生成界面，而是按设计逻辑工作。
