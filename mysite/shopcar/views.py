from django.shortcuts import render,reverse, redirect
from django.contrib.auth.decorators import login_required
# from goods import models
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.http import HttpResponse, JsonResponse
# from .models import ShopCart
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json


def gou_wu_che(request):
    if request.method == "GET":
        return render(request, 'shopcar/car_index.html')
    if request.method == "POST":
        # result = request.POST[""]
        pass
#
# @require_GET
# def add(request, count, g_id):
#     goods = models.Goods.objects.filter(pk=g_id).first()
#     allTotal = int(goods.price) * int(count)
#     shopcarts = ShopCart.objects.filter(user=request.user)
#     carts_count = len(shopcarts)
#     for shopcart1 in shopcarts:
#         if shopcart1.goods == goods:
#             shopcart1.allTotal += allTotal
#             shopcart1.count += int(count)
#
#             shopcart1.save()
#             break
#     else:
#         shopcart = ShopCart(goods=goods, count=count, allTotal=allTotal, user=request.user)
#         shopcart.save()
#         carts_count += 1
#     return HttpResponse("{}".format(carts_count))
#
#
# @login_required
# def shopCarts_list(request):
#     pageNow = int(request.GET.get("pageNow", 1))
#     shopcarts = ShopCart.objects.filter(user=request.user).order_by("-addTime")
#     # 每页显示的条数
#     pageSize = 4
#     # 获取分页对象
#     paginator = Paginator(shopcarts, pageSize)
#     # 获取分页对象的列表，参数是当前页码
#     page = paginator.page(pageNow)
#
#     # 总页数
#     num_pages = paginator.num_pages
#     # 进行页码控制
#     # 1.总页数<5, 显示所有页码
#     # 2.当前页是前3页，显示1-5页
#     # 3.当前页是后3页，显示后5页 10 9 8 7
#     # 4.其他情况，显示当前页前2页，后2页，当前页
#     if num_pages < 5:
#         pages = range(1, num_pages + 1)
#     elif pageNow <= 3:
#         pages = range(1, 6)
#     elif num_pages - pageNow <= 2:
#         pages = range(num_pages - 4, num_pages + 1)
#     else:
#         pages = range(pageNow - 2, pageNow + 3)
#
#     return render(request, "shopcart/list.html", {"page": page, "pageSize": pageSize, "pages": pages, "num_pages": num_pages})
#
#
# @csrf_exempt
# @require_POST
# @login_required
# def delete(request):
#     sc_id = request.POST.get("sc_id")
#     if sc_id:
#         shopcart = ShopCart.objects.get(pk=sc_id)
#         shopcart.delete()
#         return HttpResponse("删除购物车成功~")
#     else:
#         return HttpResponse("删除购物车失败~")

def add(request):
    if request.method == "GET":
        return render(request, "shopcar/add.html")
    elif request.method == "POST":
        names = request.POST["name"]
        count = request.POST["count"]
        price = request.POST["price"]
        all = int(count) * int(price)

        sel = request.POST["sel"]
        # kan1 = request.POST["kan1"]
        # kan11 = request.POST["kan11"]
        # kan22 = request.POST["kan22"]


        return render(request, "shopcar/add.html", {"name": names, "count": count, "price": all, "sel": sel})