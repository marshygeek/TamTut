# Generated by Django 2.2.7 on 2019-12-29 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20191228_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfeed',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_by', to='core.Profile'),
        ),
        migrations.AlterField(
            model_name='userfeed',
            name='user_profile_posted',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_posted', to='core.Profile'),
        ),
    ]
