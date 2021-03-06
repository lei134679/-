# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-03-14 06:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品编号')),
                ('name', models.CharField(max_length=255, verbose_name='商品名称')),
                ('price', models.IntegerField(verbose_name='商品单价')),
                ('stock', models.IntegerField(verbose_name='商品库存')),
                ('count', models.IntegerField(verbose_name='销售数量')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='上架时间')),
                ('desc', models.TextField(verbose_name='商品介绍')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='图片编号')),
                ('path', models.ImageField(blank=True, null=True, upload_to='static/images/GoodsImage/', verbose_name='图片路径')),
                ('status', models.BooleanField(default=True, verbose_name='默认展示')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.Goods', verbose_name='所属商品')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='类型主键')),
                ('gt_name', models.CharField(max_length=255, verbose_name='类型名称')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='static/images/GoodsType/', verbose_name='图片')),
                ('gt_desc', models.TextField(verbose_name='类型描述')),
                ('null', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Goods.GoodsType', verbose_name='子类型')),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_detail_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.GoodsType', verbose_name='商品类型'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.Store', verbose_name='所属店铺'),
        ),
    ]
