from django.db import models

# Create your models here.

class Question(models.Model):
    title=models.CharField(max_length=10)

class Choice(models.Model):
    option=models.CharField(max_length=10)
    num=models.IntegerField(default=0)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)


