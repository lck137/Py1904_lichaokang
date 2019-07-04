
from django.conf.urls import url
from . import views

app_name="booktest"

#应用路由
urlpatterns=[
    url(r"^$",views.index,name='index'),
    url(r"^list/$",views.list,name='list'),
    url(r"^detail/(\d+)/$",views.detail,name='detail'),
    url(r"^delhero/(\d+)/$",views.delhero,name='delhero'),
]








