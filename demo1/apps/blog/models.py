from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField

# Create your models here.

#图片
class Ads(models.Model):
    img=models.ImageField(upload_to='ads')
    desc=models.CharField(max_length=20)
    index=models.IntegerField(default=0)

    def __str__(self):
        return self.desc

#类别
class Category(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title

#标签
class Tag(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title

#文章
class Article(models.Model):
    title = models.CharField(max_length=20)
    category=models.ForeignKey(Category,models.CASCADE)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    votes=models.IntegerField(default=0)
    body=UEditorField(imagePath='articleimg/',width='100%')
    # body=models.TextField()
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.title





