from django.db import models
from .contants import Phonetype


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)

    # created_by = models.

    def __str__(self):
        return self.name


class Phone(models.Model):
    number = models.CharField(max_length=13)
    contacts = models.ForeignKey('Contact', on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=Phonetype.choises())

    def __str__(self):
        return self.number
