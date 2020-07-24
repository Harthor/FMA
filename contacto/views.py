
from django.shortcuts import render

from .models import Contacto
from django.views.generic import ListView

class ContactoListView(ListView):
    model = Contacto
    template_name = 'contacto.html'