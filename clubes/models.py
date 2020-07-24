from django.db import models

# Create your models here.

class Club(models.Model):

    name = models.CharField(max_length=254, null=True, blank=True,)
    jugadores = models.IntegerField(blank=True, null=True)
    dirección = models.CharField(max_length=254, null=True, blank=True,)



    def __str__(self):
        template = '{0.name} {0.jugadores} {0.dirección}'
        return template.format(self)