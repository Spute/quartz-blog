---
title: 理解 SSH 认证
---

## 前言

回顾一下之前一直误解的内容。之前一直认为“在 SSH 密钥认证过程中，实际上是相反的 - 它使用公钥加密，私钥解密。”

如今才明白，SSH 登录认证并没有“公钥加密/私钥解密”。使用的是 <strong>数字签名</strong>，不是加密/解密。安全性是通过签名不可伪造来确保的。

## 非对称加密概念

非对称加密是密码学的一种方法，它使用 <strong>一对密钥</strong>（对称加密只有一个密钥，发送方和接收方都用同一个密钥）：

- <strong>公钥（Public Key）</strong>：可以公开给所有人。
- <strong>私钥（Private Key）</strong>：必须保密，只能由拥有者自己保存。

<strong>非对称加密是底层技术</strong>，<strong>加密模型和签名模型是它的两种不同应用场景</strong>，只是密钥使用方向不同。

### 场景

- <strong>加密模型</strong>：公钥加密 → 私钥解密。常用于保护机密内容。

  - <strong>安全邮件：</strong>发件人使用收件人的 <strong>公钥</strong> 加密邮件内容，收件人用自己的 <strong>私钥</strong> 解密。
  - <strong>TLS/HTTPS 密钥交换：</strong>客户端使用服务器的 <strong>公钥</strong> 加密随机会话密钥，服务器用自己的 <strong>私钥</strong> 解密以生成对称加密通道。
- <strong>签名模型</strong>：私钥签名 → 公钥验证。用于验证身份和完整性。

  - <strong>软件包完整性验证：</strong>开发者用自己的 <strong>私钥</strong> 对软件包生成签名，用户用开发者的 <strong>公钥</strong> 验证签名确保未被篡改。
  - <strong>SSH 公钥认证：</strong>客户端用自己的 <strong>私钥</strong> 对服务器发送的 challenge 签名，服务器用客户端的 <strong>公钥</strong> 验证签名确认身份。

## SSH 认证流程：

![[QI3SbeZ8EoP48DxNAucc8BPRnFh.png]]

在 <strong>SSH 公钥认证</strong> 中，客户端和服务器的<strong>步骤</strong>交互大致如下：

1. <strong>客户端生成一对密钥</strong>（私钥 + 公钥）。
2. <strong>公钥放到服务器</strong>（`~/.ssh/authorized_keys`）。
3. 当客户端发起连接时，服务器会：

   - 生成一个随机数（challenge）。
   - 用存储的 <strong>公钥</strong> 验证客户端的 <strong>签名</strong>，而不是用它来加密数据。

### 好处

这种方式的安全性在于：

- 即使有人截获了公钥，因为在 ssh 认证过程中只负责验证签名
- 只有持有私钥的一方才能生成签名，需要保管好
- SSH 认证时，客户端用私钥在本地生成签名，网络上传输的只是 <strong>签名结果</strong>。私钥从来不会通过网络传输，这是安全性的关键。

## SSH 密钥配置步骤

1. 在客户端生成 SSH 密钥对:

```bash
ssh-keygen -t rsa -b 4096
```

按回车后会在 ~/.ssh/ 目录下生成两个文件:

- id_rsa (私钥)
- id_rsa.pub (公钥)

1. 将公钥复制到远程服务器:

```bash
ssh-copy-id username@remote_host
```

或者手动复制（手动复制时，谨慎把换行符增加了，否则不生效）:

```bash
cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

1. 设置远程服务器 SSH 配置的权限:

```bash
ssh username@remote_host "chmod 700 ~/.ssh; chmod 600 ~/.ssh/authorized_keys"
```

1. 测试 SSH 密钥登录:

```bash
ssh username@remote_host
```

<strong>指定密钥登录：</strong>

是-i 后面接的是私钥文件，而不是公钥。因为对于本地机器是用私钥解密的。

```
ssh -i ~/.ssh/id_rsa flexivsu@10.24.13.30
```

1. (可选)如果要提高安全性,可以编辑远程服务器的 SSH 配置文件禁用密码登录:

```bash
sudo nano /etc/ssh/sshd_config
```

修改或添加以下行:

```
PasswordAuthentication no
```

然后重启 SSH 服务:

```bash
sudo systemctl restart sshd
```

1. 确保开启公钥验证:

```
# 在服务端中
cat /etc/ssh/sshd_config

# 确保包含以下设置:
PubkeyAuthentication yes
```

### 客户端自定义 ssh 配置

在~/.ssh/config 中添加配置使连接更方便:

```
Host git.flexiv.cloud
  Hostname git.flexiv.cloud
  Port 522
  IdentityFile ~/.ssh/gitlab/id_rsa

Host termux
  HostName 100.102.133.20
  Port 8022
  User u0_a633
```
