from django.db import models

from django.contrib.auth.models import User


class Stores(models.Model):
	id = models.AutoField(primary_key=True)
	# 店铺名称
	name = models.CharField(max_length=255, unique=True, verbose_name="店铺名称")
	# 店铺封面
	cover = models.ImageField(upload_to="sataic/stores", default="sataic/stores/3.jpg", verbose_name="店铺封面")
	# 店铺描述
	intro = models.TextField(verbose_name="店铺描述")
	# 开店时间
	openTime = models.DateTimeField(auto_now_add=True, verbose_name="开店时间")
	#店铺状态
	status = models.IntegerField(default=0, verbose_name="店铺状态")
	#店主
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="店主")
