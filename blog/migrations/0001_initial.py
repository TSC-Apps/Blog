# Generated by Django 2.2.3 on 2019-08-24 07:27

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('is_admin', models.BooleanField(default=False)),
                ('avatar', models.ImageField(upload_to='profile_photos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('article_type', models.CharField(choices=[('Programming', 'Programming'), ('UX/UI', 'UX/UI'), ('Electronics', 'Electronics'), ('Other', 'Other')], default='Programming', max_length=20)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
