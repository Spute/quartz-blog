---
title: 基于 tree.js 实现的 3D 骰子
---

## 前言

最近在 codepen 中发现一个很有趣的项目，一个使用 Three.js 和 Oimo 物理引擎创建的 3D 骰子模拟器，具有逼真的物理效果和流畅的动画。

花了一点时间将这个纯前端的项目部署了一下（电脑和手机浏览器都可以使用），平时需要用 roll 骰子的时用用，还是很合适。

项目已开源。

项目地址：[https://github.com/Spute/3d-dice-three-js](https://github.com/Spute/3d-dice-three-js)

体验网址：[3d-dice.520233.best](https://3d-dice.520233.best/)

![[JrPkbkGocoZGKvxkyqucC5Oxn9b.png]]

## ✨ 特性

- 🎲 逼真的 3D 骰子 - 使用 Three.js 渲染的 3D 骰子模型
- 🚀 物理引擎 - 集成 Oimo 物理引擎实现真实物理碰撞
- ⚡ 流畅动画 - 使用 GSAP 实现平滑的动画效果
- 🎨 视觉效果 - 包含发光效果和阴影渲染
- 🎯 交互控制 - 可调整骰子数量，支持轨道控制
- 📱 响应式设计 - 适配不同屏幕尺寸

## 🎮 使用方法

1. 打开应用后，你会看到一个 3D 场景，其中包含骰子和控制面板
2. 点击"ROLL"按钮投掷骰子
3. 使用"-"和"+"按钮调整骰子数量（1-12 个）
4. 使用鼠标拖拽旋转视角
5. 使用滚轮缩放场景

## 🔗 原始项目

该项目基于 CodePen 项目：<u>[https://codepen.io/fuzionix/pen/KKjgVaX](https://codepen.io/fuzionix/pen/KKjgVaX)</u>
