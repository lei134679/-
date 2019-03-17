from django.db import models
from django.contrib.auth.models import User


# 用户类Users
class Users(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='用户编号')
    mickname = models.CharField(max_length=255, unique=True, verbose_name='用户昵称')
    age = models.CharField(max_length=200, verbose_name='用户年龄')
    gender = models.CharField(max_length=50, null=True, verbose_name='用户性别')
    header = models.ImageField(upload_to='static/images/users_head/',
                               default='static/images/users_head/default.png'
                               , verbose_name='用户头像')
    phone = models.CharField(max_length=50, verbose_name='联系方式')
    status = models.IntegerField(default=1, verbose_name='用户状态')
    user = models.OneToOneField(User, on_delete=models.Model, verbose_name='关联')


# 收货地址Address
class Address(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='地址编号')
    recv_name = models.CharField(max_length=255, verbose_name='收货人姓名')
    recv_phone = models.CharField(max_length=50, verbose_name='收货人联系方式')
    province = models.CharField(max_length=255, verbose_name='省区')
    city = models.CharField(max_length=255, verbose_name='市区')
    country = models.CharField(max_length=255, verbose_name='县区')
    desc = models.CharField(max_length=255, verbose_name='详细描述')
    status = models.BooleanField(default=True,verbose_name='是否默认地址')
    users = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='所属用户')