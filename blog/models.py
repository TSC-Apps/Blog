from django.db import models
from django.conf import settings
from tinymce.models import HTMLField

# Create your models here.

user = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    user = models.ForeignKey(user, default=1, null=True, on_delete=models.SET_NULL)
    title = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    # slug title of blog post in url
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    article_types = [('Programming', 'Programming'), ('UX/UI', 'UX/UI'), ('Electronics', 'Electronics'),
                     ('Other', 'Other')]
    article_type = models.CharField(max_length=20, choices=article_types, default='Programming')
    content = HTMLField()

    # displays title instead of object in django admin
    def __str__(self):
        return self.title
