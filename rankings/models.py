from django.db import models
from django.contrib.auth import get_user_model



class Player(models.Model):
    
    name = models.CharField(max_length=254, null=True, blank=True,)
    ranking = models.IntegerField()
    elo = models.IntegerField(blank=True, null=True)
