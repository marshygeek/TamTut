# Generated by Django 2.2.7 on 2020-01-02 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20191229_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followed',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.RemoveField(
            model_name='userfeed',
            name='user_profile_posted',
        ),
        migrations.AddField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(related_name='_profile_follows_+', to='core.Profile'),
        ),
        migrations.AddField(
            model_name='userfeed',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='core.Profile', verbose_name="author's profile"),
        ),
        migrations.DeleteModel(
            name='Followers',
        ),
    ]
