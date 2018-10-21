from django.conf.urls import url

from . import views


urlpatterns = [
	url(r"^add/$", views.add, name="add"),
	url(r"^findType/$", views.findType, name="findType"),
]