from django.contrib.auth.models import User
from django.db import models
from projects.models import Project

ISSUE_TAG_CHOICES = (("Bug", "Bug"), ("Improvement", "Improvement"), ("Task", "Task"))
ISSUE_PRIORITY_CHOICES = (('Low', "Low"), ("Mid", "Mid"), ("High", "High"))
ISSUE_STATUS_CHOICES = (("To-Do", "To-Do"), ("Pending", "Pending"), ("Closed", "Closed"))


class Issue(models.Model):
    title = models.CharField(max_length=100, blank=False)
    desc = models.CharField(max_length=2000, blank=False)
    tag = models.CharField(choices=ISSUE_TAG_CHOICES, max_length=100,  blank=False)
    priority = models.CharField(choices=ISSUE_PRIORITY_CHOICES, max_length=100,  blank=False)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, blank=False)
    status = models.CharField(choices=ISSUE_STATUS_CHOICES, max_length=100,  blank=False)
    author_user_id = models.ForeignKey(User, related_name="issue_author", on_delete=models.CASCADE, blank=False)
    assignee_user_id = models.ForeignKey(User, related_name="issue_assigned_user",
                                         on_delete=models.CASCADE, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)

