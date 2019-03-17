from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from . models import GoodsType
from . import models


def add_goods(request, store_id):
    """
    添加商品
    :param request:
    :param store_id:
    :return:
    """
    if request.method == 'GET':
        goodstype = models.GoodsType.objects.filter(null_id=None)
        return render(request, 'goods/add_goods.html', {'store_id': store_id, 'goodstype': goodstype})
    if request.method == 'POST':
        # 获取页面信息
        name = request.POST['name']
        price = request.POST['price']
        stock = request.POST['stock']
        count = request.POST['count']
        desc = request.POST['desc'].strip()
        try:
            # 获取商品类型
            type2 = request.POST['type2']
            # 获得添加图片总数
            num = int(request.POST['num'])
            if num == 1:
                # 一张图片的商品添加
                # 获得每张图片
                print('1'*50)
                try:
                    image = request.FILES['img1']
                    print('2' * 50)
                    # 商品保存数据库
                    goods = models.Goods(name=name, price=price, stock=stock, count=count, desc=desc,
                                         goods_detail_type_id=type2, goods_store_id=store_id)
                    goods.save()
                    # 图片保存数据库
                    models.GoodsImage(path=image, goods=goods).save()
                    # 添加成功，返回添加商品页面
                    goodstype = models.GoodsType.objects.filter(null_id=None)
                    return render(request, 'goods/add_goods.html',
                                  {'store_id': store_id, 'goodstype': goodstype, 'success': '商品添加成功, 继续添加'})

                except:
                    # 一张图片都没选，返回重新选择
                    goodstype = models.GoodsType.objects.filter(null_id=None)
                    return render(request, 'goods/add_goods.html',
                                  {'store_id': store_id, 'goodstype': goodstype, 'mag': '请选择商品图片'})
            else:
                # 多张图片的商品添加
                # 商品保存数据库
                goods = models.Goods(name=name, price=price, stock=stock, count=count, desc=desc,
                                     goods_detail_type_id=type2, goods_store_id=store_id)
                goods.save()
                for i in range(1,num+1):
                    img = 'img'+str(i)
                    try:
                        # 获得每张图片
                        image = request.FILES[img]
                        # 获得默认
                        default = request.POST['default']
                        # 判断是否默认
                        if default == img:
                            # 默认图片保存数据库
                            models.GoodsImage(path=image, status='1', goods=goods).save()
                        else:
                            #  不是默认的图片保存数据库
                            models.GoodsImage(path=image, status='0', goods=goods).save()
                    except:
                        # 添加成功，返回添加商品页面
                        goodstype = models.GoodsType.objects.filter(null_id=None)
                        return render(request, 'goods/add_goods.html',
                                      {'store_id': store_id, 'goodstype': goodstype, 'success': '商品添加成功, 继续添加'})

                # 添加成功，返回添加商品页面
                goodstype = models.GoodsType.objects.filter(null_id=None)
                return render(request, 'goods/add_goods.html',
                              {'store_id': store_id, 'goodstype': goodstype, 'success': '商品添加成功, 继续添加'})

        except:
            # 类型未选择，重新选择
            goodstype = models.GoodsType.objects.filter(null_id=None)
            return render(request, 'goods/add_goods.html', {'store_id': store_id, 'goodstype': goodstype, 'mag':'请选择商品类型'})




def ajax_type(request):
    """
    查找一级类型，返回所有二级类型
    :param request:
    :return:
    """
    type_id = request.GET.get('type_id')
    goodstype = models.GoodsType.objects.filter(null=type_id)
    # print(goodstype)
    type2 = serialize("json", goodstype)
    # print(type2)
    return HttpResponse(type2)


def look_goods(request, store_id):
    """
    查看此商店商品
    :param request:
    :param store_id:
    :return:
    """
    if request.method == 'GET':
        store = models.Store.objects.get(pk=store_id)
        goods = store.goods_set.all()
        goodstype = GoodsType.objects.filter(null_id=None)
        return render(request, 'goods/look_goods.html', {'store': store, 'goods':goods, 'goodstype': goodstype})


def del_goods(request, goods_id, store_id):
    """
    删除商品
    :param request:
    :param goods_id:
    :param store_id:
    :return:
    """
    models.Goods.objects.get(pk=goods_id).delete()
    return redirect(reverse('goods:look_goods', args=store_id))


def alt_goods(request, goods_id, store_id):
    if request.method == 'GET':
        goods = models.Goods.objects.get(pk=goods_id)
        goodstype = models.GoodsType.objects.filter(null_id=None)
        return render(request, 'goods/alt_goods.html', {'goods':goods, 'goodstype':goodstype, 'goods_id':goods_id, 'store_id':store_id})
    if request.method == 'POST':
        # 获取页面信息
        name = request.POST['name']
        price = request.POST['price']
        stock = request.POST['stock']
        count = request.POST['count']
        desc = request.POST['desc'].strip()
        try:
            type2 = request.POST['type2']
            # 更新商品信息
            models.Goods.objects.filter(pk=goods_id).update(name=name, price=price, stock=stock, count=count, desc=desc, goods_detail_type_id=type2)
        except:
            # 更新商品信息
            models.Goods.objects.filter(pk=goods_id).update(name=name, price=price, stock=stock, count=count, desc=desc)
        # 查新出商品相关图片
        images = models.GoodsImage.objects.filter(goods_id=goods_id)
        # 获得需要删除的照片id
        for i in images:
            img = request.POST.get('img'+str(i.id), None)
            if img:
                # 判断默认图片不删除
                if i.status:
                    pass
                else:
                    models.GoodsImage.objects.get(pk=img).delete()
        # 跟新默认图片
        default = request.POST['default']
        try:
            def_img = models.GoodsImage.objects.get(pk=default)
            if def_img.status:
                pass
            else:
                images.update(status='0')
                def_img.status = '1'
                def_img.save()
        except:
            pass
        # 保存新增的图片
        # 获得添加图片总数
        num = int(request.POST['num'])
        if num == 1:
            # 一张图片的商品添加
            # 获得每张图片
            print('1' * 50)
            try:
                image = request.FILES['img1']
                print('2' * 50)
                # 获得默认
                default = request.POST['default']
                # 判断是否默认
                if default == 'img1':
                    # 默认图片保存数据库
                    images.update(status='0')
                    models.GoodsImage(path=image, status='1', goods_id=goods_id).save()
                else:
                    #  不是默认的图片保存数据库
                    models.GoodsImage(path=image, status='0', goods_id=goods_id).save()
                return redirect(reverse('goods:look_goods', args=store_id))
            except:
                return redirect(reverse('goods:look_goods', args=store_id))
        else:
            # 多张图片的商品添加
            for i in range(1, num + 1):
                img = 'img' + str(i)
                try:
                    # 获得每张图片
                    image = request.FILES[img]
                    # 获得默认
                    default = request.POST['default']
                    # 判断是否默认
                    if default == img:
                        # 默认图片保存数据库
                        images.update(status='0')
                        models.GoodsImage(path=image, status='1', goods_id=goods_id).save()
                    else:
                        #  不是默认的图片保存数据库
                        models.GoodsImage(path=image, status='0', goods_id=goods_id).save()
                    return redirect(reverse('goods:look_goods', args=store_id))
                except:
                    return redirect(reverse('goods:look_goods', args=store_id))


def details_goods(request, goods_id):
    """
    商品购买详情
    :param request:
    :param goods_id:
    :return:
    """
    goods = models.Goods.objects.get(pk=goods_id)
    goodstype = GoodsType.objects.filter(null_id=None)
    return render(request, 'goods/details_goods.html', {'goods':goods, 'goodstype':goodstype})