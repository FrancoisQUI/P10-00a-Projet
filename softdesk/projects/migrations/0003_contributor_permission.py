# Generated by Django 3.2.9 on 2021-11-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20211125_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='permission',
            field=models.CharField(blank=True, choices=[('Create', 'Create'), ('Read', 'Read'), ('Update', 'Update'), ('Delete', 'Delete')], max_length=6),
        ),
    ]