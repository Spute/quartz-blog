---
title: 手机也能装浏览器插件！Edge 安卓完全攻略
publish: "true"
tags:
  - 文章
---
## 前言

移动端浏览器一直无法自由安装插件，体验远弱于桌面端。而 微软Edge 是目前少数真正支持插件的安卓手机浏览器：正式版可安装官方精选插件，Canary 测试版甚至能安装任意扩展，让手机浏览体验直接拉满。本篇教你 3 分钟完成安装。

通过安装插件，你可以在手机上实现广告拦截、视频加速、网页翻译、阅读增强等功能，极大丰富移动端浏览体验。

---

## 正式版插件安装（最简单）

**这个方法操作简单，适合新手**，无需折腾。 如下是安装沉浸式翻译的示例。
![[Pasted image 20251121182451.png]]

**操作步骤：**

1. **安装 Edge 浏览器**
    
    - 在应用商店搜索「Microsoft Edge」或扫码安装。
        
2. **进入扩展中心**
    
    - 打开 Edge → 右下角菜单（三横） → 扩展
        
3. **安装扩展**
    
    - 找到沉浸式翻译 → 点击安装
        
    - 系统自动完成，无需登录或设置
        

**注意**：官方渠道仅能安装 Edge 推荐的少量扩展，若想安装任意扩展，需要使用 Canary 方法。

---

## Canary 测试版插件安装（高级玩法）

这个方法适合想安装任意 Edge 插件的用户。只要插件在 Edge 插件商店上架，就能完全安装到安卓手机。同时支持使用本地crx插件文件安装

**操作步骤：**

1. **安装 Edge Canary**：Google Play 搜索 Edge Canary（测试版，功能更新快）
        
2. **启用开发者选项**：Edge Canary → 菜单 → 设置 → 关于 Microsoft Edge
        
    连续点击版本号 5 次 → 出现“已启用开发者选项”, 然后进入开发人员选项，可以看到如下页面，包含 “Extension Install by ID” 和 “Extension Install by crx” 

    ![[82e8e165-ce17-4170-b642-0154a186b63c.jpg| 250x550]]
        
4. **获取插件 ID**
    
    - 访问 Edge 插件商店（桌面或手机均可）https://microsoftedge.microsoft.com/addons/Microsoft-Edge-Extensions-Home
        
    - 插件地址类似：  `https://microsoftedge.microsoft.com/addons/detail/插件名/amkbmndfnliijdhojkpoglbnaaahippg`。最后一串字符即为插件 ID，例如沉浸式翻译：`amkbmndfnliijdhojkpoglbnaaahippg`

5. **打开 Extension Install by ID**
    
    - 设置 → 开发者选项 → 找到 Extension Install by ID → 点击进入安装界面
        
6. **输入插件 ID → 自动安装**
    
    - 在 Edge 的 “Extension Install by ID” 输入框粘贴 ID → 即可安装
7. 选择crx文件安装，设置 → 开发者选项 → 找到 Extension Install by crx → 点击进入安装界面

## 安卓Edge安装包
有条件的可以去google play商店下载最新版的：
正式版Edge：https://play.google.com/store/search?q=edge+browser+microsoft&c=apps

测试版Edge：https://play.google.com/store/apps/details?id=com.microsoft.emmx.canary

也可以使用我下载好的：
夸克网盘「Edge Canary」链接：https://pan.quark.cn/s/9bc99440a7a0  提取码：rTar 