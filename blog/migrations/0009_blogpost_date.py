# Generated by Django 2.2.3 on 2019-07-23 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190716_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
