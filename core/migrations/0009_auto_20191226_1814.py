# Generated by Django 2.2.7 on 2019-12-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20191226_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
