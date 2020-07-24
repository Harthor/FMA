from django.shortcuts import render

from .models import Titulado
from django.views.generic import ListView

class TituladoListView(ListView):
    model = Titulado
    template_name = 'rankings.html'