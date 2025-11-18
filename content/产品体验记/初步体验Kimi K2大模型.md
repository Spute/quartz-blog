---
title: 初步体验 Kimi K2 大模型
---

最近我关注到了 Kimi K2，这是一款由月之暗面正式发布并同步开源的模型。它采用 MoE 架构，总参数达 1T，激活参数 32B ，在代码能力与通用 Agent 任务处理方面表现颇为出色。从官方发布的文章（链接：mp.weixin.qq.com ）中可知，在 SWE Bench Verified、Tau2、AceBench 等基准性能测试里，Kimi K2 均斩获了开源模型中的最优成绩，彰显出其在代码、Agent、数学推理任务上的领先实力 。

登录 kimi 官网，选择 k2 模型即可体验。

![[XJs8bNgdfowWmUxzBhfcGu5Anib.png]]

然后我对 Kimi K2 进行了初步测试，选取了 3 个用例进行验证，然而测试结果不尽人意，3 个用例均出现了 bug。并且，在使用过程中我还发现其吐字速度较为迟缓。我推测，这或许是由于免费页面测试所分配的配置不够高导致的。 从目前看来，想要一句话生成复杂的页面还是有些困难。

![[GRyXbqLSKo7y2nxTqwScZ5mKnyc.png]]

![[V4PlbNuNVo0Zv8xIxClcoBKNnog.png]]

![[ThxobRdxRoLjIzxeymPcnXzynSd.png]]
