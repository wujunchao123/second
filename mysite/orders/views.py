from django.shortcuts import render
from django.views.decorators.http import require_POST

from shopcar.models import ShopCart
from goods.models import Goods

@require_POST
def confirm(request):
	g_ids = request.POST.getlist("g_id")
	goods = ShopCart.goods.objects.filter(pk__in=g_ids)
	pass


def pay(reuqest):
	pass


def done(request):
	pass


def list(request):
	pass


def detail(request, o_id):
	pass
