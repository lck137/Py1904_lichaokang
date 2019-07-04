from django.db import models

#MVT 中的M 数据模块
#ORM对象
# Create your models here.


class Bookinfo(models.Model):
    title=models.CharField(max_length=20)
    pub_time=models.DateTimeField(auto_now=True)

class Heroinfo(models.Model):
    name=models.CharField(max_length=20)
    # gender=models.BooleanField(default=True)
    gender=models.CharField(max_length=5,choices=(('man','男'),('women','女')))
    content=models.CharField(max_length=100)
    book=models.ForeignKey(Bookinfo,on_delete=models.CASCADE)



