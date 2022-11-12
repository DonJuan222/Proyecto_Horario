from django.urls import path
from . import views

urlpatterns = [
    path('programa/', views.mostrar_programa_formacion, name='programa'),
    path('programa/create/', views.create_Programa, name='createPrograma'),
    path('editar/<int:programa_id>/', views.editarPrograma, name='editarPrograma'),
        path('eliminar/<int:programa_id>/', views.eliminarPrograma, name='eliminarPrograma'),
    path('filtrar/', views.filtrar_programa_formacion, name='filtro'),
 
]

   # path('trimestre/<int:programa_id>/', views.programa_formacion, name='programa'),
    # path('', views.home, name='home'),