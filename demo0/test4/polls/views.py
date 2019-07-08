from django.shortcuts import render,reverse,redirect

# Create your views here.
from .models import Question,Choice


#装饰器

def checklogin(func):
    def check(request,*args):
        username=request.COOKIES.get('username')
        if username:
            return func(request,*args)
        else:
            return redirect(reverse("polls:plogin"))
    return check

@checklogin
def index(request):
    username = request.COOKIES.get('username')
    if username != None:
        questions=Question.objects.all()
        return render(request,"polls/index.html",{"questions":questions,'username':username})
    else:
        return redirect(reverse("polls:plogin"))


@checklogin
def detail(request,id):
    question=Question.objects.get(pk=id)
    if request.method == 'GET':
        return render(request,'polls/detail.html',{"question":question})
    elif request.method == 'POST':
        optionid=request.POST.get('option')
        option=Choice.objects.get(pk=optionid)
        option.num+=1
        option.save()

        return redirect(reverse("polls:result",args=(id,)))
@checklogin
def result(request,id):
    question=Question.objects.get(pk=id)
    return render(request,"polls/result.html",{'question':question})


#登录
def plogin(request):
    if request.method == "GET":
        return render(request,"polls/plogin.html",{})
    elif request.method == "POST":
        response=redirect(reverse("polls:index"))
        response.set_cookie("username",request.POST.get('username'))
        return response
#退出
def ploginout(request):
    # 1.cookie方法
    res=redirect(reverse("polls:plogin"))
    res.delete_cookie('username')
    return res












