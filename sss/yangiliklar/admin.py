from django.contrib import admin

# Register your models here.
from yangiliklar.models import (
    Post, Like, Comment
)

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
