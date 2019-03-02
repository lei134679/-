from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
# 验证码
from django.http import HttpResponse
from io import BytesIO
from . import models
from . import utils

# Create your views here.
from . import models

"""
***********************************用户处理***************************************
"""


def index(request):
    """
    首页
    :param request:
    :return:
    """
    if request.method == 'GET':
        # try:
        #     article = models.Article.objects.all().exclude(user_id=request.user.id)
        #     print(article)
        #     return render(request, 'user/index.html', {"article":article})
        # except:
        #     pass
        article = models.Article.objects.all().order_by("-id")
        return render(request, 'user/index.html', {"article": article})


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
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        cmbProvince = request.POST['cmbProvince']
        cmbCity = request.POST['cmbCity']
        cmbArea = request.POST['cmbArea']
        addr = request.POST['addr']
        addrs = '%s-%s-%s-%s'%(cmbProvince,cmbCity,cmbArea,addr)
        # 数据库查找
        t_user = models.User.objects.filter(username=username)
        # 数据校准
        if gender not in ['男', '女']:
            return render(request, 'user/register.html', {'mag': '性别输入有误'})
        elif username == '':
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
                user = models.User.objects.create_user(username=username, password=password)
                user.save()
                try:
                    image = request.FILES['image']
                    models.Users(age=age, gender=gender, phone=phone, addr=addrs,img=image, user=user).save()
                    return render(request, 'user/login.html')
                except:
                    models.Users(age=age, gender=gender, phone=phone, addr=addrs, user=user).save()
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
    if request.method == 'GET':
        try:
            next = request.GET['next']
            return render(request, 'user/login.html', {'next': next})
        except:
            return render(request, 'user/login.html')
    if request.method == 'POST':
        # 获得页面信息
        username = request.POST['username']
        password = request.POST['password']
        yzm = request.POST['yzm']
        user = authenticate(username=username, password=password)
        if yzm != request.session.get("check_code"):
            return render(request, 'user/login.html', {'mag': '验证码错误'})
        if user:
            login(request, user)
            try:
                next = request.POST['next']
                return redirect(next)
            except:
                return redirect('/user/index/')
        else:
            return render(request, 'user/login.html', {'mag': '用户名或密码错误'})


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
        return render(request, 'user/alter_password.html')
    if request.method == 'POST':
        oldpwd = request.POST['oldpassword']
        pwd = request.POST['password']
        next_password = request.POST['next_password']
        if len(pwd) < 6:
            return render(request, 'user/alter_password.html', {'mag': '密码必须大于6个字符'})
        elif len(pwd) > 18:
            return render(request, 'user/alter_password.html', {'mag': '密码必须小于18个字符'})
        elif pwd != next_password:
            return render(request, 'user/alter_password.html', {'mag': '输入密码不一致'})
        username = request.user.username
        user = authenticate(username=username, password=oldpwd)
        if user:
            if user.is_active:
                user.set_password(pwd)
                user.save()
                logout(request)
                return render(request, 'user/login.html')
        else:
            return render(request, 'user/alter_password.html', {"mag": '原始密码错误'})


@login_required
def data(request, id):
    """
    修改资料
    :param request:
    :return:
    """
    if request.method == 'GET':
        users = models.Users.objects.filter(user_id=request.user.id)[0]
        addr = users.addr.split('-')
        return render(request, 'user/alter_data.html', {'users':users, 'addr':addr})
    if request.method == 'POST':
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        cmbProvince = request.POST['cmbProvince']
        cmbCity = request.POST['cmbCity']
        cmbArea = request.POST['cmbArea']
        addr = request.POST['addr']
        addrs = '%s-%s-%s-%s' % (cmbProvince, cmbCity, cmbArea, addr)
        if gender not in ['男', '女']:
            return render(request, 'user/alter_data.html', {'mag': '性别输入有误'})
        else:
            # print(age, gender, phone, addrs)
            try:
                image = request.FILES['image']
                models.Users.objects.filter(pk=id).update(age=age, gender=gender, phone=phone, addr=addrs,img=image, user=request.user)
                return render(request, 'user/details.html')
            except:
                models.Users.objects.filter(pk=id).update(age=age, gender=gender, phone=phone, addr=addrs, user=request.user)
                return render(request, 'user/details.html')


# 验证码
def create_code_img(request):
    # 在内存中开辟空间用以生成临时的图片
    f = BytesIO()
    img, code = utils.create_code()
    # 保存验证码信息到 session 中，方便下次表单提交时进行验证操作
    request.session['check_code'] = code
    img.save(f, 'PNG')
    return HttpResponse(f.getvalue())


"""
***********************************文章处理***************************************
"""


@login_required
def add_article(request):
    """
    发表文章
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'article/add.html')
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        print(title, content)
        if len(title) == 0:
            return render(request, 'article/add.html', {'mag': '标题不能为空'})
        elif len(content) < 5:
            return render(request, 'article/add.html', {'mag': '内容必须大于5个字符'})
        else:
            try:
                user_id = request.user.id
                models.Article(title=title, content=content, user_id=user_id).save()
                return render(request, 'article/success.html')
            except Exception as e:
                print(e)
                return render(request, 'article/add.html', {'mag': '输入有误，请重新输入'})


@login_required
def success_article(request):
    """
    发表成功
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'article/success.html')


@login_required
def list_article(request):
    """
    文章列表页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        user_article = request.user.article_set.all()
        return render(request, 'article/list.html', {'all': user_article})


def detalis_article(request, id):
    """
    文章详情页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        article = models.Article.objects.filter(pk=id)[0]
        try:
            u_id = request.user.id
            return render(request, 'article/details.html', {"article": article, 'u_id': u_id})
        except:
            u_id = -1
            return render(request, 'article/details.html', {"article": article, 'u_id': u_id})


@login_required
def del_article(request, id):
    """
    删除文章
    :param request:
    :param id:
    :return:
    """
    if request.method == 'GET':
        models.Article.objects.filter(pk=id).delete()
        return redirect('/user/list_article/')


@login_required
def update_article(request, id):
    """
    修改文章
    :param request:
    :param id:
    :return:
    """
    if request.method == 'GET':
        article = models.Article.objects.filter(pk=id)[0]
        return render(request, 'article/update.html', {'article': article})
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        print(title, content)
        if len(title) == 0:
            return render(request, 'article/add.html', {'mag': '标题不能为空'})
        elif len(content) < 5:
            return render(request, 'article/add.html', {'mag': '内容必须大于5个字符'})
        else:
            try:
                models.Article.objects.filter(pk=id).update(title=title, content=content, last_time=datetime.now())
                return redirect('/user/%s/detalis_article/' % id)
            except Exception as e:
                print(e)
                return redirect('/user/%s/update_article/' % id)
