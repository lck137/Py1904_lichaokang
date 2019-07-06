from django.shortcuts import render,reverse,redirect

# Create your views here.

from .models import Bookinfo,Heroinfo


def index(request):

    return render(request,"booktest/index.html",{"username":'lck'})

def list(request):
    books=Bookinfo.objects.all()
    return render(request,"booktest/list.html",{"books":books})

def detail(request,id):
    book=Bookinfo.objects.get(pk=id)
    return render(request,"booktest/detail.html",{"book":book})
def delhero(request,id):
    hero=Heroinfo.objects.get(pk=id)
    bookid=hero.book.id
    hero.delete()
    return redirect(reverse("booktest:detail",args=(bookid,)))
def delbook(request,id):
    book=Bookinfo.objects.get(pk=id)
    book.delete()
    return redirect(reverse("booktest:list"))
def addbook(request):
    B=Bookinfo()
    if request.method == "GET":
        return render(request,"booktest/addbook.html",{})
    elif request.method == "POST":
        title=request.POST.get('title')
        B.title=title
        B.save()
        return redirect(reverse("booktest:list"))

def addhero(request,id):

    book=Bookinfo.objects.get(pk=id)
    if request.method == "GET":
        return render(request,"booktest/addhero.html",{"book":book})
    elif request.method == "POST":
        name=request.POST.get("name")
        content=request.POST.get("content")
        gender=request.POST.get("gender")
        hero = Heroinfo()
        hero.name=name
        hero.content=content
        hero.gender=gender
        hero.book=book
        hero.save()
        # Heroinfo.objects.addhero(name,content,gender,book)
        return redirect(reverse("booktest:detail",args=(id,)))



















