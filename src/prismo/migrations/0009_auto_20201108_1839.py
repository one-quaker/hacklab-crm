# Generated by Django 3.1.2 on 2020-11-08 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prismo', '0008_auto_20201108_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doorlog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='door_log', to='prismo.userprofile'),
        ),
    ]