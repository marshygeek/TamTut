# Generated by Django 2.2.7 on 2019-12-27 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20191227_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followed',
        ),
    ]
