# Quartz v4

> “敞开门工作的人会被各种打扰，但他们也偶尔会获得关于世界是什么、什么才重要的线索。”——理查德·哈明

Quartz 是一套工具，帮助你免费将你的[数字花园](https://jzhao.xyz/posts/networked-thought)和笔记发布为网站。
Quartz v4 进行了彻底重写，专注于终端用户的可扩展性和易用性。

🔗 阅读文档并开始使用：https://quartz.jzhao.xyz/

# 使用说明
- 本地构建并预览
`npx quartz build --serve`
- 推送到github自动部署
`npx quartz sync`

| 命令                              | 会不会执行 `git pull`                      | 适用场景                 | 风险                        |
| ------------------------------- | ------------------------------------- | -------------------- | ------------------------- |
| **`npx quartz sync`**           | ✔ 会执行 `git pull --rebase --autostash` | 每次正常更新内容推送时          | 可能遇到远程冲突                  |
| **`npx quartz sync --no-pull`** | ❌ 不会执行 git pull                       | **首次部署**用、确定不需要拉取远程时 | 如果远程有内容，会被覆盖（push 时失败或冲突） |
