from django.db import models

# Create your models here.

class Titulado(models.Model):

    name = models.CharField(max_length=254, null=True, blank=True,)
    título = models.CharField(max_length=254, null=True, blank=True,)
    elo = models.IntegerField(null=True, blank=True)



    def __str__(self):
        template = '{0.name} {0.título} {0.elo}'
        return template.format(self)