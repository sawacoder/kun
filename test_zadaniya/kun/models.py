from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.db import models


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
    title = RichTextField()
    body = RichTextUploadingField()
    text = RichTextUploadingField(null=True)

    def __str__(self):
        return self.title


class Rightmodel(Auditable):
    title = RichTextField()
    body = RichTextUploadingField()
    text = RichTextUploadingField(null=True)

    def __str__(self):
        return self.title
