from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Auditable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(default=-1)
    updated_by = models.IntegerField(default=-1)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Modelmodel(Auditable):
    title = models.CharField(max_length=200)
    body = RichTextUploadingField()
