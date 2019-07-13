from django.shortcuts import render,reverse,redirect,HttpResponse,get_object_or_404
from django.views import View
from .models import *
from .forms import ArticleFrom,CommentForm,UserRegisterForm,UserLoginForm
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,logout,login
from PIL import ImageDraw,Image,ImageFont
import io,random
from django.core.cache import cache
from django.core.mail import send_mass_mail,send_mail,EmailMultiAlternatives
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer


# Create your views here.

#序列化


#主页

#装饰器
def checklogin(func):
    def check(request,*args):
        if request.user and request.user.is_authenticated:
            return func(request,*args)
        else:
            return redirect(reverse('blog:login1'))
    return check





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
        page=getpage(request,articles,3)
        return render(request,'blog/index.html',{'page':page,'ads':ads,'date_list':date_list})
    def post(self,request):
        redirect(reverse('blog:index'))


class SingleView(View):
    def get(self,request,id):
        article=get_object_or_404(Article,pk=id)
        comform=CommentForm()
        article.votes+=1
        article.save()
        return render(request,'blog/single.html',{'article':article,'comform':comform,
                                                  'create_time':article.create_time,})
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

class Full(View):
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
#标签
class TagesView(View):
    def get(self,request,id):
        tag=Tag.objects.get(pk=id)
        articles=tag.article_set.all()
        page=getpage(request,articles,1)
        return render(request,'blog/index.html',{'page':page})


#注册
def register(request):
    if request.method == "POST":
        user_form=UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.is_active=False
            new_user.save()
            recvlist=['15239222843@163.com']

            # 发送邮件  SMTP POP3
            serializer = TimedJSONWebSignatureSerializer(settings.SECRET_KEY)
            serializerstr=serializer.dumps({'userid':new_user.id}).decode('utf-8')
            try:
                send_mail('Django邮件', 'Django可以发送邮件', settings.DEFAULT_FROM_EMAIL, recvlist)
                mail = EmailMultiAlternatives("python发送激活验证邮件",
                                          "<h2><a href='http://127.0.0.1:8000/active/%s/'>点我 激活</a></h2>"%(serializerstr),settings.EMAIL_HOST_USER, recvlist)
                mail.content_subtype = 'html'
                mail.send()
                print('发送成功')
            except Exception as e:
                print(e)
            return render(request,'blog/login.html')
        else:
            return HttpResponse('注册表单输入有错')

    elif request.method == "GET":
        user_form=UserRegisterForm()
        context={'user_form':user_form}
        return render(request,'blog/register.html',context)
    else:
        return HttpResponse('请用get或post请求数据')

#登录
def login1(request):
    if request.method == 'POST':
        user_form = UserLoginForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        verifycode=request.POST.get('verify')
        if verifycode == cache.get('verify'):
            return HttpResponse('验证码错误')
        user = authenticate(request, username=username, password=password)
        if user:
            # 将用户数据保存在 session 中，即实现了登录动作
            login(request, user)
            return redirect("blog:index")
        else:
            return render(request,'blog/login.html')
    elif request.method == 'GET':
        user_form = UserLoginForm()
        context = {'user_form': user_form}
        return render(request, 'blog/login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")
#用户激活
def active(request,id):

    serializerstr = TimedJSONWebSignatureSerializer(settings.SECRET_KEY)
    serializerobj=serializerstr.loads(id)
    id=serializerobj['userid']
    user = get_object_or_404(User, pk=id)
    user.is_active = True
    user.save()
    return redirect(reverse('blog:login1'))

#退出
def loginout1(request):
    logout(request)
    return redirect(reverse('blog:index'))

#验证码
def verify(request):
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 25
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
    fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
    draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    cache.set('verify',rand_str)
    # 构造字体对象
    font = ImageFont.truetype('calibrib.ttf', 28)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')


