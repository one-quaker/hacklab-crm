# Generated by Django 3.1.2 on 2020-11-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prismo', '0002_auto_20201108_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='door_key',
            field=models.CharField(default='', max_length=16, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
