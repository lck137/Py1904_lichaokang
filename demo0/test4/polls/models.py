from django.db import models

# Create your models here.

class Question(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Choice(models.Model):
    option=models.CharField(max_length=20)
    num=models.IntegerField(default=0)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.option





