from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    """用户学习的主题""" 
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #使其只显示与当前登录的用户相关联的数据 ||代码没问题，但显示有问题，不管哪个账户都显示所有的主题 https://learndjango.com/tutorials/django-best-practices-referencing-user-model
    text = models.CharField(max_length=200) 
    date_added = models.DateTimeField(auto_now_add=True) 
    def __str__(self): 
        """返回模型的字符串表示""" 
        return self.text
    

class Entry(models.Model): 
    """学到的有关某个主题的具体知识""" 
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) 
    text = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True) 
 
    class Meta: 
        verbose_name_plural = 'entries' 
 
    def __str__(self): 
        """返回模型的字符串表示""" 
        return self.text[:50] + "..." 
