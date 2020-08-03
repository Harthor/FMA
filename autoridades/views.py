from django.shortcuts import render

from .models import Autoridad
from django.views.generic import ListView
from .tables import AutoridadTable

def autoridad_list(request):

    table = AutoridadTable(Autoridad.objects.all())

    return render(request, "autoridades.html", {
        "table": table
    })