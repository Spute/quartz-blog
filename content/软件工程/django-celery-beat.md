---
title: django-celery-beat
---

需求

- 需要一种可以直接管理周期任务的方式，更好地满足日常业务

  - 查看、修改、删除系统定时任务。
  - 手动执行一些不定期的任务，如：发送邮件通知
- 使用者：

  - 业务管理员
  - 开发人员
- 需求特点：低频、特定用户、刚需？

## 展示

## 优缺点

- ROI 高：无需二次开发实现前后端功能
- 前端页面简陋
- 使用独立的鉴权方式（账号密码登录），可能存在安全风险

## 实现方案

- 使用开源包：django-celery-beat
- 启动 celery beat 时使用 scheduler 参数指定自定义的调度器

```python
command: "celery -A flexiv_business_service beat -l info --logfile=./logs/beat.log --scheduler django_celery_beat.schedulers:DatabaseScheduler"
```

- 使用 Django admin 后台，控制调度器
- [Celery 文档](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#using-custom-scheduler-classes)

## 风险&安全性

<table>
<tr>
<td>风险<br/></td><td>- 对本应用的影响<br/></td><td>- 对其他应用的风险<br/></td><td>备注<br/></td></tr>
<tr>
<td>admin中是否存在敏感数据<br/></td><td>无<br/></td><td>无<br/></td><td><br/></td></tr>
<tr>
<td>admin中账号密码泄露<br/></td><td><br/></td><td>无<br/></td><td>接入ad？<br/></td></tr>
<tr>
<td>admin后台的api是否影响之前业务api<br/></td><td>无<br/><br/></td><td><br/></td><td><br/></td></tr>
<tr>
<td><br/></td><td><br/></td><td><br/></td><td><br/></td></tr>
</table>

## 实施

![[boxcnzxk4TvI6UhmakZtoNII9Fh.png]]

- 清理 admin 旧账号，保证账号安全
- 使用域名访问 prms 的 admin 后台
- 例如：http://pdms.defensor-dev.flexiv.cloud/pdms/admin/login/?next=/pdms/admin/
- 如何使用 AD 域账号登录，弃用 django admin 账号密码

  - [https://docs.djangoproject.com/en/4.1/ref/settings/#authentication-backends](https://docs.djangoproject.com/en/4.1/ref/settings/#authentication-backends)

  ```python
  ```

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']

```

- 

- auth模块的
	- auth
	- authenticate方法
	- forms.py的AuthenticationForm

- CSRF
	- https://docs.djangoproject.com/en/4.1/ref/csrf/
	- 中间人攻击，对GET安全，对POST、PUT、DELETE方法不安全



```
