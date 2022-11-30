from django.forms import ModelForm
from .models import *



class FormAmbiente(ModelForm):
    class Meta:
        model = ambiente
        fields ='__all__'

class FormMunicipio(ModelForm):
    class Meta:
        model = municipio
        fields ='__all__'

        