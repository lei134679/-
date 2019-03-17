from django.shortcuts import render, redirect, reverse
from . import models
from Goods.models import GoodsType
# Create your views here.


def on_store(request):
    """
    注册店铺
    :param request:
    :return:
    """
    if request.method == 'GET':
        goodstype = GoodsType.objects.filter(null_id=None)
        return render(request, 'store/on_store.html', {'goodstype': goodstype})
    if request.method == 'POST':
        name = request.POST['name']

        intro = request.POST['intro'].strip()
        status = request.POST['status']
        print(name, intro, status)
        try:
            cover = request.FILES['cover']
            models.Store(name=name, intro=intro, status=status, cover=cover, users=request.user).save()
        except:
            models.Store(name=name, intro=intro, status=status, users=request.user).save()
        return redirect(reverse('store:my_store'))


def alt_store(request, id):
    if request.method == 'GET':
        store = models.Store.objects.get(pk=id)
        goodstype = GoodsType.objects.filter(null_id=None)
        return render(request, 'store/alt_store.html', {'store': store, 'goodstype': goodstype})
    if request.method == 'POST':
        name = request.POST['name']
        intro = request.POST['intro'].strip()
        status = request.POST['status']
        print(name, intro, status)
        store = models.Store.objects.get(pk=id)
        try:
            cover = request.FILES['cover']
            store.name, store.intro, store.status, store.cover = name, intro, status, cover
            store.save()
        except:
            store.name, store.intro, store.status = name, intro, status
            store.save()
        return redirect(reverse('store:my_store'))


# def store_goods(request):
#     """
#     店铺列表
#     :param request:
#     :return:
#     """
#     if request.method == 'GET':
#         stores = models.Store.objects.all()
#
#         return render(request, 'store/store_goods.html', {'stores':stores})


def on_off(request, id):
    """
    开店或关店
    :param request:
    :return:
    """
    store = models.Store.objects.get(pk=id)
    if store.status:
        store.status = "False"
    else:
        store.status = "True"
    store.save()
    return redirect(reverse('store:my_store'))


def details_store(request, id):
    """
    商店详情，此商店商品
    :param request:
    :param id:
    :return:
    """
    store = models.Store.objects.get(pk=id)
    return render(request, 'store/store_goods.html', {'store':store})


def del_store(request, id):
    """
    删除商店
    :param request:
    :param id:
    :return:
    """
    models.Store.objects.get(pk=id).delete()
    return redirect(reverse('store:my_store'))


def my_store(request):
    """
    我的店铺，店铺列表
    :param request:
    :return:
    """
    if request.method == 'GET':
        stores = models.Store.objects.all()
        goodstype = GoodsType.objects.filter(null_id=None)
        return render(request, 'store/my_store.html', {'stores':stores, 'goodstype': goodstype})