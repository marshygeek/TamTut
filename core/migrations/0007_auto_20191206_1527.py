# Generated by Django 2.2.7 on 2019-12-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191206_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='TamTut', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='TamTut', help_text='Optional.', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='TamTut', help_text='Optional.', max_length=30),
        ),
    ]
