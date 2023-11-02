from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, username, nickname, email, password, profile_image=None):        
        if not email:            
            raise ValueError('이메일을 기입해주세요')
        if not username:            
            raise ValueError('아이디를 입력하세요')
        if not password:            
            raise ValueError('비밀번호를 입력해주세요')

        user = self.model(            
            email=email,
            username=username,
            nickname=nickname,
            profile_image=profile_image,       
        )        
        user.set_password(password)        
        user.save()        
        return user

    def create_superuser(self, username, nickname, email, password):        
    
        user = self.create_user(            
            email = email,
            username = username,
            nickname = nickname,               
            password=password,
            )
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user 


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    email = models.EmailField(        
        max_length=255,        
        unique=True,    
        )
    username = models.CharField(max_length=20, default="", unique=True)
    nickname = models.CharField(max_length=20, default="", unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['email','nickname']
    profile_image = models.ImageField(
        upload_to='accounts/profile_images/%Y/%m/%d', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.nickname

    @property
    def is_staff(self):
        return self.is_admin