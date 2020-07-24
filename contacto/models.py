from django.db import models

# Create your models here.

class Contacto(models.Model):

    name = models.CharField(max_length=254, null=True, blank=True,)
    número_telefónico = models.IntegerField(null=True, blank=True)



    def __str__(self):
        template = '{0.name} {0.número_telefónico}'
        return template.format(self)