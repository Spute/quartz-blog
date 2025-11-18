---
title: manus 学习笔记
---

# 相关文章

[https://mp.weixin.qq.com/s/AwDkMvFYsunQbQkapgC7Ag](https://mp.weixin.qq.com/s/AwDkMvFYsunQbQkapgC7Ag)

[https://baoyu.io/blog/where-is-manus-moat](https://baoyu.io/blog/where-is-manus-moat)

[Manus 学习手册（持续更新）](https://aiyanxishe.feishu.cn/wiki/AAm0wQXecihKrukuvE0cphUbn59?from=from_copylink)

GAIA 是智能体最全面的基准测试，GAIA 中的问题非常难，突出了基于 LLM 的系统的某些困难。·GAIA: [https://hf.co/datasets/gaia-benchmark/GAIA](https://hf.co/datasets/gaia-benchmark/GAIA)

在 GAIA 的公开排行榜上，GPT-4-Turbo 的平均成绩不到 7%。最高的提交是一种基于 Autogen 的解决方案，使用了复杂的多智能体系统并利用 OpenAI 的工具调用功能，达到了 40%。

公开排行榜:[https://hf.co/spaces/gaia-benchmark/leaderboard](https://hf.co/spaces/gaia-benchmark/leaderboard)

# 回放案例

官方案例：https://manus.im/usecases

个人使用：[https://s7zkncrc8l.feishu.cn/base/RFl2bVZa8aBrf9sNAxKcJe6Ynjb?table=tbldohmKAenye18s&view=vewRc5mcyl](https://s7zkncrc8l.feishu.cn/base/RFl2bVZa8aBrf9sNAxKcJe6Ynjb?table=tbldohmKAenye18s&view=vewRc5mcyl)

# 前言

Manners 最近特别火爆各种媒体争相报道，有央视网报道，一夜之间火爆全网，又是一个 AI 产品刷屏爆火之后，随着是 AI 应用方向相关板块大涨，然后全网都在求邀请码，然后这个邀请码被黄牛炒到了 5 万的高价。

有人说说将成为下一个 Deepseek。而了解一个事物的最好方法是写一篇文章去了解他。

2025 年期待自己与 AI 一同进步！

# manus 是什么？

manus 是由 Monica 团队打造的通用 AI 智能体平台，全球首款通用型 agent，致力于将用户的想法转化为具体成果，就是他不仅能回答问题，还能自主分析任务需求。通过调用虚拟环境中的工具，如浏览器，代码编辑器，文本处理器等，完成从数据收集到结果交付的全流程操作。

# manus 干什么？

无论是分析股市趋势，生成财务报告，规划旅途行程还是编写可行的代码，Manus 能高效执行并输出可视化成果。如下是我收集的一些案例，大家可以通过案例回放来切实感受一下 manus 的强大。

官方案例：https://manus.im/usecases

个人使用案例：[https://s7zkncrc8l.feishu.cn/base/RFl2bVZa8aBrf9sNAxKcJe6Ynjb?table=tbldohmKAenye18s&view=vewRc5mcyl](https://s7zkncrc8l.feishu.cn/base/RFl2bVZa8aBrf9sNAxKcJe6Ynjb?table=tbldohmKAenye18s&view=vewRc5mcyl)

manus 平台采用多智能体架构，在云端虚拟机执行，只需在浏览器中即可使用 manus

并且在 GIAI 基准测试中超越了 openAI 的 deep research，展现出卓越的任务处理能力。以下是测评结果（来自官网）：

![[Abs4bj60xoFdk2xfAkDcaRWdnke.png]]

# manus 工作流程

![[GuhLbi1SyoUVYrxSwE9cJ2RYnQg.png]]

用户向 Manus 提出任务请求后，任务规划器（Claude）会理解用户需求并生成一个详细的任务清单，然后任务执行调度器（Qwen）根据这个清单分配给不同的 Agents 去执行各自的子任务，这些 Agents 在虚拟机这个 Linux 系统的工作间中使用浏览器和 Python 环境完成各自的任务，并将结果保存，当所有子任务完成后，任务汇总生成器（Claude）会收集并整合这些结果，最后生成一个完整的报告发送给用户，这样用户就得到了他们需要的解决方案。

这个过程就像是一个团队合作的项目，用户提出需求，大脑（任务规划器）制定计划，助手们（Agents）执行任务，最后大脑再次介入，整合所有结果，并向用户报告。这样，用户就可以得到他们需要的结果，这个过程也无需人为的编排工作流程，完全由 manus 来自主控制完成。

# coze 和 manus 的对比

我们把刚出现 manus 产品和已经推出一段时间的扣子平台做个比较，来加深对 manus 的了解。

Manus 是一个通用的智能体，而扣子是一个 AI 应用创建平台。扣子是通过人为的方式定义一些工作流程，来实现对任务的自动化处理。Manus 是利用 AI 大模型的泛化能力、智能性去自动规划工作流程，来实现任务的处理。

这就引出一个观点：<strong>“Less Structure, More Intelligence”</strong>（更少结构，更多智能）。<strong>AI 应用的未来趋势是减少人为设计的结构化流程，更多地依靠模型自身的智能能力自然演化出各种能力。</strong>

- 目前业内很多平台（如扣子 Coze 等）都在使用 workflow（工作流）来构建 AI 应用。这种方式通过人为设计的结构化流程，明确规定 AI 模型的行为和任务执行顺序。
- 一些业内人士（如 Flood Sung）认为，这种人为设计的 workflow 结构实际上限制了模型本身的能力发挥。他们认为，workflow 这种结构化的设计方式是短期的解决方案，长期来看并没有价值，最终会被模型自身的智能能力所取代。
- Manus 就是一个典型的例子，它没有使用任何人为搭建的 workflow，而是完全依靠模型自身的智能能力自然演化出各种能力。这种设计理念强调模型本身的智能和泛化能力，而非通过人为设计的结构去“教会”模型如何工作。

对于这种观点，不知道大家怎么看？欢迎留言讨论。
