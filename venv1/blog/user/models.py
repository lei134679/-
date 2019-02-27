from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import django.utils.timezone as timezone
# Create your models here.


class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='编号')
    title = models.CharField(max_length=255, verbose_name='标题')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_time = models.DateTimeField(auto_now=True, verbose_name='上次修改时间')
    content = HTMLField(verbose_name='内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')