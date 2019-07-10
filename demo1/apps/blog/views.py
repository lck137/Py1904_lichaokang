from django.shortcuts import render,reverse,redirect,HttpResponse

from .models import *
# Create your views here.

#主页
def index(request):
    if request.method == "GET":
        return render(request,'blog/index.html')
    elif request.method == "POST":
        redirect(reverse('blog:index'))

def full(request):
    if request.method== "GET":
        return render(request, "blog/full-width.html")
    elif request.method == "POST":
        return redirect(reverse('blog:full'))

def single(request):
    if request.method == "GET":
        return render(request, "blog/single.html")
    elif request.method == "POST":
        return redirect(reverse('blog:single'))

def contact(request):
    if request.method == "GET":
        return render(request, "blog/contact.html")
    elif request.method == "POST":
        return redirect(reverse('blog:contact'))

