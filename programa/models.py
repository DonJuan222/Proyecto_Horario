from django.db import models
from home.models import municipio
from home.models import ambiente
from home.models import horario
from home.models import instructor



# Create your models here.

class centro_Formacion(models.Model):
   
    nombre_Centro=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del Centro')
    id_Municipio=models.ForeignKey(municipio, on_delete=models.CASCADE,null=True,blank=True, verbose_name='Id de Municipio')
    id_Ambiente=models.ForeignKey(ambiente, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Id de Ambiente')

 
    class Meta:

        verbose_name='Centro de formacion'
        verbose_name_plural='Centros de formacion'


class programa_Formacion(models.Model):

    ficha= models.IntegerField(blank=False,null=False, verbose_name='Ficha') 
    nombre_Programa=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del Programa')
    trimestre=models.CharField(max_length=200,blank=False,null=False, verbose_name='Trimestre')
    id_Horario=models.ForeignKey(horario, on_delete=models.CASCADE,null=True,blank=True, verbose_name='Id de Horario')
    id_Centro_Formacion=models.ForeignKey(centro_Formacion, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Id de Centro de Formacion')
    id_Instructor=models.ForeignKey(instructor, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Id del Instructor')
    
    class Meta:

        verbose_name='Programa de Formacion'
        verbose_name_plural='Programas de Formacion'
