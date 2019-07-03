from django.db import models

# Create your models here.

class Bookinfo(models.Model):
    title=models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now=True)

class Heroinfo(models.Model):
    name=models.CharField(max_length=20)
    content=models.CharField(max_length=100)
    book=models.ForeignKey(Bookinfo,on_delete=models.CASCADE)



