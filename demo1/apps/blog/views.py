from django.shortcuts import render,reverse,redirect,HttpResponse,get_object_or_404
from django.views import View
from .models import *
from .forms import ArticleFrom
from django.core.paginator import Paginator

# Create your views here.

#主页

class IndexView(View):
    def get(self,request):
        ads=Ads.objects.all()
        articles=Article.objects.all()
        pagenum=request.GET.get('page')
        pagenum=1 if not pagenum else pagenum
        page=Paginator(articles,1).get_page(pagenum)
        return render(request,'blog/index.html',{'page':page,'ads':ads})

    def post(self,request):

        redirect(reverse('blog:index'))

class SingleView(View):
    def get(self,request):
        article=Article.objects.all()
        return render(request,'blog/single.html',locals())

    def post(self,request):
        return redirect(reverse('blog:single'))

class AddArticleView(View):
    def get(self,request):
        artform = ArticleFrom()
        return render(request,'blog/addarticle.html',locals())

    def post(self,request):
        artform = ArticleFrom(request.POST)
        if artform.is_valid():
            article = artform.save(commit=False)
            article.category = Category.objects.first()
            article.author = User.objects.first()
            article.save()
            return redirect(reverse('blog:index'))


class FullView(View):
    def get(self,request):
        return render(request, "blog/full-width.html")

    def post(self,request):
        return redirect(reverse('blog:full'))

class ContactView(View):
    def get(self,request):
        return render(request, "blog/contact.html")

    def post(self,request):
        return redirect(reverse('blog:contact'))

#分类
def category(request):
    category_list=Category.objects.all()
    print(category_list,'===========')
    return render(request,'blog/index.html',{'category_list':category_list})

#归档
def archives(request,):

    date_list=Article.objects.get('create_time')
    return render(request,'blog/index.html',context={'date_list':date_list})


def article_list(request):
    article_list=Article.objects.all()
    paginator=Paginator(article_list,1)

    page=request.GET.get('page')
    articles=paginator.get_page(page)

    context={'articles':articles}

    return render(request,'blog/index.html',context)