# from django.db import models
from home.models import municipio
from home.models import ambiente
from home.models import instructor
from programa.models import centro_Formacion
from programa.models import programa_Formacion


# # Create your models here.


# class horario(models.Model):
#     programas=models.ForeignKey(programa_Formacion, on_delete=models.CASCADE,null=False,blank=False, verbose_name='Programa de Formacion')
#     municipios=models.ForeignKey(municipio, on_delete=models.CASCADE, null=False,blank=False, verbose_name='Municipio')
#     ambiente=models.ForeignKey(ambiente, on_delete=models.CASCADE, null=False,blank=False, verbose_name='Ambiente')
#     Centro=models.ForeignKey(centro_Formacion, on_delete=models.CASCADE, null=False,blank=False, verbose_name='Centro de Formacion')
#     instructores=models.ForeignKey(instructor, on_delete=models.CASCADE, null=False,blank=False, verbose_name='Instructor')
    
#     class Meta:

#         verbose_name='Agenda '
#         verbose_name_plural='Agendas'
