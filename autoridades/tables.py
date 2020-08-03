import django_tables2 as tables
from .models import Autoridad

class AutoridadTable(tables.Table):
    class Meta:
        model = Autoridad
        exclude = ('id',)