from django.urls import path
from . import views
    
urlpatterns = [
    
    path('', views.home, name='home'),
    path('login/', views.ingresar, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.cerrarSesion, name='logout'),

    path('ambiente/', views.mostrar_ambiente, name='ambiente'),
    path('ambiente/create/', views.create_Ambiente, name='createAmbiente'),
    path('editar/ambiente/<int:ambiente_id>/', views.editarAmbiente, name='editarAmbiente'),
    path('eliminar/ambiente/<int:ambiente_id>/', views.eliminarAmbiente, name='eliminarAmbiente'), 

    path('municipio/', views.mostrar_Municipio, name='municipio'),
    path('municipio/create/', views.create_Municipio, name='createMunicipio'),
    path('editar/municipio/<int:municipio_id>/', views.editarMunicipio, name='editarMunicipio'),
    path('eliminar/municipio/<int:municipio_id>/', views.eliminarMunicipio, name='eliminarMunicipio'),  

    path('tipo/', views.mostrar_Tipo, name='tipo'),
    path('tipo/create/', views.createTipo, name='createTipo'),
    path('editar/tipo/<int:tipo_id>/', views.editarTipo, name='editarTipo'),
    path('eliminar/tipo/<int:tipo_id>/', views.eliminarTipo, name='eliminarTipo'),

    path('sede/', views.mostrar_Sede, name='sede'),
    path('sede/create/', views.createSede, name='createSede'),
    path('editar/sede/<int:sede_id>/', views.editarSede, name='editarSede'),
    path('eliminar/sede/<int:sede_id>/', views.eliminarSede, name='eliminarSede'),

]

