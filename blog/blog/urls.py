from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>/', views.post, name='post'),
    path('write/', views.write, name='write'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('search/<str:tag>/', views.search, name='search'),
]