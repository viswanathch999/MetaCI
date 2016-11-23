from __future__ import unicode_literals

from django.db import models

class Repository(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    
class Branch(models.Model):
    name = models.CharField(max_length=255)
    repo = models.ForeignKey(Repository, related_name='branches')
    deleted = models.BooleanField(default=False)