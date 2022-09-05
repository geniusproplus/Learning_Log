# learning_log

## 1. Azure部署Django网页系列视频

- https://www.youtube.com/playlist?list=PLlrxD0HtieHjHCQ0JB_RrhbQp_9ccJztr

## 2. Django网页应用快速在Azure创建（微软官方文档）：

- https://docs.microsoft.com/zh-cn/azure/app-service/quickstart-python?tabs=django%2Cwindows%2Cazure-portal%2Clocal-git-deploy%2Cdeploy-instructions-azportal%2Cterminal-powershell%2Cdeploy-instructions-zip-azcli

## 3. github部署Django网页（微软官方文档）：

- https://docs.microsoft.com/zh-CN/azure/app-service/deploy-github-actions?tabs=applevel

## 4. 网页部署过程中的问题处理

### DisallowedHost at / (解决)

- 在settings.py文件中设置debug和allowed_posts

### 安全验证问题处理有问题 （解决了一半）

- Forbidden (403) CSRF verification failed. Request aborted.

- 可能是从第20.2.6小节的内容没有做  《Python编程：从入门到实践》P422-P435 （托管方案是Azure不是书中的Heroku，这个猜测不对）

    （这个猜测暂未证明）或者是因为sqlite3的原因，需要连接azure数据库，可以看看这个playlist：https://www.youtube.com/watch?v=Z4gLolNTM5I（数据库连接）


- 解决方案：注释掉settings.py中的MIDDLEWARE列表中的'django.middleware.csrf.CsrfViewMiddleware'

    解决方案的缺点：注释掉这一行代码，django不在执行CSRF安全验证，网页会很容易被攻击。

    注册：开始到结束都正常

    登录：登录界面正常，但点击登录按钮后还是返回Forbidden (403)CSRF verification failed. Request aborted.

- 网站的功能大致就这些，都是换汤不换药，下一步，该考虑网页安全性的问题了。

## 5. 网页开发学习路径（初步判断，没有经过调研）

- 网页开发基础内容：功能实现（函数）与应用部署

- 网页开发进阶内容：界面美化

- 网页开发高级内容：网页安全

