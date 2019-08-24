from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, password=None):
        if not username or not first_name or not last_name:
            raise ValueError("No credentials passed")
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, password):
        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password, )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    is_admin = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='profile_photos')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin


class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    article_types = [('Programming', 'Programming'), ('UX/UI', 'UX/UI'), ('Electronics', 'Electronics'),
                     ('Other', 'Other')]
    article_type = models.CharField(max_length=20, choices=article_types, default='Programming')
    content = RichTextUploadingField()

    # displays title instead of object in django admin
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
