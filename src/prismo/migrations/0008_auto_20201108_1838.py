# Generated by Django 3.1.2 on 2020-11-08 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prismo', '0007_auto_20201108_1836'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='useraccess',
            unique_together={('user', 'access')},
        ),
    ]