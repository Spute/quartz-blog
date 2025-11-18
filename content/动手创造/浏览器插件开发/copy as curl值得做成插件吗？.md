---
title: copy as curl 值得做成插件吗？
---

使用 curl 最快捷的方式

打开 chrome devtools -> network panel -> 选择具体的网络请求 -> copy as curl (bash)

这个操作链路挺长的，转换成本地调试，域名需要手动改成本地的，bash 自带换行，直接显示在一行方便修改

curl 'http://asdbase-dev.flexiv.cloud/api/account/v1/roles/9/permission/' \

-H 'Accept: application/json, text/plain, */*' \

-H 'Accept-Api-Language: zh-CN' \

-H 'Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7' \

-H 'Authorization: Token 5268d209b931decfec9d046973c522a6ed1b048ce5c65d6d70d12ae4705be1fa' \

-H 'Cache-Control: no-cache' \

-H 'Connection: keep-alive' \

-b 'csrftoken=s2HFdqDF43g9BO6zJE7vxfjZ0wgHIHtp; sessionid=ppj7549ywoqtsmlfw3tld92fgquloq79' \

-H 'Pragma: no-cache' \

-H 'Referer: http://asdbase-dev.flexiv.cloud/admin/role' \

-H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36' \

-H 'X-timezone: Asia/Shanghai' \

--insecure
