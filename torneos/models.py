from django.db import models

# Create your models here.

class Torneo(models.Model):

    name = models.CharField(max_length=254, null=True, blank=True,)
    fecha = models.DateTimeField()
   



    def __str__(self):
        template = '{0.name} {0.fecha}'
        return template.format(self)