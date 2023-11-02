from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='blog'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('<int:pk>/create/comment/', views.CommentCreateView.as_view(), name='comment_create'),
    path('<int:pk>/delete/comment/<int:comment_pk>/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('<int:pk>/update/comment/<int:comment_pk>/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('<int:pk>/create/recomment/', views.ReCommentCreateView.as_view(), name='recomment_create'),
    path('<int:pk>/delete/recomment/<int:recomment_pk>/', views.ReCommentDeleteView.as_view(), name='recomment_delete'),
    path('<int:pk>/update/recomment/<int:recomment_pk>/', views.ReCommentUpdateView.as_view(), name='recomment_update'),
    path('write/', views.PostCreateView.as_view(), name='write'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
]