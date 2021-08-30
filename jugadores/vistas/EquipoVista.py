from django.views import View
from django.shortcuts import render
from jugadores.models import Equipo


class EquipoVista(View):
    def get(self,request):
        equipos = Equipo.objects.all()  # leer todos los datos desde la entidad producto
        context = {"equipos": equipos}
        return render(request, 'equipos_template.html', context)
