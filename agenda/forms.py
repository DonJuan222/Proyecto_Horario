from django.forms import ModelForm
from .models import *


class FormAgenda(ModelForm):
    class Meta:
        model = agenda
        fields ='__all__'