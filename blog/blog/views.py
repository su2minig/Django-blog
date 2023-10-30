from typing import Any
# from django.db.models.query import QuerySet
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/blog.html'
    def get_queryset(self):
        request = self.request
        a = search(request)
        return a


blog = PostList.as_view()

def search(request):
    if request.GET.get('q'):
        q = request.GET.get('q')
        result = Post.objects.filter(Q(title__icontains=q) | Q(contents__icontains=q) | Q(tags__name__icontains=q)).distinct()
    else:
        result = Post.objects.all()
    # print(result)
    return result
    # return render(request, 'blog/blog.html', {'result': result})



class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        print(self.kwargs)
        post = Post.objects.get(pk=pk)
        post.view_count += 1
        post.save()
        return super().get_object(queryset)


post = PostDetail.as_view()

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog')
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        print(self)
        print(form)
        print(self.request)
        post = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
        post.author = self.request.user
        return super().form_valid(form)


write = PostCreate.as_view()

class PostUpdate(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog')

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user

edit = PostUpdate.as_view()


class PostDelete(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog')

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user

delete = PostDelete.as_view()


# search = PostSearch.as_view()
