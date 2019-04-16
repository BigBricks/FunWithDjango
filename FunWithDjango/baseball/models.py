# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name

class Player(models.Model):
    player_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=2)
# Create your models here.
