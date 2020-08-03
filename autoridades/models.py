from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Autoridad(models.Model):

    cargo = models.CharField(max_length=254, null=True, blank=True,)
    name = models.CharField(max_length=254, null=True, blank=True,)
    


    
