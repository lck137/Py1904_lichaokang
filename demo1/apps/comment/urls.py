from django.conf.urls import url
from . import views
from comment.models import Comment

app_name='comment'

urlpatterns=[
    url(r"^comment/(\d+)/$",views.AddComment.as_view(),name='comment'),
]

