
from comment.models import Comment
from django import forms
from .models import Article
from django.contrib.auth.models import User

class ArticleFrom(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','body','category']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),

        }
        labels={
            'title':'文章标题',
            'body':'文章正文',
            'category':'文章类别',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','url','content']



class UserRegisterForm(forms.ModelForm):
    password=forms.CharField(label=u"密码")
    password2=forms.CharField(label=u"重复密码")
    class Meta:
        model=User
        fields=['username','email']

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password'] !=cd['password2']:
            raise forms.ValidationError(u"密码不匹配")
        return cd['password2']


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)

    class Meta:
        model=User
        fields=['username','password']




