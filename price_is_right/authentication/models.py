from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    company = models.CharField(blank=True, max_length=10)

    def __unicode__(self):
        return self.user.username
