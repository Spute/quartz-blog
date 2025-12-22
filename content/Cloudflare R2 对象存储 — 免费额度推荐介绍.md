## 前言

Cloudflare R2 是一款兼容 S3 API 的全球对象存储服务，最大的亮点是 **真正的免出站流量（egress）费用**，这意味着你把数据从 R2 发送到互联网时不会产生额外带宽费用，非常适合 Web 资源托管和中大型内容分发场景。[Cloudflare Docs+1](https://developers.cloudflare.com/r2/pricing/?utm_source=chatgpt.com)

## 💡 免费额度

Cloudflare 为 R2 的 **标准存储（Standard Storage）** 提供了每月免费额度，让你在初期使用或小规模应用时几乎不用付费：

✅ **10 GB‑month 存储容量免费**  
也就是说，只要你存储的数据量不超过 10 GB（按平均每日峰值算的 GB‑month），这一部分的存储是免费的。[Cloudflare Docs](https://developers.cloudflare.com/r2/pricing/?utm_source=chatgpt.com)

✅ **1 百万次 Class A 操作免费**  
包括创建、写入、列举对象等操作，每月前 1 000 000 次操作不收费。[Cloudflare Docs](https://developers.cloudflare.com/r2/pricing/?utm_source=chatgpt.com)

✅ **10 百万次 Class B 操作免费**  
针对读取、查询等操作，前 10 000 000 次也无需付费（例如 `GetObject` 请求）。[Cloudflare Docs](https://developers.cloudflare.com/r2/pricing/?utm_source=chatgpt.com)

✅ **出站带宽 (egress) 永远免费**  
无论是静态网站资源还是数据下载，R2 本身不会对数据传输量收费。[Cloudflare Docs](https://developers.cloudflare.com/r2/pricing/?utm_source=chatgpt.com)

📌 注意：免费额度只适用于标准存储，不包括“**不频繁访问存储（Infrequent Access）**”类别。[Cloudflare Docs](https://developers.cloudflare.com/r2/pricing/?utm_source=chatgpt.com)

---

### 🎯 适合谁用？

- **个人开发者或初创产品** — 小规模项目很容易在免费额度内运行。
    
- **静态资源托管** — 与 Cloudflare CDN 配合，可进一步优化成本。
    
- **面向全球用户的应用** — 免出站费用降低了跨区域分发的成本。
    

---

### 🧠 总结

Cloudflare R2 的免费额度十分友好：**10 GB 存储 + 1M 写入 + 10M 读取/列举操作/月** 再加上 **零出站流量费**，对于初期用户或小流量应用来说，这几乎是一种“**免费可用的对象存储**”解决方案。想部署静态网站资源、媒体内容或大文件存储时，不妨优先考虑 R2