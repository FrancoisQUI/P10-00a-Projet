from django.db import models

from django.contrib.auth.models import User


PROJECT_TYPE_CHOICES = (('Backend', 'Backend'),
                        ('Frontend', 'Frontend'),
                        ('iOS', 'iOS'),
                        ('Android', 'Android'))

CONTRIBUTOR_PERMISSION_CHOICES = (('Read', 'Read'),
                                  ('Write', 'Write'))


class Project(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=2000, blank=False)
    type = models.CharField(choices=PROJECT_TYPE_CHOICES,
                            max_length=100, blank=False)
    author_user_id = models.ForeignKey(to=User,
                                       related_name='projects',
                                       on_delete=models.CASCADE)
    contributors = models.ManyToManyField(User,
                                          through="Contributor")

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user_id = models.ForeignKey(to=User,
                                related_name='contributor_user',
                                on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Project,
                                   related_name='contributor_project',
                                   on_delete=models.CASCADE)
    role = models.CharField(max_length=100, blank=False)
    permission = models.CharField(choices=CONTRIBUTOR_PERMISSION_CHOICES,
                                  max_length=6,
                                  blank=False, default='Read')

    class Meta:
        unique_together = ('project_id', 'user_id')

