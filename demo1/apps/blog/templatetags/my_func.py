'''
自定义模板表达式
扩展Django原有功能

'''

from django.template import library
register=library.Library()
from blog.models import Article,Category,Tag

#最新文章
@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.order_by('-create_time')[:num]

#分类
@register.simple_tag
def getlatestcategorys(num=3):
    return Category.objects.all()[:num]

#归档
@register.simple_tag
def getarchives():
    return Article.objects.dates('create_time','month',order="DESC")

#标签云
@register.simple_tag
def gettags():
    return Tag.objects.all()







