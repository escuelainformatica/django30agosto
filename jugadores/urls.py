from django.urls import path

from jugadores import views

urlpatterns = [
    path('listado/',views.listar,name='listar'),
    path('listado/rest/',views.listar_dato,name='listar_dato'),
    path('equipo/listado/',views.EquipoVista.as_view(),name='listar_equipo'),
]