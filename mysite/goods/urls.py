from django.conf.urls import url

from . import views


urlpatterns = [
	url(r"^(?P<store_id>\d+)/add/$", views.add, name="add"),
	url(r"^(?P<g_id>\d+)/detail/$", views.detail, name="detail"),
	url(r"^findType/$", views.findType, name="findType"),
]