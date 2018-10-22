from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_GET # 请求
from django.core.serializers import serialize # 序列化
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required #登陆后才能使用，否则跳到登陆界面

from . import models
from stores.models import Stores
from goods.models import Goods


#商品增加
@login_required
def add(request, store_id):
	if request.method == "GET":
		type1 = models.GoodsType.objects.filter(goodType__isnull=True)
		return render(request, "goods/add.html", {"store_id": store_id, "type1": type1})
	else:
		name = request.POST["name"]
		price = request.POST["price"]
		stock = request.POST["stock"]
		store_id = request.POST["store"]
		type2 = request.POST["type2"]
		intro = request.POST["intro"]
		cover = request.FILES["cover"]

		store = Stores.objects.get(pk=store_id)
		goodsType = models.GoodsType.objects.get(pk=type2)

		# 数据验证

		goods = models.Goods(name=name, price=price, stock=stock, intro=intro, store=store, goodsType=goodsType)
		goods.save()

		goodImage = models.GoodsImage(path=cover, goods=goods)
		goodImage.save()

		return redirect(reverse("stores:detail", kwargs={"s_id": store.id}))


# 二级类型查询函数
@require_GET
def findType(request):
	goodType_id = request.GET["goodType_id"]
	type2 = models.GoodsType.objects.filter(goodType=goodType_id)
	return HttpResponse(serialize("json", type2))


# 商品详情界面
@login_required
def detail(request, g_id):
	goods = models.Goods.objects.get(pk=g_id)
	return render(request, "goods/detail.html", {"goods": goods})


#修改商品
@login_required
def update(request, g_id):
	pass


#删除商品
@login_required
def delete(request, g_id):
	pass