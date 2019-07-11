from django.shortcuts import render,reverse,redirect,HttpResponse,get_object_or_404
from django.views import View
from .models import *
from .forms import ArticleFrom,CommentForm
from django.core.paginator import Paginator

# Create your views here.

#主页

def getpage(request,object_list,per_num):
    pagenum=request.GET.get('page')
    pagenum=1 if not pagenum else pagenum
    page=Paginator(object_list,per_num).get_page(pagenum)
    return page





class IndexView(View):
    def get(self,request):
        ads=Ads.objects.all()
        articles=Article.objects.all()
        date_list=Article.objects.order_by('-create_time')
        page=getpage(request,articles,1)
        return render(request,'blog/index.html',{'page':page,'ads':ads,'date_list':date_list})
    def post(self,request):
        redirect(reverse('blog:index'))

class SingleView(View):
    def get(self,request,id):
        article=get_object_or_404(Article,pk=id)
        comform=CommentForm()
        article.votes+=1
        article.save()
        return render(request,'blog/single.html',{'article':article,'comform':comform})

    def post(self,request,id):
        article = get_object_or_404(Article, pk=id)
        cf=CommentForm(request.POST)
        comform=cf.save(commit=False)
        comform.article=article
        comform.save()
        return redirect(reverse('blog:single',args=(article.id,)))

class AddArticleView(View):
    def get(self,request):
        artform = ArticleFrom()
        return render(request,'blog/addarticle.html',locals())

    def post(self,request):
        artform = ArticleFrom(request.POST)
        if artform.is_valid():
            article = artform.save(commit=False)
            # article.category = Category.objects.first()
            article.author = User.objects.first()
            article.save()
            return redirect(reverse('blog:index'))
        return render(request,'blog/addarticle.html',{'error':'添加失败'})


class FullView(View):
    def get(self,request):
        ads = Ads.objects.all()
        articles = Article.objects.all()
        date_list = Article.objects.order_by('-create_time')
        page = getpage(request, articles, 5)
        return render(request, 'blog/full.html', {'page': page, 'ads': ads, 'date_list': date_list})

    def post(self,request):
        return redirect(reverse('blog:full'))

class ContactView(View):
    def get(self,request):
        return render(request, "blog/contact.html")

    def post(self,request):
        return redirect(reverse('blog:contact'))

#分类
class CategoryView(View):
    def get(self,request,id):
        category = Category.objects.get(pk=id)
        article_list=category.article_set.all()
        page=getpage(request,article_list,1)
        return render(request,'blog/index.html',{'article_list':article_list,'page':page,'category':category})

#归档
class ArchivesView(View):
    def get(self,request,year,month):
        date_list=Article.objects.filter(
            create_time__year=year,
            create_time__month=month).order_by('-create_time')
        page = getpage(request, date_list, 1)
        return render(request, 'blog/index.html', {'date_list': date_list,'page':page})

class TagesView(View):
    def get(self,request,id):
        tag=Tag.objects.get(pk=id)
        articles=tag.article_set.all()
        page=getpage(request,articles,1)
        return render(request,'blog/index.html',{'page':page})

