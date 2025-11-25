---
title: 问答式理解--HTTPS 协议
category: 长期内容
---

https 协议是什么？

- 是 http 协议的安全版本，在 http 基础上增加 SSL/TLS 加密协议来保护传输的数据

https 协议解决的问题是？

- 保护用户的隐私，防止中间人攻击。比如路由器的中间篡改。

如何做到安全的？

- 通过数字证书实现数据加密、数据完整性校验

https 会话相对于 http 会话多了哪些步骤？

- 服务器通过证书私钥生成公钥，下发<strong>服务器证书</strong>
- 客户端通过<strong>CA 证书</strong>，通过签名验证的方式，验证<strong>服务器证书</strong>是否有效
- 通过证书公钥加密后的会话秘钥
- 服务器使用证书秘钥解密<strong>会话秘钥</strong>
- 客户端服务器之间使用会话秘钥加密和解密后续的通讯数据

![[LfaabYU3ZouPezxkvKncPPxbnrb.png]]

ca 证书在 https 加密中发挥的作用是？

CA 证书在 HTTPS 中的作用是验证服务器身份是否可信。通过<strong>签名机制</strong>确保公钥的真实性，从而让浏览器放心建立加密通信。

客户端的 CA 根证书是怎么获取的？是否可以手动配置？

客户端的 <strong>CA 根证书</strong>（Root CA）确实不是动态获取的，而是通过 <strong>操作系统 / 浏览器厂商</strong> 事先内置的。可以<strong>在操作系统里手动导入 / 删除根证书。或者在浏览器里单独配置。</strong>

https 会话过程中为啥同时使用对称加密和非对称加密？

- 以非对称加密方式下发公钥证书，安全性更高（公钥的泄露，不会影响私钥）
- 以对称加密方式进行后续的会话通信，效率更高（加密解密算法效率高，一端泄露两端受影响）

使用 curl 指令访问 https 时数字证书会保存到哪？

- linux 系统：/etc/ssl/certs/DigiCert_Global_Root_CA.pem

使用 nginx 如何配置 https 证书？

- 配置证书文件和私钥文件

SSL 与 SSH 的联系？

- SSL（Secure Sockets Layer）处于传输层，一种数据传输加密协议，用于保护用户隐私和数据安全。
- SSH（Secure Shell）处于应用层，一种用于在网络上安全执行命令和传输文件的协议。
