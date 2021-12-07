from django.db import models
from django.contrib.auth.models import User

from issues.models import Issue


class Comment(models.Model):
    description = models.CharField(max_length=100, blank=False)
    author_user_id = models.ForeignKey(to=User,
                                        related_name='comment_author',
                                        on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issue,
                                    related_name='commented_issue',
                                    on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_user_id} - {self.issue_id} - {self.created_time}"
