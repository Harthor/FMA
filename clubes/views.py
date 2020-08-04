from django.shortcuts import render
from .models import Club
from django.views.generic import ListView

class ClubListView(ListView):
    model = Club
    template_name = 'clubes.html'
