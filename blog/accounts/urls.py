from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update/<int:pk>', views.ProfileUpdateView.as_view(), name='update'),
    path('delete/user/<int:pk>', views.UserDeleteView.as_view(), name='delete')
]
