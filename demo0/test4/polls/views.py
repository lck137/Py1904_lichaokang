from django.shortcuts import render,reverse,redirect,HttpResponse
from django.contrib.auth import authenticate,logout,login
# Create your views here.
from .models import Question,Choice,PollsUser


#装饰器
def checklogin(func):
    def check(request,*args):
        #1.cookie方法
        # username=request.COOKIES.get('username')
        #2.session方法
        # username=request.session.get('username')
        if request.user and request.user.is_authenticated:
            return func(request,*args)
        else:
            return redirect(reverse('polls:pregister'))
    return check

@checklogin
def index(request):
    #1.cookie方法
    # username = request.COOKIES.get('username')
    #2.session方法
    # username=request.session.get('username')
    # if username != None:
    #     questions=Question.objects.all()
    #     return render(request,"polls/index.html",{"questions":questions,'username':username})
    # else:
    #     return redirect(reverse("polls:plogin"))


    #3.用户授权

    username=request.user
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions,'username':username})


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




        return render(request,"polls/plogin.html")
    elif request.method == "POST":

    #     #1.cookie方法
    #     response=redirect(reverse("polls:index"))
    #     # response.set_cookie("username",request.POST.get('username'))
    #     # return response
    #
    #     #2.session方法
    #     request.session['username']=request.POST.get('username')
    #     return redirect(reverse("polls:index"))
        #3.Django自带授权
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect(reverse("polls:index"))
        else:
            return render(request,"polls/plogin.html",{'errors':'登录失败'})

def pregister(request):
    if request.method =="GET":
        return render(request,"polls/pregister.html")
    elif request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=PollsUser.objects.create_user(username=username,password=password)
        if user:
            print(user,'=========')
            return redirect(reverse('polls:plogin'))
        else:
            return redirect(reverse('polls:pregister'))


#退出
def ploginout(request):
    # 1.cookie方法
    # res=redirect(reverse("polls:plogin"))
    # res.delete_cookie('username')
    # return res

    #2.session方法
    # request.session.flush()
    # return redirect(reverse("polls:plogin"))

    #3.Django自带授权
    logout(request)
    return redirect(reverse('polls:plogin'))











