from django.urls import path
from . import views
    
urlpatterns = [
    
    path('', views.home, name='home'),
    path('login/', views.ingresar, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.cerrarSesion, name='logout'),

    path('ambiente/', views.mostrar_ambiente, name='ambiente'),
    path('ambiente/create/', views.create_Ambiente, name='createAmbiente'),
    path('editar/<int:ambiente_id>/', views.editarAmbiente, name='editarAmbiente'),
    path('eliminar/<int:ambiente_id>/', views.eliminarAmbiente, name='eliminarAmbiente'), 

     path('municipio/', views.mostrar_Municipio, name='municipio'),
    path('municipio/create/', views.create_Ambiente, name='createAmbiente'),
    path('editar/<int:municipio_id>/', views.editarMunicipio, name='editarMunicipio'),
    path('eliminar/<int:municipio_id>/', views.eliminarMunicipio, name='eliminarMunicipio'),  
]

