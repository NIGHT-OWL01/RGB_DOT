# Generated by Django 3.2.9 on 2021-12-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='implements',
            name='name',
            field=models.CharField(default='no', max_length=20),
        ),
        migrations.AddField(
            model_name='tractor',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]