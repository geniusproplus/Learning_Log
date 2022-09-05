"""为应用程序users设定url模式"""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views
app_name = 'users' #这里写了users path那里就不用加了
urlpatterns = [
    #登录页面
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'), #https://blog.csdn.net/weixin_43009363/article/details/87735445
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
