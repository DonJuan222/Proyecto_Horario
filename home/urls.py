from django.urls import path
from . import views
    
urlpatterns = [
    path('login/', views.ingresar, name='login'),
    path('signup/', views.signup, name='signup'),
   
    path('logout/', views.cerrarSesion, name='logout'),


]

 # path('trimestre/', views.trimestr, name='trimestre'),