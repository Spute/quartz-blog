---
title: 如何通过 django 和 Sphinx 导出 django4.2 的中文版 pdf
---

# 前言

看到 v2ex 社区有个求 django 中文 pdf 文档的帖子，这或许是一个常见需求吧，可以解决离线查看问题，尝试搜索引擎搜索并没有找到合适的东西。第二天看到另外一个网友给出特别好的解决方案，眼前一亮，打开了思路，这里简单记录一下。

# 价值

- 可以导出其他项目官方文档，方便离线查看
- 依赖于多语言的支持，对项目的规划有借鉴意义

# 如何实现

文档源码在 [github.com/django/django](https://github.com/django/django/tree/main/docs)

中文翻译在 [github.com/django/django-docs-translations](http://github.com/django/django-docs-translations)

把它俩搞一起，用 sphinx 构建一个 pdf 。

原理：

django 的官方文档网站中，使用的也是 django 项目中的文本和结构，翻译的文件在另一个仓库中，翻译依赖 po 类型的翻译文本文件。需要的是将两个仓库合并，以 [Sphinx](https://www.sphinx-doc.org/en/master/#) 工具导出。

# Claude 的解决步骤

> # Django 4.2 中文文档 PDF 生成指南

## 环境准备

1. 首先安装必要的依赖:

```bash
pip install sphinx sphinx-intl sphinx-rtd-theme
pip install django==4.2
pip install rst2pdf
```

## 获取 Django 文档源码

1. 克隆 Django 文档仓库:

```bash
git clone https://github.com/django/django.git
cd django/docs
```

## 配置 Sphinx

1. 在 docs 目录下创建或修改 conf.py 文件:

```python
import os
import sys

# 项目信息
project = 'Django'
copyright = '2024, Django Software Foundation'
author = 'Django Software Foundation'
release = '4.2'

# 扩展配置
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'rst2pdf.pdfbuilder'
]

# PDF输出配置
pdf_documents = [(
    'index',
    u'django-4.2-docs-zh_CN',
    u'Django 4.2 文档',
    u'Django Software Foundation'
)]

# 中文支持配置
language = 'zh_CN'
locale_dirs = ['locale/']
gettext_compact = False

# HTML主题设置
html_theme = 'sphinx_rtd_theme'
```

## 准备中文翻译

1. 生成 pot 文件:

```bash
make gettext
```

1. 更新中文翻译文件:

```bash
sphinx-intl update -p _build/gettext -l zh_CN
```

1. 在 `locale/zh_CN/LC_MESSAGES/` 目录下编辑.po 文件进行翻译

## 生成 PDF

1. 构建中文 PDF:

```bash
sphinx-build -b pdf . _build/pdf -D language=zh_CN
```

## 字体配置

1. 创建字体配置文件 `fontconfig.json`:

```json
{
    "pdf": {
        "font_path": [
            "/usr/share/fonts/",
            "/usr/local/share/fonts/"
        ],
        "font_face": {
            "normal": "NotoSansCJK-Regular.ttc",
            "bold": "NotoSansCJK-Bold.ttc",
            "italic": "NotoSansCJK-Regular.ttc",
            "bold_italic": "NotoSansCJK-Bold.ttc"
        }
    }
}
```

## 常见问题解决

1. 中文显示方块:

   - 确保安装了中文字体
   - 在系统中安装 Noto Sans CJK 或其他中文字体
   - 更新 fontconfig.json 中的字体路径
2. 目录层次过深:

   - 在 conf.py 中添加:

   ```python
   ```

pdf_toc_depth = 3

```
	
3. 图片显示问题:
	- 确保图片路径正确
	- 使用绝对路径引用图片
		
## 优化建议

1. 分章节生成:
	- 可以先生成单章节PDF进行测试
	- 使用 `sphinx-build -b pdf . _build/pdf -D language=zh_CN topics/http.rst`
		
2. 性能优化:
	- 使用 `-j auto` 参数启用多进程构建
	- 示例: `sphinx-build -j auto -b pdf . _build/pdf -D language=zh_CN`







```
