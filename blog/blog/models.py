from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50)
    contents = models.TextField()
    image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d',  blank=True)
    file = models.FileField(
        upload_to='blog/files/%Y/%m/%d',  blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # 처음 생성될 때만
    updated_at = models.DateTimeField(auto_now=True) # 수정될 때마다
    view_count = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        time = self.created_at.strftime('%Y-%m-%d %H:%M')
        author = self.author
        return f'제목: {self.title}, 작성자: {author},시간: {time}'
    
    def get_absolute_url(self):
        return f'/tube/{self.pk}/'
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name