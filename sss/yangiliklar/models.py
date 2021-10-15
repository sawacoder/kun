from django.db import models
from django.contrib.admin.decorators import register


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    body = models.TextField()
    posted_by = models.IntegerField(default=-1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "News"

    def __str__(self):
        return self.title


class Like(models.Model):
    is_like = models.IntegerField(default=1, null=False)
    liked_by = models.IntegerField(default=-1, null=False)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "likes"

    def __str__(self):
        return str(self.post.id)


class Comment(models.Model):
    comment = models.CharField(max_length=270)
    commented_by = models.IntegerField(default=-1, null=False)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.comment
