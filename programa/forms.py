from django.forms import ModelForm
from .models import *



class FormPrograma(ModelForm):
    class Meta:
        model = programa_Formacion
        fields ='__all__'

class FormCentro(ModelForm):
    class Meta:
        model = centro_Formacion
        fields ='__all__'

class FormInstructor(ModelForm):
    class Meta:
        model = instructor
        fields ='__all__'



