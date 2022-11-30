from django.urls import path
from . import views

urlpatterns = [
    path('programa/', views.mostrar_programa_formacion, name='programa'),
    path('programa/create/', views.create_Programa, name='createPrograma'),
    path('editar/<int:programa_id>/', views.editarPrograma, name='editarPrograma'),
    path('eliminar/<int:programa_id>/', views.eliminarPrograma, name='eliminarPrograma'),
    path('instructores/', views.mostrar_Instructores, name='instructores'),
    path('instructores/create/', views.create_Instructor, name='createInstructor'),
    path('editar/instructor/<int:instructor_id>/', views.editarInstructor, name='editarInstructor'),
    path('eliminar/instructor/<int:instructor_id>/', views.eliminarInstructor, name='eliminarInstructor'),
]

  