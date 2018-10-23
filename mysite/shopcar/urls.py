
from django.conf.urls import url

from . import views
#
urlpatterns = [
    url(r"^(?P<count>\d+)/(?P<goods_id>\d+)/add/$", views.add, name="add"),
    # url(r"^add/$", views.add, name="add"),
    url(r"^list/$", views.list, name="list"),
    # url(r"^delete/&", views.delete, name="delete"),
    url(r"^$", views.gou_wu_che, name="gou_wu_che")

]