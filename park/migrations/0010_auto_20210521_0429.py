# Generated by Django 3.2.3 on 2021-05-21 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0009_space'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='space',
            name='level_name',
        ),
        migrations.RemoveField(
            model_name='space',
            name='variety',
        ),
    ]
