from django.db import models

# 导入店铺
from stores.models import Stores


# 商品类型模块
class GoodsType(models.Model):
	id = models.AutoField(primary_key=True)
	# 商品类型名称
	name = models.CharField(max_length=255, unique=True, verbose_name="商品类名称")
	# 商品类型图片
	cover = models.ImageField(upload_to="static/goods", default="static/goods/1.jpg", verbose_name="商品类图片")
	# 商品类型描述
	intro= models.TextField(verbose_name="商品类描述")
	# 商品类型关联
	goodType = models.ForeignKey("self", null=True, blank=True, verbose_name="父级类型", on_delete=models.CASCADE)


# 商品类型
class Goods(models.Model):
	id = models.AutoField(primary_key=True)
	# 商品名称
	name = models.CharField(max_length=255, verbose_name="商品名称")
	# 商品价格
	price = models.FloatField(verbose_name="商品单价")
	# 剩余库存
	stock = models.IntegerField(verbose_name="剩余库存")
	# 销量
	count = models.IntegerField(default=0, verbose_name="销量")
	# 上架时间
	creatTime = models.DateTimeField(auto_now_add=True)
	# 商品描述
	intro = models.TextField(verbose_name="商品描述")
	# 所属店铺
	store = models.ForeignKey(Stores, on_delete=models.CASCADE, verbose_name="商品所属店铺")
	# 所属类型
	goodsType = models.ForeignKey(GoodsType, on_delete=models.CASCADE, verbose_name="商品所属类型")


# 商品图片的模块
class GoodsImage(models.Model):
	id = models.AutoField(primary_key=True)
	# 商品图片存放路径
	path = models.ImageField(upload_to="static/goods", default="static/goods/2.jpg", verbose_name="商品图片")
	# 图片描述
	intro = models.TextField(null=True, blank=True, verbose_name="商品图片描述")
	# 默认显示的图片
	status = models.BooleanField(default=False, verbose_name="默认显示的图片")
	# 所属商品
	goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="所属商品")
