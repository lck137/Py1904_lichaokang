
from comment.models import Comment
from django import forms
from .models import Article

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











