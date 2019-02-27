from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
from . import models


def index(request):
    """
    首页
    :param request:
    :return:
    """
    return render(request, 'user/index.html')


def register(request):
    """
    注册用户，返回登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'user/register.html')
    if request.method == 'POST':
        # 获得页面信息
        username = request.POST['username']
        password = request.POST['password']
        next_password = request.POST['next_password']
        print(password, password, next_password)
        # 数据库查找
        t_user = models.User.objects.filter(username=username)
        # 数据校准
        if username == '':
            return render(request, 'user/register.html', {'mag': '用户名不能为空'})
        elif len(password) < 6:
            return render(request, 'user/register.html', {'mag': '密码必须大于6个字符'})
        elif len(password) > 18:
            return render(request, 'user/register.html', {'mag': '密码必须小于18个字符'})
        elif password != next_password:
            return render(request, 'user/register.html', {'mag': '输入密码不一致'})
        elif len(t_user) != 0:
            return render(request, 'user/register.html', {'mag': '用户名已存在'})
        else:
            try:
                models.User.objects.create_user(username=username, password=password).save()
                return render(request, 'user/login.html')
            except Exception as e:
                print(e)
                return render(request, 'user/register.html', {'mag': '输入有误'})


def user_login(request):
    """
    用户登录及判断，返回上级页面或首页
    :param request:
    :return:
    """
    if  request.method == 'GET':
        try:
            next = request.GET['next']
            return render(request, 'user/login.html', {'next': next})
        except:
            return render(request, 'user/login.html')
    if request.method == 'POST':
        # 获得页面信息
        username = request.POST['username']
        password = request.POST['password']
        # print(username, password, mag)
        user = authenticate(username=username, password=password)
        # print(user)
        if user:
            login(request, user)
            try:
                next = request.POST['next']
                return redirect(next)
            except:
                return render(request, 'user/index.html')
        else:
            return render(request, 'user/login.html', {'mag':'用户名或密码错误'})


@login_required
def user_logout(request):
    """
    退出登录，返回首页
    :param request:
    :return:
    """
    logout(request)
    return render(request, 'user/login.html')


@login_required
def details(request):
    """
    个人资料
    :param request:
    :return:
    """
    return render(request, 'user/details.html')


@login_required
def alter(request):
    """
    修改密码，返回登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'user/alter.html')
    if request.method == 'POST':
        oldpwd = request.POST['oldpassword']
        pwd = request.POST['password']
        next_password = request.POST['next_password']
        if len(pwd) < 6:
            return render(request, 'user/alter.html', {'mag': '密码必须大于6个字符'})
        elif len(pwd) > 18:
            return render(request, 'user/alter.html', {'mag': '密码必须小于18个字符'})
        elif pwd != next_password:
            return render(request, 'user/alter.html', {'mag': '输入密码不一致'})
        username = request.user.username
        user = authenticate(username=username, password=oldpwd)
        if user:
            if user.is_active:
                user.set_password(pwd)
                user.save()
                logout(request)
                return render(request, 'user/login.html')
        else:
            return render(request, 'user/alter.html', {"mag": '原始密码错误'})
