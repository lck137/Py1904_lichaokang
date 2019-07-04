from django.shortcuts import render,redirect,reverse

# Create your views here.

from django.conf.urls import url
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Bookinfo,Heroinfo


def index(request):
    # return HttpResponse("<h1 style='color:green'>首页</h1> <a href='/booktest/list/'>跳转到列表页</a>" )
    #获取模板
    # temp1=loader.get_template("booktest/index.html")
    #使用模块渲染字典参数
    # result=temp1.render({"username":'lck'})
    #将渲染的结果返回
    # return HttpResponse(result)
    return render(request,"booktest/index.html",{"username":'lck'})

def list(request):

    books=Bookinfo.objects.all()
    return render(request,"booktest/list.html",{"books":books})

def detail(request,s):

    books=Bookinfo.objects.get(pk=s)
    return render(request,"booktest/detail.html",{"books":books})

def delhero(request,id):
    hero=Heroinfo.objects.get(pk=id)
    bookid=hero.book.id
    hero.delete()
    return redirect(reverse("booktest:detail",args=(bookid,)))

def addhero(request,id):
    book =Bookinfo.objects.get(pk=id)
    if request.method=="GET":
        return render(request,"booktest/addhero.html",{"book":book})
    elif request.method=="POST":
        name=request.POST.get("username")
        content=request.POST.get("content")
        gender=request.POST.get("gender")
        hero=Heroinfo()
        hero.name=name
        hero.content=content
        hero.book=book
        hero.gender=gender
        hero.save()
        return redirect(reverse("booktest:detail",args=(id,)))

def addbook(request):
    B=Bookinfo()
    if request.method=="GET":
        return render(request,"booktest/addbook.html",{})
    elif request.method=="POST":
        title=request.POST.get("title")
        B.title=title
        B.save()
        return redirect(reverse("booktest:list"))

def delbook(request,id):
    book = Bookinfo.objects.get(pk=id)
    book.delete()
    return redirect(reverse("booktest:list", ))

