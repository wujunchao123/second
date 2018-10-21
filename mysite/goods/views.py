from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_GET # 请求
from django.core.serializers import serialize # 序列化
from django.http import HttpResponse

from . import models
from stores.models import Stores


#商品增加
def add(request):
	if request.method == "GET":
		return render(request, "goods/add.html", {})
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

