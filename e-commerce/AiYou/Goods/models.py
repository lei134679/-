from django.db import models
from django.contrib.auth.models import User
from Store.models import Store


# 商品类型GoodsType
class GoodsType(models.Model):
    # 类型主键
    id = models.AutoField(primary_key=True, verbose_name='类型主键')
    # 类型名称
    gt_name = models.CharField(max_length=255, verbose_name='类型名称')
    # 图片
    cover = models.ImageField(upload_to='static/images/GoodsType/',null=True, blank=True,
                              verbose_name='图片')
    # 类型描述
    gt_desc = models.TextField(null=True, verbose_name='类型描述')
    # 父级类型：
    null = models.ForeignKey('self',null=True, on_delete=models.CASCADE, verbose_name='子类型')


# 商品信息Goods
class Goods(models.Model):
    # 商品编号
    id = models.AutoField(primary_key=True, verbose_name='商品编号')
    # 商品名称
    name = models.CharField(max_length=255, verbose_name='商品名称')
    # 商品单价
    price = models.IntegerField(verbose_name='商品单价')
    # 商品库存
    stock = models.IntegerField(verbose_name='商品库存')
    # 销售数量
    count = models.IntegerField(verbose_name='销售数量')
    # 上架时间
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上架时间')
    # 商品介绍
    desc = models.TextField(verbose_name='商品介绍')
    # 商品类型
    goods_detail_type = models.ForeignKey(GoodsType, on_delete=models.CASCADE,
                                          verbose_name='商品类型')
    # 所属店铺
    goods_store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='所属店铺')


# 商品图片GoodsImage
class GoodsImage(models.Model):
    # 图片编号
    id = models.AutoField(primary_key=True, verbose_name='图片编号')
    # 图片路径
    path = models.ImageField(upload_to='static/images/GoodsImage/',
                             null=True, blank=True, verbose_name='图片路径')
    # 默认展示
    status = models.BooleanField(default=True, verbose_name='默认展示')
    # 所属商品
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='所属商品')