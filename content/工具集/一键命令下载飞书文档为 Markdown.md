---
title: 一键命令下载飞书文档为 Markdown
---

## 前言

飞书云文档具备简洁、丝滑、功能强大、免费、效率高等优点，是很多人日常写作的首选工具。但是它并不支持 markdown 格式的导出，很难快速发布到其他文章平台。今天分享的一个开源免费的工具一键实现这个功能。

- 项目地址：[https://github.com/Wsine/feishu2md](https://github.com/Wsine/feishu2md)

<strong>准备工作：</strong>

- 下载工具包：[https://github.com/Wsine/feishu2md/releases](https://github.com/Wsine/feishu2md/releases)
- 获取 api-key(参考项目 README.md 文件)
- 修改配置文件

<strong>使用示例：</strong>

打开 powershell 命令行，输入工具名称 + 需要下载的飞书文档链接即可。

![[MTGKbYp4BoIRebxiAx5cygfHnxh.png]]

### 生成配置文件

通过 `feishu2md config --appId <your_id> --appSecret <your_secret>` 命令即可生成该工具的配置文件。

通过 `feishu2md config` 命令可以查看配置文件路径以及是否成功配置。更多的配置选项请手动打开配置文件更改。

使用‘‘config’’指令查询配置，显示配置文件路径：

![[YzkgbGEUzoq9QwxZ8rzctUc7nsG.png]]

### 下载单个文档为 Markdown

通过 `feishu2md dl <your feishu docx url>` 直接下载，文档链接可以通过 分享 > 开启链接分享 > 互联网上获得链接的人可阅读 > 复制链接 获得。

示例：

`$ feishu2md dl "https://domain.feishu.cn/docx/docxtoken"`

### 批量下载某文件夹内的全部文档为 Markdown

此功能暂时不支持 Docker 版本

通过 `feishu2md dl --batch <your feishu folder url>` 直接下载，文件夹链接可以通过 分享 > 开启链接分享 > 互联网上获得链接的人可阅读 > 复制链接 获得。

示例：

`$ feishu2md dl --batch -o output_directory "https://domain.feishu.cn/drive/folder/foldertoken"`

### 批量下载某知识库的全部文档为 Markdown

通过 `feishu2md dl --wiki <your feishu wiki setting url>` 直接下载，wiki settings 链接可以通过 打开知识库设置获得。

示例：

`$ feishu2md dl --wiki -o output_directory "https://domain.feishu.cn/wiki/settings/123456789101112"`
