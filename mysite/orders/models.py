from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
	id = models.AutoField(primary_key=True)
	# 订单所属用户
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="所属用户")
	# 订单生成时间
	create_time = models.DateTimeField(auto_now_add=True, verbose_name="订单生成时间")
	# 收件人
	recv_name = models.CharField(max_length=100, verbose_name="收件人")
	# 收件人联系方式
	recv_tel = models.CharField(max_length=50, verbose_name="收件人电话")
	# 售货地址
	recv_address = models.CharField(max_length=255, verbose_name="收货地址")
	# 订单总金额
	all_price = models.FloatField(verbose_name="订单总金额")
	# 订单备注
	remake = models.CharField(max_length=255, verbose_name="备注信息")


class OrderItem(models.Model):
	id = models.AutoField(primary_key=True)
	# 商品编号
	goods_id = models.IntegerField(verbose_name="商品编号")
	# 商品图片
	goods_img = models.CharField(max_length=255, verbose_name="商品图片")
	# 商品名称
	goods_name = models.CharField(max_length=255, verbose_name="商品名称")
	# 商品价格
	goods_price = models.FloatField(verbose_name="商品价格")
	# 购买数量
	goods_count = models.IntegerField(verbose_name="商品数量")
	# 商品总价
	goods_price_all = models.FloatField(verbose_name="成交价格")
	# 所属订单
	order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="所属订单")