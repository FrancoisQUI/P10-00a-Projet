# Generated by Django 3.2.9 on 2021-11-24 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=2000)),
                ('tag', models.CharField(choices=[('Bug', 'Bug'), ('Improvement', 'Improvement'), ('Task', 'Task')], max_length=100)),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Mid', 'Mid'), ('High', 'High')], max_length=100)),
                ('status', models.CharField(choices=[('To-Do', 'To-Do'), ('Pending', 'Pending'), ('Closed', 'Closed')], max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_assigned_user', to=settings.AUTH_USER_MODEL)),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_author', to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
