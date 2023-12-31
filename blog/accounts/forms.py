from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class ProfileUpdateForm(UserCreationForm):
    nickname = forms.CharField(label="별명")
    profile_image = forms.ImageField(label="프로필 이미지")

    class Meta:
        model = User
        fields = ['nickname', 'profile_image','password1', 'password2']
        


class UserForm(UserCreationForm, forms.ModelForm):
    profile_image = forms.ImageField(required=False)
    nickname = forms.CharField(label="별명")
    class Meta:
        model = User
        fields = ['username', 'nickname',
                'email', 'profile_image', 
                'password1', 'password2',]