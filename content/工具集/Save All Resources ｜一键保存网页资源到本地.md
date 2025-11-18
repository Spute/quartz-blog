---
title: Save All Resources ｜ 一键保存网页资源到本地
---

## 前言

当我们在网页上看到一个好看的 H5 页面，或者是相当酷炫的 JS 动画，一个很自然的想法就是 F12，然后下载资源占为己有。而 F12 是前端开发人员的利器，在 Chrome 开发者工具中，调试时使用最多的功能有：ELements（元素）、Console（控制台）、Sources（源代码），Network（网络）等。

但是如果要保存网站内容，一种做法是直接右键另存为整个网页。虽然有时网页也能正常运行，但是也会不可避免地丢失了网站文件夹的结构。

当然，你也可以在 Sources 中挨个文件地另存为，然后重新建立文件夹结构。但此种做法，只能应对资源量较少的网页，而且操作繁琐。

而有个谷歌浏览器插件：Save All Resources 可以快速地帮你完成这个操作。

> 不使用浏览器 save as 功能，是因为它没有把文件保存到对应文件夹, 而且会改动保存下来的 html 文件

## Save All Resources 插件简介

Save All Resources 插件可以一键下载当前网站所有资源的一个宝藏插件。

地址：[https://chromewebstore.google.com/detail/save-all-resources/abpdnfjocnmdomablahdcfnoggeeiedb](https://chromewebstore.google.com/detail/save-all-resources/abpdnfjocnmdomablahdcfnoggeeiedb)

![[Js4FbtVANoMdbAxhlKecTdvGnJh.png]]

## Save All Resources 插件的<strong>使用方法</strong>

1. 下载安装扩展。
2. 打开需要下载保存的网站
3. 按快捷键 F12 打开开发者工具。

![[UAV2bWzUco9y1dxjbMZctTAEnlf.png]]

1. 翻到最后一个选项选择 resourcessaver，点击 Save All Resources 即可。

![[QLa6bnLg8odXBbxvn3UcjUvHnad.png]]

1. 解压保存的压缩包，进入对应的网站名文件夹，打开 index.html 这个网页文件，即可本地打开这个保存下来的的网站。

![[PXFHb9psboNR9Cx7oLbcGcYunTg.png]]

![[DhrdbknX4oam2txLFDjcsKZUnS4.png]]

## 反爬手段

以 https://wxchat-2nr.pages.dev/#/网站为例

一些网站会通过 `debugger`、死循环或窗口尺寸检测等手段防止调试或爬取数据。当打开 F12 开发者工具时，脚本触发 `debugger` 会导致页面暂停，看似“卡死”，而正常访问则不受影响。解决方案包括关闭断点、禁用 DevTools 暂停或通过控制台重写 `debugger` 函数。

> PS: 分析防爬机制，需遵守法律与网站使用规范。

如果是反爬网站会出现如下页面，操作如下

- 点击“取消所有断点”
- 继续 JavaScript 脚本执行

![[M5qlbbOcpormcsx1zv7cBDTDnle.png]]
