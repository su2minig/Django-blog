from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 처음 생성될 때만
    updated_at = models.DateTimeField(auto_now=True) # 수정될 때마다
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        time = self.created_at.strftime('%Y-%m-%d %H:%M')
        return f'제목: {self.title}, 시간: {time}'
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name