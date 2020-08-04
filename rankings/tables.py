import django_tables2 as tables
from .models import Player

class PlayerTable(tables.Table):
    class Meta:
        model = Player
        exclude = ('id',)