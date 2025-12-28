from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    """博客文章表单"""
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {
            'title': '文章标题',
            'text': '文章内容',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入标题（最多200个字符）'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '请输入文章内容...',
                'rows': 8,
            }),
        }