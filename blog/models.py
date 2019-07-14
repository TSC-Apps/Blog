from django.db import models
from django.conf import settings
from tinymce.models import HTMLField

# Create your models here.

user = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    user = models.ForeignKey(user, default=1, null=True, on_delete=models.SET_NULL)
    title = models.TextField()

    # slug title of blog post in url
    slug = models.SlugField(unique=True)
    content = HTMLField()

    # displays title instead of object in django admin
    def __str__(self):
        return self.title
