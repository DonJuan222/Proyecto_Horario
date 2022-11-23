from datetime import timedelta
from django.db import models
from home.models import instructor



# Create your models here.

class dias(models.Model):
    dias_Semana=models.CharField(max_length=200,blank=True,null=True, verbose_name='Dias')
    
    class Meta:

        verbose_name='Dia '
        verbose_name_plural='Dias'

    def __str__(self):
     return self.dias_Semana

class integracion(models.Model):
    instructores_f=models.ForeignKey(instructor, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Instructores')
    dias_Semana=models.ForeignKey(dias, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Dias')
    
    class Meta:
        verbose_name='Integracion '
        verbose_name_plural='Integraciones'
 

class agenda(models.Model):
    hora_Inicio= models.TimeField(null=True,blank=True, verbose_name='Hora de Inicio')
    hora_Fin= models.TimeField(null=True,blank=True, verbose_name='Hora fin')
    fecha_Creacion = models.DateTimeField(null=True,blank=True, verbose_name='Fecha de Creacion')
    fecha_Vencimiento = models.DateTimeField(null=True,blank=True,verbose_name='Valido Hasta')
    asignacion=models.ForeignKey(integracion, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Asignar Dia')
    
    class Meta:

        verbose_name='Agenda '
        verbose_name_plural='Agendas'

  