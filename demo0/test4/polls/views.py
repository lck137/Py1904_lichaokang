from django.shortcuts import render,reverse,redirect

# Create your views here.
from .models import Question,Choice


def index(request):
    questions=Question.objects.all()
    return render(request,"polls/index.html",{"questions":questions})

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

def result(request,id):
    question=Question.objects.get(pk=id)
    return render(request,"polls/result.html",{'question':question})














