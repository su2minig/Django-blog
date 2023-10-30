from django import forms
from .models import Post, Tag
# , Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'contents', 'image', 'file','tags'] 
        #  'thumb_image', 'file_upload', 

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['message']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']