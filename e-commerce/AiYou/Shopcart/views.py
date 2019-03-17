from django.shortcuts import render
from django.http import JsonResponse
from Goods.models import Goods
from . import models


def add_shopcart(request):
    """
    ajax添加购物车
    :param request:
    :return:
    """
    goods_id = request.GET['goods_id']
    price = Goods.objects.get(pk=goods_id).price
    num = request.GET['num']
    subtotal = int(price)*int(num)
    # 判断购物车里是否有此商品
    shopcart = models.Shopcart.objects.filter(goods_id=goods_id)
    if len(shopcart) > 0:
        num = int(shopcart[0].count)+int(num)
        subtotal = int(shopcart[0].subtotal)+subtotal
        shopcart[0].count, shopcart[0].subtotal = num, subtotal
        shopcart[0].save()
    else:
        models.Shopcart(count=num, subtotal=subtotal, goods_id=goods_id, users=request.user).save()
    return JsonResponse({"a":'添加成功!'})


def shopcars(request):
    """
    购物车类列表
    :param request:
    :return:
    """
    if request.method == 'GET':
        stopcars = models.Shopcart.objects.filter(users=request.user)
        # 购物车总价格
        resault = 0
        for i in stopcars:
            resault += int(i.subtotal)
        return render(request, 'shopcart/shopcars.html', {'stopcars':stopcars, 'resault':resault})