"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = 2019/2/27
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
    # *****************用户处理****************************
    url(r'^index/$', views.index, name='index'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^details/$', views.details, name='details'),
    url(r'^alter/$', views.alter, name='alter'),
    url(r'^(\d+)/data/$', views.data, name='data'),
    # 验证码
    url(r'^create_code_img/$', views.create_code_img, name='create_code_img'),
    # *****************文章处理***************************
    url(r'^add_article/$', views.add_article, name='add_article'),
    url(r'^success_article/$', views.success_article, name='success_article'),
    url(r'^list_article/$', views.list_article, name='list_article'),
    url(r'^(\d+)/detalis_article/$', views.detalis_article, name='detalis_article'),
    url(r'^(\d+)/del_article/$', views.del_article, name='del_article'),
    url(r'^(\d+)/update_article/$', views.update_article, name='update_article'),
]