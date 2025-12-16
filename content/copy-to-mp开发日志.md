---
category: 文章写作
publish: "false"
tags:
  - 软件工程
title: copy-to-mp开发日志
date: 2025-12-15
alias: " wj0tzsnh6nehhp2v3lci"
---
# 项目描述

参考开源项目：
花生编辑器：https://github.com/alchaincyf/huasheng_editor
obsidian的copy-to-html插件：https://github.com/mvdkwast/obsidian-copy-as-html


将花生的editor变成一个obsidian插件，而不是只能复制为html然后粘贴到飞书云文档，然后再贴花生的eidtor上去。。。
这种方式会让md的部分格式变形。。。而且不太方便


测试发现直接复制插件的内容到mp会让标题的样式、代码的样式变形。

参照花生编辑器，构建一个测试md文件，里面包含常用的样式。方便验证效果。

研究花生编辑器发现，剪切板居然可以同时保留两种格式的内容，然后根据粘贴的编辑器，使用不同的格式。解答了我使用粘贴到记事本和公众号编辑后台出现不同的形式。

花生是如何知道微信公众号能够接受什么格式的html的？
有官方文档吗？

其实是大概弄明白了花生编辑器的实现方案了，使用的vue3的CDN全局渲染方式来生成内容。

## 写一个将html转换复制到剪切板的调试工具
```
        const simplifiedHTML = doc.body.innerHTML;

        const plainText = doc.body.textContent || '';

  

        const htmlBlob = new Blob([simplifiedHTML], { type: 'text/html' });

        // const textBlob = new Blob([plainText], { type: 'text/plain' });

        // Plain：给纯文本用（仍然是 HTML 源码）

        const textBlob = new Blob([simplifiedHTML], { type: 'text/plain' });

  

        const clipboardItem = new ClipboardItem({

          'text/html': htmlBlob,

          'text/plain': textBlob

        });

  

        await navigator.clipboard.write([clipboardItem]);
```