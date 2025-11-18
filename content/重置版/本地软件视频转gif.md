---
title: 本地软件视频转 gif
publish: "true"
---

## 前言

最近写公众号，需要使用录制的视频，使用壹伴的文章采集功能，却无法将视频同步到公众号草稿。手动上传视频还得设置封面，等待审核，远没有图片方便。

于是想到一个一种方案是将视频转 GIF，这样就可以保证演示的效果，又能快速发布公众号文章了。

最近写公众号，需要做一些视频演示，可是手动上传视频还得设置封面，等待审核，远没有上传图片方便。 于是想到一个一种方案是将视频转 GIF ，这样就可以保证演示的效果，又能快速发布公众号文章了。于是网上找到一个现成的项目，但是有些问题，就基于这个项目修改了一下，然后部署到 cloudflare 里。分享给需要的朋友。

## 简介

一个基于浏览器的视频转 GIF 工具[项目地址](https://github.com/Spute/video-to-gif)，使用 [ffmpeg.wasm](https://github.com/ffmpegwasm/ffmpeg.wasm) 在浏览器中直接处理视频转换。

网站 demo：[https://video2gif.520233.best/](https://video2gif.520233.best/)

本项目基于 [video-to-gif](https://github.com/mryhryki/video-to-gif) 二次开发

## 功能特性

- 🎥 <strong>完全在浏览器中处理</strong> - 无需上传到服务器，保护隐私
- ⚙️ <strong>丰富的转换设置</strong> - 可调节帧率、尺寸、时间范围
- 📱 <strong>拖拽上传</strong> - 支持拖拽或粘贴视频文件
- 📊 <strong>实时预览</strong> - 视频预览和转换进度显示
- 💾 <strong>历史记录</strong> - 自动保存转换历史，支持下载
- 🔒 <strong>隐私保护</strong> - 所有处理都在本地完成

效果展示：

![[KXsZbXPCSo8TefxfvEec1ok7nXf.gif]]

## 浏览限制与问题

- 大文件无法处理：因在内存中运行，转换大视频容易报错。
- 浏览器兼容性差：依赖 SharedArrayBuffer ，在部分浏览器（如 IE ）不可用。可以使用 [caniuse](https://caniuse.com/?search=SharedArrayBuffer) 查看浏览器是否支持 SharedArrayBuffer

![[QopHbv4TooXxW1xo5skcJ5zBnfc.png]]

### 技术原理

官方文档[“使用”部分](https://github.com/ffmpegwasm/ffmpeg.wasm#usage)

- 使用 `<script>` 标签直接引入 `@ffmpeg/ffmpeg` 库：

`<script src="``https://unpkg.com/@ffmpeg/ffmpeg@0.9.4/dist/ffmpeg.min.js``"></script>`

- 转换命令与 FFmpeg 一致，例如：

`await ffmpeg.run('-i', '(file name)', '-r', '(frame rate)', 'output.gif');`

- 在 <strong>Next.js</strong> 等框架中，需要通过 `window.FFmpeg` 判断是否加载成功。
- <strong>npm 包版本不可直接用于浏览器</strong>，推荐参考官方 README，按 `<script>` 方式引入。

### 总结

- WebAssembly 工具封装完善 ，能快速上手使用，用户几乎不需要太多学习成本。
- FFmpeg.wasm 目前在实用性上有较多限制（兼容性、内存瓶颈），但展示了 <strong>浏览器端处理多媒体的可能性</strong>。
- 纯前端即可完成过去需要本地软件的任务，这让人对 Web 技术的未来充满期待。

# 格式对比
