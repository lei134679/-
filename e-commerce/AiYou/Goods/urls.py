"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = 2019/3/14
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
    url(r'^add_goods/(\d+)/$', views.add_goods, name='add_goods'),
    url(r'^ajax_type/$', views.ajax_type, name='ajax_type'),
    url(r'^look_goods/(\d+)/$', views.look_goods, name='look_goods'),
    url(r'^del_goods/(\d+)/(\d+)/$', views.del_goods, name='del_goods'),
    url(r'^alt_goods/(\d+)/(\d+)/$', views.alt_goods, name='alt_goods'),
    url(r'^details_goods/(\d+)/$', views.details_goods, name='details_goods'),
]