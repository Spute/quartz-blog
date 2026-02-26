---
title: 【开发者自荐】Obsidian 插件：一键复制笔记到微信公众号
publish: "true"
category: 文章写作
date: 2025-12-24
alias: " rwqz1iwbzqyxy2j01mog"
tags:
  - 实践
  - 工具分享
---
## 前言

这是一个 [Obsidian](https://obsidian.md/) 插件，用于**一键将当前笔记以微信公众号格式复制到剪贴板**，可直接粘贴到微信公众号后台，实现高效发布与分享。

插件支持 **Markdown 正文、本地图片与网络图片** 的完整复制，无需依赖第三方网站，也不需要配置公众号密钥、 Token 等任何信息。只需执行一次obsidian命令，复制后粘贴即可完成发布流程。

### 项目背景

在日常使用中，将 Obsidian 笔记发布到微信公众号一直是个麻烦事：

- 在线 Markdown 转公众号工具**不支持本地图片**
- 操作步骤繁琐，格式容易丢失
- 每次发布都需要反复调整样式

因此开发了这个插件，目标很简单：  **让 Obsidian 笔记发布到公众号这件事，变得像复制粘贴一样简单。**

---

**🌟 开源项目**  
如果你觉得这个插件对你有帮助，欢迎访问 GitHub 仓库并点一个 Star：

👉 [https://github.com/Spute/obsidian-copy-to-mp](https://github.com/Spute/obsidian-copy-to-mp)

---

## 使用演示
![https://pic.520233.best/2025-12-24-14-17-44.gif](https://pic.520233.best/2025-12-24-14-17-44.gif)

---

## 功能特性


- 支持通过 **命令面板（Ctrl + P）** 运行，也可绑定快捷键
    
- 支持：复制**选中内容**,未选中内容时，复制**整个文档**
        
- 自动将内容转换为**微信公众号可直接粘贴的 HTML 格式**
    
- 媒体支持：支持本地图片和网络图片

- 样式处理：目前只有内置样式，后续会扩展支持多套样式方案

-  配置功能：粘贴内容可包含Markdown 文件名，文档开头的元数据

---

## 已知问题

- 暂不支持移动端 Obsidian
    
- 当图片较多或图片较大时，Data URI 方式可能占用较多内存
    
- 列表中部分加粗内容在个别场景下可能出现自动换行

- 不支持视频复制

-  复制链接，只会包含名称，实际的链接url会显示不出来。可能是公众号不允许外链的原因，只能转换成文本才行。
    

---

## 安装与使用

目前仅支持**本地安装**（插件已提交官方插件市场，尚未审核通过，暂无法在线安装）。

### 安装教程

可参考以下教程完成插件安装：
目前只支持本地安装（提交obsidian官方还未审核通过，无法在线安装）。

安装方法可参考我的教程：

- [B站介绍视频（包含安装步骤）: https://www.bilibili.com/video/BV1W4iuBpEWv/#reply115814850106975](https://www.bilibili.com/video/BV1W4iuBpEWv/#reply115814850106975)
    
- [Obsidian 进阶教程：插件安装: https://blog.520233.best/Obsidian-%E8%BF%9B%E9%98%B6%E6%95%99%E7%A8%8B%EF%BC%9A%E6%8F%92%E4%BB%B6%E5%AE%89%E8%A3%85](https://blog.520233.best/Obsidian-%E8%BF%9B%E9%98%B6%E6%95%99%E7%A8%8B%EF%BC%9A%E6%8F%92%E4%BB%B6%E5%AE%89%E8%A3%85)

## 问题反馈

如果在使用过程中发现问题或有改进建议，欢迎在 GitHub 仓库提交 Issue。

---

## 联系方式 & 支持

你的支持是项目持续维护和更新的动力 🙏

**赞赏码：**

<img src="https://pic.520233.best/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20251222142804_282_346.jpg" width="200" height="200" alt="赞赏码">

**微信联系方式（请说明来意）：**
<img src="https://pub-2326c75947ef43449218077f86785a82.r2.dev/my-wechat.jpg" width="200" alt="WX">


---


## 致谢

本项目参考并基于以下优秀开源项目，特此感谢：

- [花生编辑器](https://github.com/alchaincyf/huasheng_editor)
    
- [obsidian-copy-as-html](https://github.com/mvdkwast/obsidian-copy-as-html)
    