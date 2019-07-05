from django.contrib import admin

# Register your models here.

from .models import Question,Choice



class QuestionInline(admin.StackedInline):
    model = Choice
    #关联个数
    extra = 1
class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)



