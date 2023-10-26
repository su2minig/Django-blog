from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/blog.html'
    def get_queryset(self):
        request = self.request
        a = search(request)
        return a



def search(request):
    if request.GET.get('q'):
        q = request.GET.get('q')
        result = Post.objects.filter(Q(title__icontains=q) | Q(contents__icontains=q)).distinct()
    else:
        result = Post.objects.all()
    print(result)
    return result
    # return render(request, 'blog/blog.html', {'result': result})


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post.html'

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog')

class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog')

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog')





blog = PostList.as_view()
post = PostDetail.as_view()
write = PostCreate.as_view()
edit = PostUpdate.as_view()
delete = PostDelete.as_view()
# search = PostSearch.as_view()
