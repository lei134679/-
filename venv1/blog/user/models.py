from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import django.utils.timezone as timezone
# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='用户编号')
    age = models.CharField(max_length=200, null=True, blank=True, verbose_name='用户年龄')
    gender = models.CharField(max_length=50, null=True, blank=True, verbose_name='用户性别')
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name='联系方式')
    addr = models.CharField(max_length=255, null=True, blank=True, verbose_name='用户地址')
    img = models.ImageField(upload_to='static/imgs/', default='static/imgs/default.png', verbose_name='用户头像')
    user = models.OneToOneField(User, on_delete=models.Model, verbose_name='关联')


class ArticleType(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='类型id')
    type = models.CharField(max_length=100, verbose_name='文章类型')
    def __str__(self):
        return self.type


class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='编号')
    title = models.CharField(max_length=255, verbose_name='标题')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_time = models.DateTimeField(auto_now=True, verbose_name='上次修改时间')
    content = HTMLField(verbose_name='内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    type = models.ForeignKey(ArticleType, on_delete=models.CASCADE, verbose_name='所属类型')
    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='评论编号')
    content = models.CharField(max_length=255, verbose_name='评论内容')
    null = models.ForeignKey('self', null=True, verbose_name='评论')
    user_cont = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户评论')
    art_cont = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='评论文章')
    def __str__(self):
        return self.content