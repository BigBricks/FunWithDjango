# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return "%s %s" % (self.team_name, self.players)


class Player(models.Model):
    player_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team)
    position = models.CharField(max_length=2)


# Create your models here.
