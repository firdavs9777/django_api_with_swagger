# Generated by Django 2.2.6 on 2022-07-15 02:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostsModel',
            new_name='Post',
        ),
    ]
