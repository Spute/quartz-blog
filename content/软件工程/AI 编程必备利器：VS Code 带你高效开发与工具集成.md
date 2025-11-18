---
title: AI 编程必备利器--VS Code 带你高效开发与工具集成
---

## 前言

如果你想学习 AI 编程，VS Code 是不错的选择。它支持 Python、JavaScript 等多种语言和 AI 工具集成，能够大幅提升开发效率，方便调试与实验，是入门和进阶 AI 编程的工具。

VS Code 是开源的代码编辑器，生态和插件体系非常强大，很多 AI 编辑器（如 <strong>Cursor、Windsurf</strong>）都基于它的架构衍生。<strong>Claude Code</strong> 这类 AI 工具也提供 VS Code 集成。

学习 VS Code 的意义在于，它不仅是编程的高效利器，还能通过插件、AI 辅助和跨平台支持，帮助开发者提升生产力，建立现代化的开发工作流，对初学者和专业人士都有长远价值。

## 下载安装

1. 访问官网

首先，打开浏览器，访问 VSCode 官方网站：[https://code.visualstudio.com/](https://code.visualstudio.com/)

1. 选择下载版本
   VSCode 官网会根据你的操作系统自动推荐合适的版本。你也可以点击按钮下方的 <u>other platforms</u>，选择其他版本。

- Windows 系统：提供 User Installer 和 System Installer 两种安装包
- Mac 系统：提供 `.zip` 和 `.dmg` 两种安装包
- Linux 系统：提供多种安装包格式

1. 使用下载包安装即可

## 快捷键

学习快捷键的可以提高效率，减少重复操作，节省时间，让注意力更专注。同时还能提升专业感和操作流畅度。

PS: 标黄的为常用内容

<table>
<tr>
<td>类别<br/></td><td>快捷键组合<br/></td><td>功能描述<br/></td></tr>
<tr>
<td>快速跳转<br/></td><td>Ctrl+P<br/></td><td>快速打开文件<br/></td></tr>
<tr>
<td>快速跳转<br/></td><td>Ctrl+Shift+P<br/></td><td>进入命令面板模式<br/></td></tr>
<tr>
<td>编辑器与窗口管理<br/></td><td>Ctrl+N<br/></td><td>新建文件<br/></td></tr>
<tr>
<td>编辑器与窗口管理<br/></td><td>Ctrl+Shift+`<br/></td><td>新建终端<br/></td></tr>
<tr>
<td>编辑器与窗口管理<br/></td><td>Ctrl+Tab<br/></td><td>文件之间切换<br/></td></tr>
<tr>
<td>编辑器与窗口管理<br/></td><td>Ctrl+Shift+N<br/></td><td>打开一个新的VS Code编辑器<br/></td></tr>
<tr>
<td>编辑器与窗口管理<br/></td><td>Ctrl+W<br/></td><td>关闭当前窗口<br/></td></tr>
<tr>
<td>编辑器与窗口管理<br/></td><td>Ctrl+Shift+W<br/></td><td>关闭当前的VS Code编辑器<br/></td></tr>
<tr>
<td>编辑器与窗口管理<br/></td><td>Ctrl+\<br/></td><td>切出一个新的编辑器窗口（分屏）<br/></td></tr>
<tr>
<td>编辑器与窗口管理<br/></td><td>Ctrl+1/2/3<br/></td><td>切换左中右3个编辑器窗口<br/></td></tr>
<tr>
<td>代码编辑 - 格式调整<br/></td><td>Ctrl+[ / ]<br/></td><td>代码行向左或向右缩进<br/></td></tr>
<tr>
<td>代码编辑 - 格式调整<br/></td><td>Ctrl+C / V<br/></td><td>复制或剪切当前行/当前选中内容<br/></td></tr>
<tr>
<td>代码编辑 - 格式调整<br/></td><td>Shift+Alt+F<br/></td><td>代码格式化<br/></td></tr>
<tr>
<td>代码编辑 - 格式调整<br/></td><td>Alt+Up / Down<br/></td><td>将当前行向上或向下移动一行<br/></td></tr>
<tr>
<td>代码编辑 - 格式调整<br/></td><td>Shift+Alt+Up / Down<br/></td><td>将当前行向上或向下复制一行<br/></td></tr>
<tr>
<td>代码编辑 - 格式调整<br/></td><td>Ctrl+Enter<br/></td><td>在当前行下方插入一行<br/></td></tr>
<tr>
<td>代码编辑 - 格式调整<br/></td><td>Ctrl+Shift+Enter<br/></td><td>在当前行上方插入一行<br/></td></tr>
<tr>
<td>代码编辑 - 光标相关<br/></td><td>Home / End<br/></td><td>移动到行首/行尾<br/></td></tr>
<tr>
<td>代码编辑 - 光标相关<br/></td><td>Ctrl+End / Home<br/></td><td>移动到文件结尾/开头<br/></td></tr>
<tr>
<td>代码编辑 - 光标相关<br/></td><td>Shift+End / Home<br/></td><td>选择从光标到行尾/行首的内容<br/></td></tr>
<tr>
<td>代码编辑 - 光标相关<br/></td><td>Ctrl+Delete<br/></td><td>删除光标右侧的所有内容<br/></td></tr>
<tr>
<td>代码编辑 - 光标相关<br/></td><td>Shift+Alt+Right/Left<br/></td><td>扩展/缩小选取范围<br/></td></tr>
<tr>
<td>代码编辑 - 光标相关<br/></td><td>Alt+Shift+鼠标左键 或 Ctrl+Alt+Down/Up<br/></td><td>多行编辑(列编辑)<br/></td></tr>
<tr>
<td>代码编辑 - 光标相关<br/></td><td>Ctrl+D<br/></td><td>下一个匹配的也被选中<br/></td></tr>
<tr>
<td>代码编辑 - 光标相关<br/></td><td>Ctrl+U<br/></td><td>回退上一个光标操作<br/></td></tr>
<tr>
<td>代码编辑 - 光标相关<br/></td><td>Ctrl+Z<br/></td><td>撤销上一步操作<br/></td></tr>
<tr>
<td>代码编辑 - 光标相关<br/></td><td>Ctrl+Y<br/></td><td>恢复上一步操作<br/></td></tr>
<tr>
<td>代码编辑 - 光标相关<br/></td><td>Ctrl+S<br/></td><td>手动保存<br/></td></tr>
<tr>
<td>代码编辑 - 重构代码<br/></td><td>Shift+F12<br/></td><td>找到所有的引用<br/></td></tr>
<tr>
<td>代码编辑 - 重构代码<br/></td><td>Ctrl+F2<br/><br/></td><td>同时修改本文件中所有匹配的<br/></td></tr>
<tr>
<td>代码编辑 - 重构代码<br/></td><td>F8<br/></td><td>跳转到下一个 Error 或 Warning<br/></td></tr>
<tr>
<td>代码编辑 - 查找替换<br/></td><td>Ctrl+F<br/></td><td>查找<br/></td></tr>
<tr>
<td>代码编辑 - 查找替换<br/></td><td>Ctrl+H<br/></td><td>查找替换<br/></td></tr>
<tr>
<td>代码编辑 - 查找替换<br/></td><td>Ctrl+Shift+F<br/></td><td>全文查找<br/></td></tr>
<tr>
<td>代码编辑 - 查找替换<br/></td><td>Ctrl+Shift+H<br/></td><td>全文查找替换<br/></td></tr>
<tr>
<td>显示相关<br/></td><td>F11<br/></td><td>全屏显示(再次按则恢复)<br/></td></tr>
<tr>
<td>显示相关<br/></td><td>Ctrl +/-<br/><br/></td><td>放大或缩小(以编辑器左上角为基准)<br/></td></tr>
<tr>
<td>显示相关<br/></td><td>Ctrl+B<br/></td><td>侧边栏显示或隐藏<br/></td></tr>
<tr>
<td>显示相关<br/></td><td>Ctrl+Shift+E<br/></td><td>显示资源管理器<br/></td></tr>
<tr>
<td>显示相关<br/></td><td>Ctrl+Shift+G+G<br/></td><td>显示源代码管理<br/></td></tr>
<tr>
<td>显示相关<br/></td><td>Ctrl+Shift+D<br/></td><td>显示 Debug<br/></td></tr>
<tr>
<td>显示相关<br/></td><td>Ctrl+Shift+U<br/></td><td>显示 Output<br/></td></tr>
</table>

## python 插件

### Pylance

Python 的一款快速、功能丰富的语言支持扩展

lance 中文是长矛的意思，python 的工具极速冲刺

#### <strong>主要功能</strong>

Pylance 为 Python 3 提供了许多强大的功能，包括：

- <strong>文档字符串 (Docstrings)</strong>：快速查看函数或类的说明文档
- <strong>函数签名提示 (Signature help)</strong>：包含类型信息的参数提示
- <strong>参数建议 (Parameter suggestions)</strong>：输入函数时自动提示可用参数
- <strong>代码补全 (Code completion)</strong>：智能补全变量、方法和模块
- <strong>自动导入 (Auto-imports)</strong>：支持一键添加或移除 import 语句
- <strong>实时错误和警告提示 (Diagnostics)</strong>：边写代码边报告潜在问题
- <strong>代码大纲 (Code outline)</strong>：快速浏览代码结构
- <strong>代码导航 (Code navigation)</strong>：跳转到定义、查找引用等
- <strong>类型检查模式 (Type checking mode)</strong>：基于 Pyright 的类型检查
- <strong>多工作区支持 (Multi-root workspace)</strong>：原生支持多项目工作区
- <strong>IntelliCode 兼容</strong>：与 AI 驱动的智能代码补全无缝结合
- <strong>Jupyter Notebooks 兼容</strong>：在交互式笔记本中使用
- <strong>语义高亮 (Semantic highlighting)</strong>：提供更精细的代码语义着色

#### 常用功能：

函数定义跳转，静态类型检查

<strong>添加项目根目录</strong>。比如 django 会将 apps 目录设为根目录。

1. 按下 `Ctrl + Shift + P`（Windows/Linux）或 `Cmd + Shift + P`（macOS）打开命令面板。
2. 在命令面板中输入 `Preferences: Open Workspace Settings (JSON)` 并选择它。

![[NxjYbv767oOxNExtl8Scvvc7nJc.png]]

- 这将直接打开 `settings.json` 文件，你可以在这里添加或修改配置。

```
<em>// 添加项目根目录到Python路径</em>
    "python.analysis.extraPaths": [
        "./apps",
        "./fvr_asd"
    ],
```

## javascript 插件

## 代码风格检查插件 ESLint

这个是最流行的代码风格检查插件，有超过 670 万的安装量。你可以在 `.eslintrc.json` 中配置。

## 常用场景

### 查询所有引用

vscode 自带的功能

在“编辑器区域”中打开引用，而不只是小窗口查看。

![[MDcGbLo9lo1ClwxZUJScJzPRnHg.png]]

### 折叠/展开代码

Ctrl+Shift+P 打开命令框

输入“fold”查看折叠

输入“fold level”折叠不同的级别

输入“unfold”展开

![[XGvObloFMo1ehpxE8Rsc0Tc4n0b.png]]
