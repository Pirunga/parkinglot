# Generated by Django 3.2 on 2021-05-17 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0002_auto_20210515_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='motocycle_spaces',
            new_name='motorcycle_spaces',
        ),
    ]
