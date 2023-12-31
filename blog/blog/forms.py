from django import forms
from .models import Post, Tag, Comment, ReComment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents', 'image', 'file','tags'] 
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control postform'}),
            'contents': forms.Textarea(attrs={'class': 'form-control postform', 'rows': 5}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control postform'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file postform'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control-file postform'}),
        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='comment',)
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }


class ReCommentForm(forms.ModelForm):
    content = forms.CharField(label = 'recomment',)
    class Meta:
        model = ReComment
        fields = ['content','comment']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }


class CommentUpdateForm(forms.ModelForm):
    content = forms.CharField(label = '수정',)
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