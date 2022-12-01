from django.urls import path
from . import views
    
urlpatterns = [
    path('agenda/<int:agenda_id>/', views.more_Agenda, name='more_Agenda'),

    path('horario/', views.mostrarHorario, name='mostrarHorario'),
    path('horario/create/', views.createHorario, name='createHorario'),
    path('editar/horario/<int:horario_id>/', views.editarHorario, name='editarHorario'),
    path('eliminar/horario/<int:horario_id>/', views.eliminarHorario, name='eliminarHorario'),

    path('asignar/', views.mostrarAsignar, name='asignar'),
    path('asignar/create/', views.createAsignar, name='createAsignar'),
    path('editar/asignar/<int:asignar_id>/', views.editarAsignar, name='editarAsignar'),
    path('eliminar/asignar/<int:asignar_id>/', views.eliminarAsignar, name='eliminarAsignar'),

]
