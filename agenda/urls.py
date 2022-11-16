from django.urls import path
from . import views
    
urlpatterns = [
    path('agenda/', views.mostrar_Agenda, name='mostrar_Agenda'),
    path('agenda/create/', views.createAgenda, name='createAgenda'),
    path('editar/agenda/<int:agenda_id>/', views.editarAgenda, name='editarAgenda'),
    path('eliminar/agenda/<int:agenda_id>/', views.eliminarAgenda, name='eliminarAgenda'),
]
