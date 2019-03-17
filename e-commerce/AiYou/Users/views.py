from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from . import models
from Goods.models import GoodsType
from Goods.models import Goods
# 验证码
from io import BytesIO
from . import models
from . import utils


# ==========================================用户模块=================================================
def index(request):
    goodstype = GoodsType.objects.filter(null_id =None)
    goods = Goods.objects.all()
    return render(request, 'users/index.html', {'goods':goods ,'goodstype':goodstype})


def sjzx(request):
    """
    平台政策
    :param request:
    :return:
    """
    return render(request, 'users/sjzx.html')


def u_register(request):
    """
    用户注册
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'users/u_register.html')
    if request.method == 'POST':
        # 获得页面信息
        username = request.POST.get('username')  # 登录账号
        userpass = request.POST.get('password')  # 登录密码
        mickname = request.POST.get('mickname')  # 用户昵称
    try:
        # 保存数据库
        auth_user = models.User.objects.create_user(username=username, password=userpass)
        auth_user.save()
        # 保存数据库
        user = models.Users(mickname=mickname, user=auth_user)
        user.save()
        return redirect(reverse('users:u_login'))
    except:
        return render(request, 'users/u_register.html', {'mag': '输入信息有误，请重新输入'})


def ajax_reg(request):
    """
    判断注册信息是否有效
    :param request:
    :return:
    """
    # 获得页面信息
    username = request.GET.get('username', 0)  # 登录账号
    mickname = request.GET.get('mickname', 0)  # 用户昵称
    # 判断账号
    if username:
        user = models.User.objects.filter(username=username)
        if len(username) < 6 or len(username) > 18:
            return JsonResponse({'username': '账号6-18位'})
        elif len(user) > 0:
            return JsonResponse({'username': '用户已存在'})
    # 判断昵称
    elif mickname:
        user = models.Users.objects.filter(mickname=mickname)
        if len(user) > 0:
            return JsonResponse({'mickname': '昵称已存在'})
    return JsonResponse({})


def u_login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        next = request.GET.get('next', '/users/index/')
        request.session['next'] = next
        return render(request, 'users/u_login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        yzm = request.POST.get('yzm')
        print(username, password, yzm)
        if yzm != request.session['check_code']:
            return render(request, 'users/u_login.html', {'mag': '验证码不一致'})
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.session.get('next'))
        else:
            return render(request, 'users/u_login.html', {'mag': '账号或密码错误'})


def create_code_img(request):
    # 在内存中开辟空间用以生成临时的图片
    f = BytesIO()
    img, code = utils.create_code()
    # 保存验证码信息到 session 中，方便下次表单提交时进行验证操作
    request.session['check_code'] = code
    img.save(f, 'PNG')
    return HttpResponse(f.getvalue())


@login_required
def u_logout(request):
    """
    退出登录
    :param request:
    :return:
    """
    logout(request)
    return redirect(reverse('users:u_login'))


@login_required
def u_message(request):
    """
    显示个人资料，完善个人资料
    :param request:
    :return:
    """
    if request.method == 'GET':
        goodstype = GoodsType.objects.filter(null_id=None)
        return render(request, 'users/Profile.html', {'goodstype':goodstype})
    if request.method == 'POST':
        mickname = request.POST['mickname']
        age = request.POST['age']
        phone = request.POST['phone']
        email = request.POST['email']
        gender = request.POST['gender']
        # print(mickname,age,phone,email,gender,header)
        models.User.objects.filter(pk=request.user.id).update(email=email)
        user = request.user.users
        try:
            header = request.FILES['header']
            user.mickname, user.age, user.phone, user.gender, user.header = mickname, age, phone, gender, header
            user.save()
        except:
            user.mickname, user.age, user.phone, user.gender = mickname, age, phone, gender
            user.save()
        return redirect(reverse('users:u_message'))


@login_required
def alt_pwd(request):
    """
    修改密码
    :param request:
    :return:
    """
    if request.method == 'GET':
        goodstype = GoodsType.objects.filter(null_id=None)
        return render(request, 'users/alt_pwd.html', {'goodstype': goodstype})
    if request.method == 'POST':
        old_pwd = request.POST['old_pwd']
        new_pwd = request.POST['new_pwd']
        new_pwd2 = request.POST['new_pwd2']
        # print(old_pwd, new_pwd, new_pwd2)
        if new_pwd != new_pwd2:
            # return redirect(reverse('users:alt_pwd'), {'mag':'输入的密码不一致'})
            return render(request, 'users/alt_pwd.html', {'mag': '输入的密码不一致'})
        else:
            user = authenticate(username=request.user.username, password=old_pwd)
            if user:
                user.set_password(new_pwd)
                user.save()
                logout(request)
                return redirect(reverse('users:u_login'))
            else:
                return render(request, 'users/alt_pwd.html', {"mag": '原始密码错误'})


# ==========================================地址模块=================================================
@login_required
def address(request):
    """
    添加地址
    :param request:
    :return:
    """
    if request.method == 'GET':
        address = models.Address.objects.all()
        goodstype = GoodsType.objects.filter(null_id=None)
        return render(request, 'addr/addr.html', {'address': address, 'goodstype': goodstype})
    if request.method == 'POST':
        recv_name = request.POST['username']
        recv_phone = request.POST['phone']
        cmbProvince = request.POST['cmbProvince']
        cmbCity = request.POST['cmbCity']
        cmbArea = request.POST['cmbArea']
        address = request.POST['address']
        if recv_name == '' or recv_phone == '' or address == '':
            return render(request, 'addr/addr.html', {'mag': '请完善信息！'})
        # print(recv_name, recv_phone, cmbProvince, cmbCity, cmbArea, address, default)
        _id = request.user
        try:
            default = request.POST['default']
            models.Address.objects.all().update(status=False)
            models.Address(recv_name=recv_name, recv_phone=recv_phone, province=cmbProvince, city=cmbCity,
                           country=cmbArea, desc=address, status=default, users=_id).save()
        except:
            models.Address(recv_name=recv_name, recv_phone=recv_phone, province=cmbProvince, city=cmbCity,
                           country=cmbArea, desc=address, status="False", users=_id).save()
        return redirect(reverse('users:address'))


@login_required
def del_addr(request):
    """
    删除地址
    :param request:
    :return:
    """
    id = request.GET['id']
    models.Address.objects.filter(pk=id)[0].delete()
    return redirect(reverse('users:address'))
