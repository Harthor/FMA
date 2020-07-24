from django.shortcuts import render

from .models import Autoridad
from django.views.generic import ListView

class AutoridadListView(ListView):
    model = Autoridad
    template_name = 'autoridades.html'