# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='商品名称')),
                ('price', models.FloatField(verbose_name='商品单价')),
                ('stock', models.IntegerField(verbose_name='剩余库存')),
                ('count', models.IntegerField(default=0, verbose_name='销量')),
                ('creatTime', models.DateTimeField(auto_now_add=True)),
                ('intro', models.TextField(verbose_name='商品描述')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.ImageField(default='static/goods/2.jpg', upload_to='static/goods', verbose_name='商品图片')),
                ('intro', models.TextField(blank=True, null=True, verbose_name='商品图片描述')),
                ('status', models.BooleanField(default=False, verbose_name='默认显示的图片')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='所属商品')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='商品类名称')),
                ('cover', models.ImageField(default='static/goods/1.jpg', upload_to='static/goods', verbose_name='商品类图片')),
                ('intro', models.TextField(verbose_name='商品类描述')),
                ('goodType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsType', verbose_name='父级类型')),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='goodsType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsType', verbose_name='商品所属类型'),
        ),
        migrations.AddField(
            model_name='goods',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Stores', verbose_name='商品所属店铺'),
        ),
    ]