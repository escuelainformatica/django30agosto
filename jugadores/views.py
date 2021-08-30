from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

# Create your views here.
from jugadores.models import Jugador
from jugadores.models import Equipo

# import vistas.EquipoVista
from jugadores.vistas.EquipoVista import EquipoVista
from jugadores.vistas.jugadorvista import listar,listar_dato,listar_dato2



