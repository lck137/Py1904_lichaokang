
from django.conf.urls import url
from . import views
app_name='blog'

#应用url配置
urlpatterns=[
    url(r"^$", views.index, name="index"),
    url(r"full/",views.full,name='full'),
    url(r"^single/$",views.single,name='single'),
    url(r"^contact/$",views.contact,name='contact'),

]







