---
title: coze 技巧
---

# 技巧：分而治之，简化复杂工作流的开发

越是复杂的工作流，它的节点也就越多，随之带来的是编排难度、调试复杂度的指数级上升。那今天分享一个复杂的工作流的构建技巧。使用这种方式可以减少调试过程的难度，减少出错的概率。

这种方式就是：<strong>分而治之。</strong>顾名思义，这个方法就是将复杂的工作流拆分成多个更小更简单的工作流，然后每次只需关注一部分步骤，让实现和调试变得简单。

如下是生成每日英语视频的工作流，拥有挺多节点的。对于这种情况我们就可以使用分而治之的方法，来进行简化。

![[GzMGbfdZXotLy0x4WVHcPQEHnJb.png]]

具体步骤如下：

1. <strong>按功能和特点，拆分合适的板块。</strong>比如这个工作流可以拆分为：口播稿生成、语口播音合成、视频素材准备、剪映草稿合成。这样好处是如果“口播稿生成”板块很耗时，经过拆分后其他板块的调试可以独立进行，不用等待前置模块的运行。
2. 如下，选择中多个需要封装成工作流的节点，然后点击封装工作流：

![[Im90bDJ3koUlXSxwDxzcWVyknHb.png]]

1. 封装完后，刚选中的节点就被替换成子工作流

![[TSQYbYGw9obJkjxzV3icOXqBnAd.png]]

1. 如下操作，即可进入子工作流，进行编辑和调试了

![[V6AHbLoLdosUnjxoR3qcTb6QnYd.png]]

# 技巧：一种免费无限制的工作流分享方法

工作流作为实现复杂业务的关键。出于分享工作流或是请求帮助的时候，我们会需要将工作流复制到其他地方。而 coze 官方将“复制到其它空间”这个功能设为收费项目。

这里给大家分享一个免费且无限制的工作流分享方法。

![[CyM6bgNiwoJKBHxdcFOcmhHon9e.png]]

操作步骤非常简单：

1. 选择需要复杂的节点。可以直接使用 ctrl+a 全选。如下选中后会出现蓝色的框。

![[JoPkb0b3yogaGIx0eeBcI2QsnPd.png]]

1. 复制粘贴。ctrl+c 即可以文本的形式复制出来，然后可以粘贴到某个文本文件中，如记事本，或者直接微信发送进行分享。内容大概如下：

```sql
{"type":"coze-workflow-clipboard-data","source":{"workflowId":"7516558092160647187","flowMode":0,"spaceId":"7459885111341793318","isDouyin":false,"host":"www.coze.cn"},"json":{"nodes":[{"id":"178066","type":"3","meta":{"position":{"x":-1737.5850123426742,"y":639.3205147382855}},"data":{"nodeMeta":{"description":"调用大语言模型,使用变量和提示词生成回复","icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-LLM-v2.jpg","title":"问题","subTitle":"大模型"},"inputs":{"inputParameters":[{"name":"target","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"100001","name":"target"},"rawMeta":{"type":1}}}}],"llmParam":[{"name":"temperature","input":{"type":"float","value":{"type":"literal","content":"1","rawMeta":{"type":4}}}},{"name":"topP","input":{"type":"float","value":{"type":"literal","content":"0.7","rawMeta":{"type":4}}}},{"name":"responseFormat","input":{"type":"integer","value":{"type":"literal","content":"2","rawMeta":{"type":2}}}},{"name":"maxTokens","input":{"type":"integer","value":{"type":"literal","content":"1024","rawMeta":{"type":2}}}},{"name":"modleName","input":{"type":"string","value":{"type":"literal","content":"豆包·工具调用","rawMeta":{"type":1}}}},{"name":"modelType","input":{"type":"integer","value":{"type":"literal","content":"1706077826","rawMeta":{"type":2}}}},{"name":"generationDiversity","input":{"type":"string","value":{"type":"literal","content":"balance","rawMeta":{"type":1}}}},{"name":"prompt","input":{"type":"string","value":{"type":"literal","content":"","rawMeta":{"type":1}}}},{"name":"enableChatHistory","input":{"type":"boolean","value":{"type":"literal","content":false,"rawMeta":{"type":3}}}},{"name":"chatHistoryRound","input":{"type":"integer","value":{"type":"literal","content":"3","rawMeta":{"type":2}}}},{"name":"systemPrompt","input":{"type":"string","value":{"type":"literal","content":"根据学习目标{{target}}请定制生成一道英语选择题，符合以下要求：  \n1. **目标**：学习{{target}}\n2. **难度**：初级\n3. **格式**：  \n   - 英文问题（留空一个关键词， 问题必须简单，整个问题    5-8个单词，仅问题，不提供答案）  \n   - 中文翻译（不留空，直接展示有正确答案后的整句翻译）\n   - 3个选项（包含1个正确答案和2个干扰项，选项序号用大写A-Z、开始，选项不包含中文翻译）  \n4. 输出格式为: {\nquestion: \"\",\nquestionCN: \"\",\nopts: []\n}","rawMeta":{"type":1}}}}],"settingOnError":{"switch":false,"processType":1,"timeoutMs":600000,"retryTimes":0}},"outputs":[{"type":"object","name":"questionOutput","schema":[{"type":"string","name":"question"},{"type":"string","name":"questionCN"},{"type":"list","name":"opts","schema":{"type":"string"}}],"required":false}],"version":"3"},"_temp":{"bounds":{"x":-1917.5850123426742,"y":639.3205147382855,"width":360,"height":164},"externalData":{"icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-LLM-v2.jpg","description":"调用大语言模型,使用变量和提示词生成回复","title":"大模型","mainColor":"#5C62FF"}}},{"id":"114985","type":"3","meta":{"position":{"x":-1277.5850123426742,"y":639.3205147382855}},"data":{"nodeMeta":{"description":"调用大语言模型,使用变量和提示词生成回复","icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-LLM-v2.jpg","title":"口诀","subTitle":"大模型"},"inputs":{"inputParameters":[{"name":"target","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"100001","name":"target"},"rawMeta":{"type":1}}}},{"name":"questionOutput","input":{"type":"object","schema":[{"type":"string","name":"question"},{"type":"string","name":"questionCN"},{"type":"list","name":"opts","schema":{"type":"string"}}],"value":{"type":"ref","content":{"source":"block-output","blockID":"178066","name":"questionOutput"},"rawMeta":{"type":6}}}}],"llmParam":[{"name":"temperature","input":{"type":"float","value":{"type":"literal","content":"0.85","rawMeta":{"type":4}}}},{"name":"topP","input":{"type":"float","value":{"type":"literal","content":"0.8","rawMeta":{"type":4}}}},{"name":"maxTokens","input":{"type":"integer","value":{"type":"literal","content":"2000","rawMeta":{"type":2}}}},{"name":"responseFormat","input":{"type":"integer","value":{"type":"literal","content":"2","rawMeta":{"type":2}}}},{"name":"modleName","input":{"type":"string","value":{"type":"literal","content":"通义千问·Max","rawMeta":{"type":1}}}},{"name":"modelType","input":{"type":"integer","value":{"type":"literal","content":"1714394325","rawMeta":{"type":2}}}},{"name":"generationDiversity","input":{"type":"string","value":{"type":"literal","content":"balance","rawMeta":{"type":1}}}},{"name":"prompt","input":{"type":"string","value":{"type":"literal","content":"学习目标：{{target}}\n问题：{{questionOutput}}","rawMeta":{"type":1}}}},{"name":"enableChatHistory","input":{"type":"boolean","value":{"type":"literal","content":false,"rawMeta":{"type":3}}}},{"name":"chatHistoryRound","input":{"type":"integer","value":{"type":"literal","content":"3","rawMeta":{"type":2}}}},{"name":"systemPrompt","input":{"type":"string","value":{"type":"literal","content":"# 角色\n你是一位精通英语学习口诀的创作大师，专注于将英语知识的本质核心转化为清晰深刻、易懂易记且朗朗上口的押韵口诀，帮助用户在抖音短视频中深入理解英语。\n\n## 技能\n### 技能 1: 生成英语学习押韵口诀\n1. 用户提供英语学习目标或易混淆知识点后，你需快速提炼知识点本身的核心区别，转化为深刻清晰且押韵精准的口诀。\n2. 每个知识点仅对应一句口诀，禁止超过一句。\n3. 口诀形式固定为上下句字数一致、句尾押韵，如「Few 数得清，Little 量不明」，且韵脚须押得更明显、更易朗读。\n4. 口诀须精准揭示知识点的实质区别，避免表面化、浅显的内容。\n5. 口诀需用回车换行「\\n」分隔，句中禁止任何标点符号，口诀中的单词与解释之间以空格隔开。\n6. 必须确保每个知识点都有对应的一句口诀，不能遗漏或额外添加。\n7. 必须确保每个知识点都会有押韵，确保不会遗漏任何选项，每个选项口诀之间用\\n分割。\n8. 输出格式固定为以下JSON结构：\n```\n{\nkoujue: \"口诀1\\n口诀2\\n口诀3\"\n}\n```\n\n## 限制：\n- 仅围绕英语学习的内容进行创作，不接受任何无关请求。\n- 严格遵守格式要求，确保生成的口诀足够深刻、朗朗上口、韵脚清晰突出，准确把握知识用法本质，便于用户迅速记忆和深度理解。","rawMeta":{"type":1}}}}],"settingOnError":{"switch":false,"processType":1,"timeoutMs":600000,"retryTimes":0}},"outputs":[{"type":"object","name":"koujueOutput","schema":[{"type":"string","name":"koujue"}],"required":false}],"version":"3"},"_temp":{"bounds":{"x":-1457.5850123426742,"y":639.3205147382855,"width":360,"height":164},"externalData":{"icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-LLM-v2.jpg","description":"调用大语言模型,使用变量和提示词生成回复","title":"大模型","mainColor":"#5C62FF"}}},{"id":"120504","type":"3","meta":{"position":{"x":-817.5850123426742,"y":639.3205147382855}},"data":{"nodeMeta":{"description":"调用大语言模型,使用变量和提示词生成回复","icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-LLM-v2.jpg","title":"例题","subTitle":"大模型"},"inputs":{"inputParameters":[{"name":"target","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"100001","name":"target"},"rawMeta":{"type":1}}}},{"name":"questionOutput","input":{"type":"object","schema":[{"type":"string","name":"question"},{"type":"string","name":"questionCN"},{"type":"list","name":"opts","schema":{"type":"string"}}],"value":{"type":"ref","content":{"source":"block-output","blockID":"178066","name":"questionOutput"},"rawMeta":{"type":6}}}},{"name":"koujueOutput","input":{"type":"object","schema":[{"type":"string","name":"koujue"}],"value":{"type":"ref","content":{"source":"block-output","blockID":"114985","name":"koujueOutput"},"rawMeta":{"type":6}}}}],"llmParam":[{"name":"temperature","input":{"type":"float","value":{"type":"literal","content":"1","rawMeta":{"type":4}}}},{"name":"topP","input":{"type":"float","value":{"type":"literal","content":"0.7","rawMeta":{"type":4}}}},{"name":"responseFormat","input":{"type":"integer","value":{"type":"literal","content":"2","rawMeta":{"type":2}}}},{"name":"maxTokens","input":{"type":"integer","value":{"type":"literal","content":"1024","rawMeta":{"type":2}}}},{"name":"modleName","input":{"type":"string","value":{"type":"literal","content":"豆包·工具调用","rawMeta":{"type":1}}}},{"name":"modelType","input":{"type":"integer","value":{"type":"literal","content":"1706077826","rawMeta":{"type":2}}}},{"name":"generationDiversity","input":{"type":"string","value":{"type":"literal","content":"balance","rawMeta":{"type":1}}}},{"name":"prompt","input":{"type":"string","value":{"type":"literal","content":"","rawMeta":{"type":1}}}},{"name":"enableChatHistory","input":{"type":"boolean","value":{"type":"literal","content":false,"rawMeta":{"type":3}}}},{"name":"chatHistoryRound","input":{"type":"integer","value":{"type":"literal","content":"3","rawMeta":{"type":2}}}},{"name":"systemPrompt","input":{"type":"string","value":{"type":"literal","content":"根据学习目标{{input}}和{{questionOutput}}以及{{koujueOutput}}，生成3组对比例句，结构要求：  \n1. **英文例句**（包含目标词汇/语法）  \n2. **中文翻译**  \n3. **强调说明**（用箭头→标注差异，解释核心用法）  \n\n**学习内容**：  \n[在此填写需要学习的词汇/语法点，例如：辨析动词“听”的英文表达：hear/listen to]  \n\n**对比维度**：  \n[明确区分点，例如：动作主动性、结果导向、持续性等]  \n\n**例句要求**：  \n- 例句场景生活化，易理解  \n- 英文例句总单词5个单词，不要多（无需解释）\n- 每组例句结构一致，突出对比  \n- 强调部分用符号→分隔，语言简洁(单词以外一共不要超过10个字)\n\n输出样例为：\n{\n  example:[\n{\"en_US\": \"look at the blackboard\", \"zh_CN\": \"看黑板\", \"explanation\": \"强调→看（动作）→look\"},\n{\"en_US\": \"I can see the flower\", \"zh_CN\": \"我看见这朵花\", \"explanation\": \"强调→看（结果）→see\"},\n{\"en_US\": \"I often watch movies\", \"zh_CN\": \"我经常看电影\", \"explanation\": \"强调→看（持续性）→watch\"}\n]\n}\n","rawMeta":{"type":1}}}}],"settingOnError":{"switch":false,"processType":1,"timeoutMs":600000,"retryTimes":0}},"outputs":[{"type":"object","name":"exampleOutput","schema":[{"type":"list","name":"example","schema":{"type":"object","schema":[{"type":"string","name":"en_US"},{"type":"string","name":"zh_CN"},{"type":"string","name":"explanation"}]}}],"required":false}],"version":"3"},"_temp":{"bounds":{"x":-997.5850123426742,"y":639.3205147382855,"width":360,"height":164},"externalData":{"icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-LLM-v2.jpg","description":"调用大语言模型,使用变量和提示词生成回复","title":"大模型","mainColor":"#5C62FF"}}},{"id":"138873","type":"3","meta":{"position":{"x":-357.58501234267425,"y":639.3205147382855}},"data":{"nodeMeta":{"description":"调用大语言模型,使用变量和提示词生成回复","icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-LLM-v2.jpg","title":"口播稿","subTitle":"大模型"},"inputs":{"inputParameters":[{"name":"questionCN","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"178066","name":"questionOutput.questionCN"},"rawMeta":{"type":1}}}},{"name":"opts","input":{"type":"list","schema":{"type":"string"},"value":{"type":"ref","content":{"source":"block-output","blockID":"178066","name":"questionOutput.opts"},"rawMeta":{"type":99}}}},{"name":"koujue","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"114985","name":"koujueOutput.koujue"},"rawMeta":{"type":1}}}},{"name":"example","input":{"type":"list","schema":{"type":"object","schema":[{"type":"string","name":"en_US"},{"type":"string","name":"zh_CN"},{"type":"string","name":"explanation"}]},"value":{"type":"ref","content":{"source":"block-output","blockID":"120504","name":"exampleOutput.example"},"rawMeta":{"type":103}}}}],"llmParam":[{"name":"modelType","input":{"type":"integer","value":{"type":"literal","content":"1706077826","rawMeta":{"type":2}}}},{"name":"modleName","input":{"type":"string","value":{"type":"literal","content":"豆包·工具调用","rawMeta":{"type":1}}}},{"name":"generationDiversity","input":{"type":"string","value":{"type":"literal","content":"balance","rawMeta":{"type":1}}}},{"name":"temperature","input":{"type":"float","value":{"type":"literal","content":"1","rawMeta":{"type":4}}}},{"name":"topP","input":{"type":"float","value":{"type":"literal","content":"0.7","rawMeta":{"type":4}}}},{"name":"responseFormat","input":{"type":"integer","value":{"type":"literal","content":"2","rawMeta":{"type":2}}}},{"name":"maxTokens","input":{"type":"integer","value":{"type":"literal","content":"1024","rawMeta":{"type":2}}}},{"name":"prompt","input":{"type":"string","value":{"type":"literal","content":"问题：{{questionCN}}\n口诀：{{koujue}}\n选项：{{opts}}\n例子：{{example}}","rawMeta":{"type":1}}}},{"name":"enableChatHistory","input":{"type":"boolean","value":{"type":"literal","content":false,"rawMeta":{"type":3}}}},{"name":"chatHistoryRound","input":{"type":"integer","value":{"type":"literal","content":"3","rawMeta":{"type":2}}}},{"name":"systemPrompt","input":{"type":"string","value":{"type":"literal","content":"请根据问题、问题选项、口诀、例子、帮我生成一个视频教学文案，要求包含以下结构：\n先给出具体题目和选项（格式：问题，A、选项1 B、选项2 C、选项3）\n然后提供记忆口诀\n接着给每个用法配典型例子（用'比如:....强调...所以用...'的句式，这里用中文翻译后的例子说明）\n整体结构一定是:\n问题\n三个选项\n怎么选？\n比如\n三段式的例子（一定是原例子、强调...、所以用..)\n你学会了吗？\n注意每行文案用回车分割\n\n生成结果示例：\n我看见一个苹果\nA：look\nB：see\nC：watch \n怎么选？\n记口诀\n当时动作时，用look\n看到结果就用see\n专注持续，用watch\n比如\n看黑板\n是强调看的动作\n所以就用look\n我看见这朵花\n强调的是看到的结果\n所以用see\n我经常看电影，经常看是持续性的\n所以用watch\n你学会了吗？","rawMeta":{"type":1}}}}],"settingOnError":{"switch":false,"processType":1,"timeoutMs":600000,"retryTimes":0}},"outputs":[{"type":"string","name":"wenan","required":false}],"version":"3"},"_temp":{"bounds":{"x":-537.5850123426742,"y":639.3205147382855,"width":360,"height":164},"externalData":{"icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-LLM-v2.jpg","description":"调用大语言模型,使用变量和提示词生成回复","title":"大模型","mainColor":"#5C62FF"}}}],"edges":[{"sourceNodeID":"178066","targetNodeID":"114985"},{"sourceNodeID":"114985","targetNodeID":"120504"},{"sourceNodeID":"120504","targetNodeID":"138873"}]},"bounds":{"x":-1917.5850123426742,"y":639.3205147382855,"width":1740,"height":164}}
```

1. 复制如上文本。在工作流画布中使用 ctrl+v 粘贴，即可创建除开始、结束节点外的所有节点了。

![[UMFnbgpFHoBgZFxfcDvcfVbKn8c.png]]

PS：注意 浏览器设置要让 coze 网站允许读取粘贴板，否则无法粘贴工作流

![[N773byToroiBaHxpUuzcTtc4nMd.png]]

# 技巧：高效修改输入参数方法

对于包含多个输入变量的场景，使用普通的方式修改调试，如果一个变量一个变量的修改，效率很低。

这里给大家分享一个更高效的修改技巧。

![[KZBub4gPxo5CfXxSNhOcKtURnMc.png]]

如下，点击试运行，打开 json 模式

![[Zy5Tb6x3aojDsQxI2iNcsoTHn9r.png]]

一个个输入变量就聚合到一个 json 内，这样就不用一个个输入框的切换了，而且可以直接复制粘贴源数据，不要太方便。

> [!TIP]
> PS：JSON 是一种轻量级的数据格式，用简单的文本表示键值对和数组，方便人和机器读写。比如：`{"name":"小明", "age":18}` 就是一个 JSON 对象，表示名字是小明，年龄 18 岁。

![[Q11DbdcxwoxXeAxflEkcjexonye.png]]

PS：通过以下方法可以快捷获取源数据。运行完成后找到开始节点，点击展开，然后点击输入傍边的复制按钮，即可复制输入的 json 格式。

![[U4PSb87lyoVd6ox4tsgc9A9qnpb.png]]

# 文本处理节点：巧妙地引入文件类型变量

我们在创建工作流的过程中，会需要引入固定的文件类型的变量，比如如下这些，图片、音频、视频、ppt 等文件类型。如何用变量承接这些内容？

![[TqYqbhC9ZouKpMxcdhZctWU8n3e.png]]

可以选择在开始节点添加变量然后设定默认值，但这会带来一个问题，就是智能体使用这个工作流的时候，会将这些设置了默认值的变量给它设成空字符串，这样会导致 bug。

![[Jii5bEd7goey00xs5X9cTxOSnrf.png]]

此时就可以使用文本处理节点很好地解决这个问题，只需选择合适的变量类型，然后上次对应的文件。再在字符串拼接框中，单独输出使用这个变量，那这个文件变量就会作为这个节点的输出，可以方便地在后续节点睡意引用。

![[RwzDbnwmfoGe3Fx5BBScuwI0nJf.png]]
