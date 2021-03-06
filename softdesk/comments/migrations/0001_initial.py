# Generated by Django 3.2.9 on 2021-11-24 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL)),
                ('issue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commented_issue', to='issues.issue')),
            ],
        ),
    ]
