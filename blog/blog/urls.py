from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>/', views.post, name='post'),
    # path('<int:pk>/comments', views.comments_create, name='comments_create'),
    path('<int:pk>/delete/comments/<int:comment_pk>/', views.comments_delete, name='comments_delete'),
    path('write/', views.write, name='write'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('search/<str:tag>/', views.search, name='search'),
]