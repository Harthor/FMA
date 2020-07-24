
from django.shortcuts import render

from .models import Torneo
from django.views.generic import ListView

class TorneoListView(ListView):
    model = Torneo
    template_name = 'torneos.html'