
from django.forms.models import ModelForm
from .models import Article
from django import forms

from .models import Article

class ArticleFrom(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','body']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'})

        }
        labels={
            'title':'文章标题',
            'body':'文章正文',
        }










