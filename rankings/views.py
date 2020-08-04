from django.shortcuts import render
from .models import Player
from django.views.generic import ListView
from .tables import PlayerTable


def player_list(request):
        
        table= PlayerTable(Player.objects.all())

        
        return render(request, 'rankings.html', {
            "table": table
            })

