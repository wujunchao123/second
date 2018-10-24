from django.shortcuts import render,reverse, redirect
from django.contrib.auth.decorators import login_required
from goods.models import Goods
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.http import HttpResponse, JsonResponse
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json


def gou_wu_che(request):
    if request.method == "GET":
        return render(request, 'shopcar/car_index.html')
    if request.method == "POST":
        # result = request.POST[""]
        pass


@require_GET
@login_required
def add(request, count, goods_id):
	goods = Goods.objects.get(pk=goods_id)
	user = request.user

	try:
		shopCart = models.ShopCart.objects.get(user=user, goods=goods)
		shopCart.count += int(count)
		shopCart.allTotal = shopCart.count * goods.price
		shopCart.save()



	except:
		shopCart = models.ShopCart(goods=goods, user=user)
		shopCart.count = int(count)
		shopCart.allTotal = shopCart.count * goods.price
		shopCart.save()

	print('here is done!')
	json = JsonResponse({'msg':'success'})
	# json.status_code=200
	return  json
	# return redirect(reverse("shopcar:list"))


def list(request):
	# shopcarts = models.ShopCart.filter(user=request.use.order_by("-addTime"))
	shopcarts = models.ShopCart.objects.filter(user=request.user)
	return render(request, "shopcar/list.html", {"shopcarts": shopcarts})

