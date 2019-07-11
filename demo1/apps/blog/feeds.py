
from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse

class ArticleFeed(Feed):
    title="LCK的博客"
    description="介绍一些Python的开发知识"
    link='/'

    def items(self):
        return Article.objects.order_by('-create_time')[:4]

    #标题
    def item_title(self, item):
        return item.title

    #详情页
    def item_link(self, item):
        return reverse('blog:single',args=(item.id,))

    #描述
    def item_description(self, item):
        return item.body








