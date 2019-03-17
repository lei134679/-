"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = 2019/3/13
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
    url('^on_store/$', views.on_store, name='on_store'),
    # url('^store_goods/$', views.store_goods, name='store_goods'),
    url('^my_store/$', views.my_store, name='my_store'),
    url('^on_off/(\d+)/$', views.on_off, name='on_off'),
    url('^details_store/(\d+)/$', views.details_store, name='details_store'),
    url('^del_store/(\d+)/$', views.del_store, name='del_store'),
    url('^alt_store/(\d+)/$', views.alt_store, name='alt_store'),
]