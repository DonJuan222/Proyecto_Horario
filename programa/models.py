from django.db import models
from home.models import municipio,instructor,ambiente,sede,tipoPrograma
from agenda.models import agenda


# Create your models here.

class centro_Formacion(models.Model):
    nombre_Centro=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del Centro')
    id_Municipio=models.ForeignKey(municipio, on_delete=models.CASCADE,null=True,blank=True, verbose_name='Id de Municipio')
    id_Ambiente=models.ForeignKey(ambiente, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Id de Ambiente')
    sede=models.ForeignKey(sede, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Sede')

 
    class Meta:

        verbose_name='Centro de formacion'
        verbose_name_plural='Centros de formacion'

    def __str__(self):
        return self.nombre_Centro

class programa_Formacion(models.Model):

    ficha= models.IntegerField(blank=False,null=False, verbose_name='Ficha') 
    nombre_Programa=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del Programa')
    tipo_Pograma=models.ForeignKey(tipoPrograma,on_delete=models.CASCADE,max_length=200,blank=True,null=True, verbose_name='Tipo de Programa')
    jornada=models.CharField(max_length=200,blank=True,null=True, verbose_name='Jornada')
    id_Centro_Formacion=models.ForeignKey(centro_Formacion, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Id de Centro de Formacion')
    id_Instructor=models.ForeignKey(instructor, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Id del Instructor')
    agenda=models.ForeignKey(agenda, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Programa')
    class Meta:

        verbose_name='Programa de Formacion'
        verbose_name_plural='Programas de Formacion'

    def __str__(self):
        return self.nombre_Programa
