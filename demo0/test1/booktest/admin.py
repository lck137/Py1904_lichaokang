from django.contrib import admin
from .models import *


# Register your models here.


class BookinfoInline(admin.StackedInline):
    model = Heroinfo
    #关联个数
    extra = 1


#注册书籍模块

class BookinfoAdmin(admin.ModelAdmin):
    #显示字段，可以点击列头进行排序
    list_display = ["title"]
    #过滤字段，过滤框会出现在右侧
    list_filter = ["title"]
    #搜索字段，搜索框会出现在上侧
    search_fields = ['title']
    #分页，分页框会出现在下侧
    list_per_page = 1
    inlines = [BookinfoInline]



admin.site.register(Bookinfo, BookinfoAdmin)

#注册英雄模块

class HeroinfoInline(admin.StackedInline):
    model = Bookinfo
    #关联个数
    extra = 1


class HeroinfoAdmin(admin.ModelAdmin):
    #显示字段，可以点击列头进行排序
    list_display = ["name","content","book"]
    # 过滤字段，过滤框会出现在右侧
    list_filter = ["name","content","book"]
    # 搜索字段，搜索框会出现在上侧
    search_fields = ["name","content","book"]
    # 分页，分页框会出现在下侧
    list_per_page = 1


admin.site.register(Heroinfo,HeroinfoAdmin)