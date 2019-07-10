

import xadmin
from .models import *



class ArticleAdmin:
    style_fields={'body':'ueditor'}

xadmin.site.register(Category)
xadmin.site.register(Tag)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Ads)