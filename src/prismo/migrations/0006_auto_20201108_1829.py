# Generated by Django 3.1.2 on 2020-11-08 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prismo', '0005_doorlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doorlog',
            name='door_key',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
