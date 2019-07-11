
from django.conf.urls import url
from .feeds import ArticleFeed
from . import views
from .views import AddArticleView,IndexView,SingleView,ContactView,FullView
app_name='blog'

#应用url配置
urlpatterns=[
    url(r"^$",IndexView.as_view(),name="index"),
    url(r"^full/$",FullView.as_view(),name='full'),
    url(r"^single/(\d+)/$",SingleView.as_view(),name='single'),
    url(r"^contact/$",ContactView.as_view(),name='contact'),
    url(r"^addarticle/$",AddArticleView.as_view(),name='addarticle'),
    url(r"^category/(\d+)/$",views.CategoryView.as_view(),name='category'),
    url(r"^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$",views.ArchivesView.as_view(),name='archives'),
    url(r"^tag/(\d+)/$",views.TagesView.as_view(),name='tag'),
    url(r"^rss/$",ArticleFeed()),
]







