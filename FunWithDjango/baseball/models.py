# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Player(models.Model):
    player_name = models.CharField(max_length=100)
    name_team = models.OneToOneField("Team", blank=True)
    position = models.CharField(max_length=2)


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    team_members = models.ManyToManyField(Player, blank=True)

    def __str__(self):
        return "%s %s" % (self.team_name, self.team_members)


# Create your models here.
