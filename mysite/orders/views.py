from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_POST

from shopcar.models import ShopCart
from goods.models import Goods
from . import models
# from user.models import Address

@require_POST
def confirm(request):
	g_ids = request.POST.getlist("g_id")
	shop_carts = ShopCart.objects.filter(pk__in=g_ids)
	# addresses = Address.objects.filter(user=request.user)
	return render(request, "oeders/confirm.html", {"shop_carts":shop_carts})#, "addresses":addresses})


def pay(reuqest):
	pass


@require_POST
def done(request):
	c_ids = request.POST.getlist("c_id")
	address_id = request.POST["address"]

	# address = Address.objects.get(pk=address_id)
	shopcarts = ShopCart.objects.filter(pk__in=c_ids)

	_address = address.recv_name + "|" + address.recv_tel + "|" + address.province + "|" + \
			   address.city + "|" + address.area + "|" + address.street + "|" + address.desc

	# 生成订单
	order = models.Order(address=address, user=request.user, recv_name=address.recv_name, recv_tel=address.recv_tel, \
						  all_price=0, remake="")

	order.save()
	allCount = 0
	for s in shopcarts:
		g = s.goods
		orderItem = models.OrderItem(goods_id=g.id, goods_img=g.goodsimage_set.all.firet.path,\
						goods_name=g.anme, goods_price=g.price, goods_count=s.count, \
						 goods_price_all=s.allTital)

		orderItem.save()
		allCount += s.allTotal
	order.all_price = allCount
	order.save()

	return redirect(reverse("orders:list"))


def list(request):
	orders = models.Order.objects.filter(user=request.user)
	return render(request, "orders/list.html", {"orders":orders})


def detail(request, o_id):
	pass
