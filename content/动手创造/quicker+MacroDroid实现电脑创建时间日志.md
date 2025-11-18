---
title: quicker+MacroDroid 实现电脑创建时间日志
---

## 前言

时间日志是一个好用的软件，就是没有网页端

每次都需要打开手机上操作

## <strong>URL Scheme 简介</strong>

URL Scheme 是一种通过特殊格式的链接（类似网址）直接唤醒应用并执行特定操作的技术。通过浏览器、其他应用或快捷指令调用这些链接，您可以实现快速启动应用功能，无需手动操作应用界面。

### <strong>典型使用场景</strong>

1. 可与待办清单、自动化工具等应用无缝协作，直接在第三方应用中启动/停止时间日志的计时功能，无需反复切换应用界面。
2. 通过简单的网页按钮即可实时控制计时状态
3. 使用 Tasker/MacroDroid 等工具创建智能脚本可设置自动化条件（如特定时间触发、连接指定 WiFi、启动某应用等）当条件达成时自动执行计时操作<strong>（注：经测试发现部分安卓系统事件可能因版本限制无法触发，建议优先使用基础功能，高级功能供技术爱好者探索研究）</strong>

### 浏览器触发（可选）

在手机浏览器地址栏输入“sjrz://api/start?type=研究东西”，并不能触发时间日志软件的记录功能。

原因是浏览器拦截了非标准协议 sjrz，需要创建一个<strong>网页文件，</strong>其中加上跳转链接，才可正常触发

```html
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <title>URL Scheme 测试</title>
</head>
<body>
  <h2>测试开始 sjrz</h2>
  <p>
    <a href="sjrz://api/start?type=研究东西">点我尝试打开 sjrz 应用</a>
  </p>
  <h2>测试结束 sjrz</h2>
  <p>
    <a href="sjrz://api/end?type=研究东西">点我尝试打开 sjrz 应用</a>
  </p>

</body>
</html>
```

## 安装使用

- Google play 安装地址：[https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid&hl=zh](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid&hl=zh)
- 安装后可以免费体验 7 天，看广告可延长试用时长，买断的话折合人民币 47.5 元

## 相关文件

- 时间日志软件 url scheme 介绍文档：[https://www.yuque.com/julius-qz8ci/timelogger/uhnag38hywawvgp3#gkr2a](https://www.yuque.com/julius-qz8ci/timelogger/uhnag38hywawvgp3#gkr2a)
- [https://www.yuque.com/julius-qz8ci/timelogger/cb4bspi9yhcc5s0s](https://www.yuque.com/julius-qz8ci/timelogger/cb4bspi9yhcc5s0s)
