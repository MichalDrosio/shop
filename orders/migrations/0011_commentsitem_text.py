# Generated by Django 3.0.5 on 2020-06-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_commentsitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsitem',
            name='text',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]