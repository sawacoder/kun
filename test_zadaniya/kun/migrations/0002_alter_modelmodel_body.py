# Generated by Django 3.2.7 on 2021-10-13 11:56

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kun', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelmodel',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
