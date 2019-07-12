from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse
from .models import Comment,Article
from django.views.generic import View
# Create your views here.

class AddComment(View):
    def post(self,request,id):
        name=request.POST.get('name')
        email = request.POST.get('email')
        url = request.POST.get('url')
        content = request.POST.get('content')

        c=Comment()
        c.name=name
        c.email=email
        c.url=url
        c.content=content
        c.article=Article.objects.get(pk=id)
        c.save()

        return JsonResponse({'name':name,'email':email,'url':url,'content':content,
                             'create_time':c.create_time})















