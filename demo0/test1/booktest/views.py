from django.shortcuts import render

# Create your views here.

from django.conf.urls import url
from django.http import HttpResponse
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
    s = '''
        <br>
        <a href='/detail/1/'>跳转到详情页1</a>
        <br>
        <a href='/detail/2/'>跳转到详情页2</a>
        <br>
        <a href='/detail/3/'>跳转到详情页3</a>
        '''
    # return HttpResponse("<h2 style='color:red'>列表页</h2> %s"%(s,))

    # temp2=loader.get_template("booktest/list.html")
    # books = Bookinfo.objects.all()
    # result=temp2.render({"books":books})
    # return HttpResponse(result)
    books=Bookinfo.objects.all()
    return render(request,"booktest/list.html",{"books":books})




def detail(request,s):
    # return HttpResponse("<h3 style='color:hotpink;font-family:楷体;font-size:25px'>详情%s页</h3> <a href='/booktest/'>跳转到首页</a>")

    temp3=loader.get_template("booktest/detail.html")
    books=Bookinfo.objects.get(pk=s)
    result=temp3.render({"books":books})
    return HttpResponse(result)



