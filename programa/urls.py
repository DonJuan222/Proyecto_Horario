from django.urls import path
from . import views

urlpatterns = [
    path('programa/', views.programa_formacion, name='programa'),
    # path('trimestre/<int:programa_id>/', views.programa_formacion, name='programa'),
    path('', views.home, name='home'),
]
