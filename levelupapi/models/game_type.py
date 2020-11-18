from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

class GameType(models.Model):
  label = models.CharField(max_length=25)
