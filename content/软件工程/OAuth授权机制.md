---
title: OAuth 授权机制
---

- 引入授权层，经过资源所有者确认后，通过资源服务器向第三方颁发临时令牌的方式，获取资源一定范围权限
- [RFC6749](http://www.rfcreader.com/#rfc6749)

## 解决的问题

- 对比传统以账号密码的方式进行第三方授权，oauth 授权解决了哪些问题
  - 安全性：不会泄露账号密码，使用令牌临时授权
  - 便捷性：无需在第三方使用完账号密码后，为了安全修改密码。令牌可以实现一次授权多系统使用，不用更换账号密码
  - 授权范围可控：账号密码一般拥有全部权限，而令牌可以只授权需要的部分，更安全可控。

## 应用场景

- 第三方登录
- 第三方支付
- 获取第三方平台用户信息，如头像等
- ...

## 名词

- <strong>Third-party application</strong>：第三方应用程序，本文中又称"客户端"（client）

  - <strong>HTTP service</strong>：HTTP 服务提供商，本文中简称"服务提供商"，指代“后端”
  - <strong>User Agent</strong>：用户代理，本文中就是指浏览器，指代“前端”。
- <strong>Resource Owner</strong>：资源所有者，本文中又称"用户"（user）
- <strong>Authorization server</strong>：认证服务器，即服务提供商专门用来处理认证的服务器。
- <strong>Resource server</strong>：资源服务器，即服务提供商存放用户生成的资源的服务器。它与认证服务器，可以是同一台服务器，也可以是不同的服务器。

## 运行流程

![[boxcnsqGhBylfp07h5yp6G57qTh.png]]

## oauth2.0 四种授权方式

- 最终都是为了获取授权令牌（token）

<table>
<tr>
<td>Authorzationgrant<br/></td><td>类型<br/></td><td>描述<br/></td><td>特点<br/></td><td>示例<br/></td><td>应用场景<br/></td></tr>
<tr>
<td>code<br/></td><td>授权码<br/></td><td>第三方应用先申请一个授权码，然后再用该码获取令牌<br/></td><td>- 前端传送授权码，令牌只存储在后端，所有与资源服务器的通讯都是由后端完成，所以安全性高<br/>- 前端通过回调获取授权码<br/>- 后端通过回调获取令牌<br/></td><td>```javascripthttps://b.com/oauth/authorize?response_type=code&client_id=CLIENT_ID&redirect_uri=CALLBACK_URL&scope=read```<br/>```javascripthttps://a.com/callback?code=AUTHORIZATION_CODE```<br/>```javascripthttps://b.com/oauth/token?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=authorization_code&code=AUTHORIZATION_CODE&redirect_uri=CALLBACK_URL```<br/></td><td>对安全性要求高的场景：第三方支付<br/><br/></td></tr>
<tr>
<td>implicit<br/></td><td>隐藏式<br/></td><td>相对于授权码方式，省略了授权码步骤，直接获取令牌<br/></td><td>省略授权码步骤，认证服务器直接向前端颁发令牌<br/>- 安全性低<br/>- 前端通过回调获取令牌<br/>- 令牌的位置是 URL 锚点（fragment），而不是查询字符串（querystring）<br/><br/></td><td>```javascripthttps://b.com/oauth/authorize?  response_type=token&  client_id=CLIENT_ID&  redirect_uri=CALLBACK_URL&  scope=read```<br/>```javascripthttps://a.com/callback#token=ACCESS_TOKEN```<br/></td><td>适合纯前端应用<br/></td></tr>
<tr>
<td>password<br/></td><td>密码式<br/></td><td>使用用户名、密码申请令牌<br/></td><td>- 不需要跳转，通过响应获取令牌<br/>- 不安全<br/></td><td>```javascripthttps://oauth.b.com/token?  grant_type=password&  username=USERNAME&  password=PASSWORD&  client_id=CLIENT_ID```<br/></td><td>只适用于其他授权方式都无法采用的情况，而且必须是用户高度信任的应用<br/></td></tr>
<tr>
<td>client_credentials<br/><br/></td><td>凭证式<br/></td><td>使用凭证申请令牌<br/></td><td>- 这种方式给出的令牌，是针对第三方应用的，而不是针对用户的，即有可能多个用户共享同一个令牌<br/>- 不需要跳转，通过响应获取令牌<br/></td><td>```javascripthttps://oauth.b.com/token?  grant_type=client_credentials&  client_id=CLIENT_ID&  client_secret=CLIENT_SECRET```<br/></td><td>适用于没有前端的命令行应用，即在命令行下请求令牌<br/><br/></td></tr>
</table>
