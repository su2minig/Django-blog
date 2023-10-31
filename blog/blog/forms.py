from django import forms
from .models import Post, Tag, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents', 'image', 'file','tags'] 
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ['content']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']