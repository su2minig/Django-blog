from django.contrib import admin
from .models import Post, Tag, Comment, ReComment

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(ReComment)