from django.contrib import admin
from .models import Bookinfo,Heroinfo
# Register your models here.


class BookinfoInline(admin.StackedInline):
    model = Heroinfo
    extra = 1


class BookinfoAdmin(admin.ModelAdmin):
    list_display = ["title"]
    inlines =[BookinfoInline]

class HeroinfoInline(admin.StackedInline):
    model = Bookinfo
    extra = 2

class HeroinfoAdmin(admin.ModelAdmin):
    list_display = ["name",]
    inlines = [HeroinfoInline]


admin.site.register(Bookinfo)
admin.site.register(Heroinfo)







