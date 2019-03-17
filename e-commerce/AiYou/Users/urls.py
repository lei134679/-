"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = 2019/3/11
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    # ==========================用户模块===============================
    url(r'^u_register/$', views.u_register, name='u_register'),
    url(r'^u_login/$', views.u_login, name='u_login'),
    url(r'^create_code_img/$', views.create_code_img, name='create_code_img'),
    url(r'^u_logout/$', views.u_logout, name='u_logout'),
    url(r'^u_message/$', views.u_message, name='u_message'),
    url(r'^alt_pwd/$', views.alt_pwd, name='alt_pwd'),
    url(r'^index/$', views.index, name='index'),
    url(r'^sjzx/$', views.sjzx, name='sjzx'),
    url(r'^ajax_reg/$', views.ajax_reg),
    # ==========================地址模块===============================
    url(r'^address/', views.address, name='address'),
    url(r'^del_addr/$', views.del_addr, name='del_addr'),
]