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
    DIAS_LUNES="L"
    DIAS_MARTES="M"
    DIAS_MIERCOLES="I"
    DIAS_JUEVES="J"
    DIAS_VIERNES="V"
    DIAS_SABADO="S"

    DIAS_CHOISES=[
        (DIAS_LUNES, "Lunes"),
        (DIAS_MARTES, "Martes"),
        (DIAS_MIERCOLES, "Miercoles"),
        (DIAS_JUEVES, "Jueves"),
        (DIAS_VIERNES, "Viernes"),
        (DIAS_SABADO, "Sabado"),

    ]
    instructores_f=models.ForeignKey(instructor, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Instructores')
    dias_s=models.CharField(max_length=1, choices=DIAS_CHOISES, null=True, blank=True)
    
    def __str__(self):
     return self.dias_s
    
    class Meta:
        verbose_name='Integracion '
        verbose_name_plural='Integraciones'

    

class agenda(models.Model):
    hora_Inicio= models.TimeField(null=True,blank=True, verbose_name='Hora de Inicio')
    hora_Fin= models.TimeField(null=True,blank=True, verbose_name='Hora fin')
    fecha_Creacion = models.DateTimeField(null=True,blank=True, verbose_name='Fecha de Creacion')
    fecha_Vencimiento = models.DateTimeField(null=True,blank=True,verbose_name='Valido Hasta')
    dia_lunes=models.ForeignKey(integracion,related_name="Di_Lunes", on_delete=models.CASCADE, null=True,blank=True, verbose_name='Asignar Dia ')
    dia_martes=models.ForeignKey(integracion,related_name="Di_Martes", on_delete=models.CASCADE, null=True,blank=True, verbose_name='Asignar Dia ')
    dia_miercoles=models.ForeignKey(integracion,related_name="Di_Miercoles", on_delete=models.CASCADE, null=True,blank=True, verbose_name='Asignar Dia ')
    dia_jueves=models.ForeignKey(integracion,related_name="Di_Jueves", on_delete=models.CASCADE, null=True,blank=True, verbose_name='Asignar Dia ')
    dia_viernes=models.ForeignKey(integracion,related_name="Di_Viernes", on_delete=models.CASCADE, null=True,blank=True, verbose_name='Asignar Dia ')
    dia_sabado=models.ForeignKey(integracion,related_name="Di_Sabado", on_delete=models.CASCADE, null=True,blank=True, verbose_name='Asignar Dia ')
    
    
    class Meta:

        verbose_name='Agenda '
        verbose_name_plural='Agendas'

  