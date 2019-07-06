from django.db import models

# Create your models here.

class Bookinfo(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title


class HeroManage(models.Manager):

    def addhero(self, _name, _content, _gender, _book):
        hero = Heroinfo()
        hero.name = _name
        hero.content = _content
        hero.gender = _gender
        hero.book = _book
        hero.save()


class Heroinfo(models.Model):
    name=models.CharField(max_length=20)
    content=models.CharField(max_length=20)
    gender=models.CharField(max_length=5,choices=(('man','男'),('women','女')))
    book=models.ForeignKey(Bookinfo,on_delete=models.CASCADE)
    objects=HeroManage()


    def __str__(self):
        return self.name




