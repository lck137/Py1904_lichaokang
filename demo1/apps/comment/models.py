from django.db import models
from blog.models import Article

# Create your models here.

#评论
class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    url = models.URLField(blank=True, null=True, default='http://www.baidu.com')
    content = models.TextField()
    create_time=models.DateTimeField(auto_now_add=True)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)