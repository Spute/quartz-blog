---
alias: "uya0uopdms96bkplliv6"
date: 2025-12-01
title: Twocast--一款免费开源的 AI 双人播客生成器
---

推荐一个 github 开源的 AI 播客项目。效果还不错，同时支持本地部署。

🌐 官网：[Twocast.app](https://twocast.app/)

![[R4RwbhA3uonevtxtomgc02gFnDh.png]]

## ✨ 主要特性

- 👥 双人播客
- ⏱️ 一键生成 3~5 分钟播客
- 🧠 支持多种生成方式：<strong>主题</strong>  、<strong>链接</strong> 、<strong>文档</strong> （doc/pdf/txt）、<strong>列表页</strong> （5~9 分钟）
- 🌍 多语言支持
- ⬇️ 可下载音频
- 📋 播客内容包含：<strong>音频、大纲、脚本</strong>
- 🔌 支持三大平台：<strong>Fish Audio</strong> 、<strong>Minimax</strong> 、<strong>Google Gemini</strong>

## 🎧 示例播客

- 🇺🇸 English: [Hacker News Hot Articles](https://twocast.app/podcast/vs962a7f-9461-4875-b7c7-2f5aca66126e)
- 🇨🇳 中文: [Hacker News 热榜](https://twocast.app/podcast/vs789e71-b192-4374-93a2-8177f457ba5c)
- 🇨🇳 中文: [V2EX 热榜](https://twocast.app/podcast/vsbed589-6493-4ac2-8217-64d82b1ecafa)

## 🚀 快速开始

### 方法一：本地启动

1. <strong>启动依赖服务</strong>
   ```bash
   ```

docker run -t -d --restart always -p 8080:8080 -e PORT=8080 --name textract bespaloff/textract-rest-api:v4.0.2
docker run -d --restart always --name ffmpeg-api -p 8081:3000 kazhar/ffmpeg-api

```

2. <strong>配置环境变量</strong>
	```bash
cp .env.example .env
```

3. <strong>启动 Postgres 数据库</strong>
   - 创建数据库 `twocast`
   - 修改 `.env` 文件中的 `DATABASE_URL`
   - 初始化数据库：
     ```bash
     ```

npx drizzle-kit push

```

4. <strong>启动项目</strong>
	```bash
yarn && yarn start
```

### 方法二：Docker 一键启动

1. <strong>配置环境变量</strong>
   ```bash
   ```

cp .env.docker .env

```

2. <strong>启动</strong>
	```bash
docker compose up
```

## 环境变量配置

### 🔊 TTS API 配置

- 🎏 <strong>Fish Audio</strong>注册并获取 API Key：[Fish Audio](https://bit.ly/4k7AXHt)，填入 `FISH_AUDIO_TOKEN=`
- 🦾 <strong>Minimax</strong> （可选）[Profile](https://www.minimax.io/platform/user-center/basic-information) 获取 GroupID，填入 `MINIMAX_GROUP_ID=` [API keys](https://www.minimax.io/platform/user-center/basic-information/interface-key) 获取 API Key，填入 `MINIMAX_TOKEN=` 启用：`MINIMAX_ENABLED=1`
- 🌈 <strong>Google Gemini</strong> （可选，费用较高）[Google AI Studio](https://aistudio.google.com/gen-media) 获取 API Key，填入 `GEMINI_TOKEN=` 启用：`GEMINI_ENABLED=1`

### 🤖 LLM API 配置

- 💬 <strong>Chat</strong> ：[OpenRouter](https://openrouter.ai) 获取 API Key，填入 `LLM_API_KEY=`
- 🔍 <strong>Search</strong>  ：[x.ai](https://console.x.ai/) 获取 API Key，填入 `LLM_SEARCH_API_KEY=`
