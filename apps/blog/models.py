from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    name = models.CharField(max_length=100)
    body = RichTextUploadingField()

    def __str__(self):
        return self.name