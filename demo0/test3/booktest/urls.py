

from django.conf.urls import url
from . import views
#应用名
app_name="booktest"


urlpatterns=[
    url(r"^$",views.index,name="index"),
    url(r"^list/$",views.list,name="list"),
    url(r"^detail/(\d+)/$",views.detail,name="detail"),
    url(r"^delhero/(\d+)/$",views.delhero,name="delhero"),
    url(r"^delbook/(\d+)/$",views.delbook,name='delbook'),
    url(r"^addbook/$",views.addbook,name='addbook'),
    url(r"^addhero/(\d+)/$",views.addhero,name='addhero'),

]










