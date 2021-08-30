# una pagina web
from django.http import JsonResponse
from django.shortcuts import render

from jugadores.models import Jugador


def listar(request):
    jugadores = Jugador.objects.all()  # leer todos los datos desde la entidad producto
    context = {"jugadores": jugadores}
    return render(request, 'jugadores_template.html', context)



# devuelve un dato (web service, REST json)
def listar_dato(request):
    jugadores = list(Jugador.objects.all().values())
    return JsonResponse(jugadores, safe=False)

def listar_dato2(request):
    datos = {"columna":"hola","columna2":20}
    return JsonResponse(datos)
