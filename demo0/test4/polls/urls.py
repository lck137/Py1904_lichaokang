
from django.conf.urls import url
from . import views

app_name="polls"

#应用路由
urlpatterns=[
    url(r"^$",views.index,name="index"),
    url(r"^detail/(\d+)/$",views.detail,name="detail"),
    url(r"^result/(\d+)/$",views.result,name="result"),
    url(r"^plogin/$",views.plogin,name='plogin'),
    url(r"^ploginout/$",views.ploginout,name='ploginout'),
    url(r"^pregister/$",views.pregister,name='pregister'),

]




