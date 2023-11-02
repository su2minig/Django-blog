from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>/', views.post, name='post'),
    path('<int:pk>/create/comment/', views.comment_create, name='comment_create'),
    path('<int:pk>/delete/comment/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
    path('<int:pk>/update/comment/<int:comment_pk>/', views.comment_update, name='comment_update'),
    path('write/', views.write, name='write'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]