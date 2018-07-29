# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Website(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    text = models.TextField()

    def __unicode__(self):
        return self.name

# class Website(models.Model):
#     time = models.CharField(max_length=100)
#     title = models.CharField(max_length=100)
#     href = models.TextField()

#     def __unicode__(self):
#         return self.title