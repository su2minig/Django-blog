from django import forms
from .models import Post, Tag, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents', 'image', 'file','tags'] 
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'contents': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']