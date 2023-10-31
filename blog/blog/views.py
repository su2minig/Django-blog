from typing import Any
# from django.db.models.query import QuerySet
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/blog.html'
    print(dir(ListView))
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(contents__icontains=q) | Q(tags__name__icontains=q)).distinct()
        return queryset


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
        # print(self.kwargs)
        post = Post.objects.get(pk=pk)
        post.view_count += 1
        post.save()
        return super().get_object(queryset)
    
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        # form = CommentForm()
        # print(request.POST)
        # if request == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            c = Comment.objects.create(
                content=form.cleaned_data['content'],
                post=post,
                author=request.user
            )
            c.save()
        return render(request, 'blog/post.html', {'post': post, 'form': form})



def comments_delete(request, pk, comment_pk):
    print(request)
    comment = Comment.objects.get(pk=comment_pk)
    print(comment)
    comment.delete()
    return redirect('blog:post', pk)

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
