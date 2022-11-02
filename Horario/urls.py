from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('trimestre/', views.trimestr, name='trimestre'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('login/', views.ingresar, name='login')

]