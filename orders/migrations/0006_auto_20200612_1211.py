# Generated by Django 3.0.5 on 2020-06-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200612_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='adress',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
