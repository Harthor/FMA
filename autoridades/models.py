from django.db import models

# Create your models here.

class Autoridad(models.Model):

    cargo = models.CharField(max_length=254, null=True, blank=True,)
    name = models.CharField(max_length=254, null=True, blank=True,)
    


    def __str__(self):
        template = '{0.cargo} {0.name}'
        return template.format(self)
