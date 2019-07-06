from django.contrib import admin

# Register your models here.
from .models import Question,Choice


# class QuestionInline(admin.StackedInline):
#     model = Choice
#     extra = 1
#
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ['title']
#     inlines = [QuestionInline]
#
# class ChoiceInline(admin.StackedInline):
#     model = Question
#     extra = 1
#
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ['option']
#     inlines = [ChoiceInline]


admin.site.register(Question)
admin.site.register(Choice)




