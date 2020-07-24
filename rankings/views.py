from django.shortcuts import render
from .models import Player
from django.views.generic import ListView

class PlayerListView(ListView):
    model = Player
    template_name = 'rankings.html'

    def player_list(request):
        player_list = Player.objects.all()

        context = {
        'player_list' : player_list
        }
        return render(request, 'rankings.html', context)

    def order_by_ranking(request):
       players_descending = player_list.objects.order_by(ranking)