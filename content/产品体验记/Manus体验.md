---
title: Manus 体验
---

# 终于体验上 manus 这个通用智能体了

Manus 刚上线没多久，我就去申请了验证码，盼星星盼月亮，终于拿到了邀请码。之前 Manus 可是被炒到 5W 一个账号，如今终于体验上了，这次我就让它帮我制作一门面向小白的 three.js 课程。在一旁看着 Manus 规划拆解任务、列出代办清单，使用浏览器搜索资料，操作电脑创建文件，编写代码，一步步执行任务，这效率没得说。

![[Wfapb2poIoFqh4xFasEc2L0KnCg.png]]

它先是深入研究了 Three.js 的基础知识和前置要求，接着创建了一份详细的课程大纲，足足有 8 个章节，内容从基础概念到综合项目实战，安排得明明白白。之后，又开发了一系列示例代码和演示。最后，还特别贴心地生成了课程使用手册说明。

案例回放链接在这儿，大家有兴趣可以看看：https://manus.im/share/YR0QgrlAxo9oUXufSWcFdv?replay=1 。本来我还想让 Manus 生成一个能直接部署的网站，可惜当时额度用完了，只能等之后有额度了再继续推进。

查了下，免费用户赠送初始额度是 1000 积分，以下是升级的费用和效果。

![[YlDGboUFsovgzFxrCZhcCzMYnkh.png]]

# manus 制作小红书分享图：尝试解决文字乱码问题

胡子哥提出了用 manus 制作小红书分享图片的想法，目前会有文字乱码的问题。这里做一些尝试，看看能不能解决。

就像 Manus 生成的如下图片

![[WJSBbN8waodZEcxqTy3cxIS0n2d.png]]

改用 Gpt4o 来生成图片，发现和使用 manus 一样存在文字乱码问题

![[Tin1b5zqnoWgefxvAzdcofLvnrh.png]]

## 分析文字乱码问题

让 AI 分析一下原因，主要是因为：

- <strong>AI 图像模型的训练目标不同：</strong>大多数 AI 图像生成模型（如 DALL·E、Stable Diffusion）主要训练目标是生成<strong>视觉上逼真的图像</strong>，而非准确生成<strong>可读文字</strong>。文字在图像中属于「细节高敏感内容」，但模型往往只学到了文字的「视觉纹理」，没能学会其<strong>结构和语义对应关系</strong>。
- <strong>文字结构复杂，易被破坏：</strong>文字尤其是中文或复杂字体，其笔画和结构高度敏感，一点变形、错位或遮挡就可能导致难以辨认。而图像生成模型容易在这些细节上出错，比如：

  - 字体结构扭曲
  - 错别字或拼写错误
  - 混杂乱码或错误字符
- <strong>缺少针对性的训练数据：</strong>大多数生成模型训练时，图片中带<strong>清晰文字内容的样本较少</strong>，也未特别强化识别或合成文字的能力，因此表现不佳。

---

## <strong>解决方法 </strong>

## 尝试过程

manus 回放：https://manus.im/app/abIfL0BVXg7uBlA5WovbZZ

提示图片乱码后，让 Manus 自己想办法解决，它改用 Matplotlib 工具制作图片，文字倒是没乱码了，图片却变丑了。。。

![[IfrKbDweRoHABexTsdNcOetznec.png]]

让 manus 通过“图像 + 模板”方式植入文字区域。先用 AI 生成相关图，在图像中预留空白区域（如海报模板），然后后期将文字准确植入。模板生成的没啥问题，后面增加文字处理的很拉跨。。。后面再想想有没有其他办法。

![[Rq7QbPI8uoLWgZxC2EXc0uxLnvg.png]]

# 优化：manus 一键制作长文小红书分享图

接着昨天继续优化。经过昨天测试，发现 AI 生成相关图，然后使用在线图像编辑工具添加文字的方式还是有漂移的问题。今天让 manus 换成写 html+css 代码方式来渲染出合适的效果。结果如下，算是刚及格了。

![[B4v3bpuBcogtMJx1tVscmpEUnsh.png]]

## 导出 HTML 生成的图片：

manus 生成 html 并不适合直接分享，需要导出成图片的形式，方法如下：

1、打开包含 HTML 内容的网页。

2、打开开发者工具（按 F12 或右键选择“检查”）。

3、点击开发者工具左上角的设备图标（通常是一个手机和平板的图标），进入设备模式。

4、然后再先点设备模式旁边的小箭头，后用鼠标选择需要截图的区域（下图左半部分显示）。

5、在元素面板中，右键点击需要截图的元素，选择“capture node screenshot”, 图片就保存成功了。

![[MV77blaWJou3stxFQQlc2tkMnuf.png]]

![[ZCiGbhHlvoLAiKxfEy3cn5RCnwg.png]]

## 后续优化点

- 卡片的排版有点单调，可以让 AI 再美化一下。
- 图像使用的是 svg 生成的，有点丑丑的，可以找一些替代方案。

# 体验 manus 的幻灯片模式

看报道称公司搬去了新加坡，业务转移到了海外，并且暂停了和阿里的合作。

很久没有登录 manus，今天登录后发现了幻灯片模式

![[QQfxbLfGsofOukxykTPcEZ8Wn4f.png]]

简单测试一下，生成的图片网页上展示的挺好的，总体感觉还行，能到及格水平，但直接用还是有些问题。以下是测试的回放：

https://manus.im/share/file/f8ea18da-84d2-49b9-b0d7-5d075408b15d

通过这个测试发现两个问题：

1. <strong>下载 ppt 后生成的图片与网页显示的有差异。</strong>

![[RJ2NbIWFho5Pdux0DdRcfJlFnSd.png]]
![[SYTCbP27fo9aW6xMqnmcxsP7nmb.png]]

1. <strong>产生了幻觉</strong>，我只提供了一个月的消费数据，生成的 ppt 中却有有其他月份的消费数据

![[FL9gbyjpqoVyqwxtOHXcNaUJn1d.png]]
