from typing import Any
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


class PostListView(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/blog.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(contents__icontains=q) | Q(tags__name__icontains=q)).distinct()
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.view_count += 1
        post.save()
        return super().get_object(queryset)
    

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post.html'
    
    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs['pk'])
        comment = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
        comment.post = post
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blog:post', kwargs={'pk': self.kwargs['pk']})


comment_create = CommentCreateView.as_view()

class CommentUpdateView(UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    pk_url_kwarg = 'comment_pk'

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse_lazy('blog:post', kwargs = {'pk':self.object.post.pk})

comment_update = CommentUpdateView.as_view()


class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment
    pk_url_kwarg = 'comment_pk'

    def test_func(self):
        print(self.kwargs)
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse_lazy('blog:post', kwargs = {'pk':self.kwargs['pk']})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:blog')
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        post = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
        post.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:blog')
    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog')

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        print(self.get_object())
        return self.get_object().author == self.request.user