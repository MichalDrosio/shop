# Generated by Django 3.0.5 on 2020-06-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200612_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='self_phone',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
