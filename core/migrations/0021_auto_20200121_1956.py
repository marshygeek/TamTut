# Generated by Django 2.2.7 on 2020-01-21 16:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20200108_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupchat',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupchat',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='groupchat',
            name='chat_title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
