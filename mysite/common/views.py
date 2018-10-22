from django.shortcuts import render

from goods.models import GoodsType, Goods


def index(request):
	# # 第一个一级数据类型展示
	# good_type1 = GoodsType.objects.filter(pk=10001)
	# good_type1_2 = GoodsType.objects.filter(goodType=good_type1)
	# goods1_list = Goods.objects.filter(goodstype__in=good_type1_2)
	#
	# return render(request, "common/index.html", {"goods1_list": goods1_list})

    return render(request, "common/index.html")
