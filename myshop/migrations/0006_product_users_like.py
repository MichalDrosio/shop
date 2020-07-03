# Generated by Django 3.0.5 on 2020-06-19 12:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myshop', '0005_remove_category_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='images_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]