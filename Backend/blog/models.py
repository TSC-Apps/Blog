from django.db import models
from django.conf import settings

# Create your models here.

user = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    user = models.ForeignKey(user, default=1, null=True, on_delete=models.SET_NULL)
    title = models.TextField()

    # slug title of blog post in url
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
