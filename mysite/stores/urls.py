from django.conf.urls import url

from . import views


urlpatterns = [
	# 增加店铺
	url(r"^add/$", views.add, name="add"),
	# 查询店铺
	url(r"^list/$", views.list, name="list"),
	# 修改店铺
	url(r"^(?P<s_id>\d+)/update/$", views.update, name="update"),
	# 店铺详情
	url(r"^(?P<s_id>\d+)/detail/$", views.detail, name="detail"),
	# 关闭店铺
	url(r"^(?P<s_id>\d+)/(?P<status>\d+)/change/$", views.change, name="change"),
]