from django.forms import ModelForm
from .models import *



class FormHorario(ModelForm):
    class Meta:
        model = agenda
        fields ='__all__'

class FormIntegracion(ModelForm):
    class Meta:
        model = integracion
        fields ='__all__'