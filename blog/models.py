from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

user = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    user = models.ForeignKey(user, default=1, null=True, on_delete=models.SET_NULL)
    title = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    description = RichTextField(blank=True)
    article_types = [('Programming', 'Programming'), ('UX/UI', 'UX/UI'), ('Electronics', 'Electronics'),
                     ('Other', 'Other')]
    article_type = models.CharField(max_length=20, choices=article_types, default='Programming')
    content = RichTextUploadingField()

    # displays title instead of object in django admin
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
