from django.urls import path
from . import views
    
urlpatterns = [
    path('', views.ingresar, name='login'),
    path('signup/', views.signup, name='signup'),
    path('trimestre/', views.trimestr, name='trimestre'),
    path('logout/', views.cerrarSesion, name='logout'),


]