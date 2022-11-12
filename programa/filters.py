import django_filters

from .models import programa_Formacion

class filtrarTrimestre(django_filters.FilterSet):
    class Meta:
        model = programa_Formacion
        fields = {'nombre_Programa'}