
from django.conf.urls import url
from . import views
from .views import AddArticleView,IndexView,SingleView,ContactView,FullView
app_name='blog'

#应用url配置
urlpatterns=[
    url(r"^$",IndexView.as_view(),name="index"),
    url(r"^full/$",FullView.as_view(),name='full'),
    url(r"^single/$",SingleView.as_view(),name='single'),
    url(r"^contact/$",ContactView.as_view(),name='contact'),
    url(r"^addarticle/$",AddArticleView.as_view(),name='addarticle'),
    url(r"^category/$",views.category,name='category'),
    url(r"^archives/$",views.archives,name='archives'),
    url(r"^article_list/$",views.article_list,name='article_list'),

]







