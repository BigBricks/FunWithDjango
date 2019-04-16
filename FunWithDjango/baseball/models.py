# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=2)
# Create your models here.
