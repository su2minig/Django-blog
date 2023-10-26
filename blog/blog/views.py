from django.shortcuts import render
from .models import Post

def blog(request):
    list = Post.objects.all()
    return render(request, 'blog/blog.html', {'list':list})

def post(request, pk):
    pk = Post.objects.get(pk=pk)
    return render(request, 'blog/post.html', {'pk':pk})