from django.urls import path
from . import views
    
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.ingresar, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.cerrarSesion, name='logout'),


]

