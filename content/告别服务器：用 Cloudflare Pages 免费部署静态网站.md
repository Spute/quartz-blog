---
title: 告别服务器：用 Cloudflare Pages 免费部署静态网站
publish: "true"
category: 文章写作
tags:
  - 网站搭建
  - 实践
data: 2025-11-25
permalink: " lcm9kgas5p8oji6d27zl"
---

## 前言

你是否也曾认为“搭建网站 = 买服务器”？其实，借助 Cloudflare Pages 这类现代托管服务，即使没有后端服务器，也能快速发布一个高速、稳定的静态网站。

我之前和许多初学者一样，对网站托管认知停留在“必须买服务器”的阶段。后来偶然通过朋友了解到 GitHub Pages，才知道静态网站完全可以免费托管。之后同事推荐了 Cloudflare——一个功能丰富且对免费用户极为友好的平台，我才发现原来部署网站可以如此简单。

这让我意识到，很多我们原本以为复杂的技术需求，其实早有更优雅的解决方案。信息差，往往是阻碍我们尝试新工具的最大障碍。

Cloudflare Pages 是一款专业的静态网站托管服务，功能和 GitHub Pages 类似，支持直接部署 HTML、CSS、JS 等静态资源，也可集成 Git 实现自动发布。如果你打算搭建博客、项目介绍页、帮助文档或个人作品集，完全不需要购买服务器。

作为全球顶级的 CDN 服务商，Cloudflare 在全球范围内拥有大量节点，访问速度通常优于 GitHub Pages，国内海外加载表现也更稳定。此外，Cloudflare Pages 允许一个账户创建多个项目，自定义域名，非常适合个人开发者与初创项目使用。

如果你正在寻找一个简单、免费且可靠的静态网站托管平台，不妨试试 Cloudflare Pages。

## Cloudflare Page介绍

Cloudflare Pages 提供免费的静态网站托管服务，支持自定义域名和自动化部署，操作简单。

免费计划专为个人开发者和小型项目设计，提供以下额度，完全可以满足个人开发者和小型项目的基本需求。

| **服务类别**      | **具体限制**    | **说明**                 |
| ------------- | ----------- | ---------------------- |
| 构建与部署         | 500 次/月     | 每月最多自动构建部署 500 次       |
| 构建并发          | 1 个         | 同一时间仅能进行一个构建           |
| 自定义域名         | 100 个       | 可为托管的站点绑定最多 100 个自定义域名 |
| 站点数量          | 无限制         | 可创建无限个站点，但有软限制         |
| 单个站点文件        | 20,000 个    | 每个站点托管的文件总数上限          |
| 单个文件大小        | 25 MB       | 上传或构建的单个文件最大尺寸         |
| 静态文件请求        | 无限          | 站点的静态资源访问无次数限制         |
| Serverless 函数 | 100,000 次/日 | 每日函数调用请求数上限            |

## 直接上传文件部署步骤

1. 登录 Cloudflare 仪表板，导航到 Workers > Pages。选择“直接上传”方式部署（简单，无需 Git 存储库）。

![[AqiobSj2Lo5MjGxx7EKcGzhWnUc.png]]

为项目创建名称
![[BMpbbCicmoru5QxUgXbc5vVWnMf.png]]

上传项目文件：通常来自输出目录（如 `output`），包含静态网站文件（HTML、CSS、JS 等）。

![[LLrublE9boKbJZxxhEbccZ85n2l.png]]

点击“部署”，完成后使用提供的 `.pages.dev` 域名访问网站。  

![[JrhibXIJrokmi5xSn65ci7Cmnod.png]]

点击域名即可查看已部署完成的网站。

![[OldIbpk0OozL1mxve7cczzjhnIg.png]]

## 通过Github 存储库部署步骤

使用 GitHub 集成部署可动态执行构建命令，并在推送提交时自动部署，比直接上传更自动化。  ![[Pasted image 20251123235034.png]]

直接访问 [https://pages.cloudflare.com/](https://pages.cloudflare.com/) ，没有账号的可以按照提示注册，有账号的可以直接登录。

登录后点击 `创建项目` ，如下：

![[Pasted image 20251123235005.png]]

点击“连接 GitHub 账户”，在授权页面选择“Install & Authorize”。  

![[Pasted image 20251123235035.png]]

这里会弹出 Github 的授权页面，选择 `Install & Authorize` 允许 Cloudflare 访问 Github 账户，如下：

![[Pasted image 20251123235055.png]]

然后会显示 Github 存储库，也包括非公开的存储库，选择要部署的存储库，点击 `开始设置` ：

![[Pasted image 20251123235118.png]]

### 构建设置（可选）

如果需要构建命令，可以在如下页面设置构建命令和存放构建的页面的目录：

> 这个配置可以通过 cloudflare 来动态运行构建指令生成部署的静态文件，非常实用。Cloudflare 克隆存储库后会自动执行 `npm install` 之类的命令下载所需的依赖，然后执行构建命令，然后把构建完成的文件放到网站目录。

![[Pasted image 20251123235209.png ]]


### `保存并部署`

点击 `保存并部署` 后 Cloudflare Pages 就会开始构建和部署，如下：

同时下方也会输出日志：

![[Pasted image 20251123233952.png]]

部署完成后点击 `继续处理项目` 就可以看到部署的网站了，

默认的域名是 `项目名称.pages.dev` 。

## 设置域名（可选）

部署成功后，可以选择点击 `自定义域` ，来设置自己的域名

![[Pasted image 20251123233910.png]]

输入要绑定的域名：

![[Pasted image 20251123233854.png]]

如果你用的是 Cloudflare 的 DNS 的话，Cloudflare 可以一键设置 CNAME。如果不是的话就需要手动设置 CNAME，登录域名管理后台，添加一条 CNAME 指向默认的 `pages.dev` 域名。

我使用的是 Cloudflare 的 DNS，可以自动设置 CNAME：

![[Pasted image 20251123233837.png]]

设置完成后需要一段时间才会生效。
