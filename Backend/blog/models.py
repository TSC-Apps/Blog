from django.db import models


# Create your models here.

class BlogPost(models.Model):
    title = models.TextField()

    # slug title of blog post in url
    slug = models.SlugField(unique=True)

    content = models.TextField(null=True, blank=True)
