from datetime import timedelta
from django.db import models
from home.models import instructor
from programa.models import programa_Formacion


# Create your models here.


class agenda(models.Model):
    cantidad_dias=models.SmallIntegerField(verbose_name='Cantidad de dias a Reservar', )
    fecha_Creacion = models.DateTimeField(null=True,blank=True, verbose_name='Fecha de Creacion')
    fecha_Vencimiento = models.DateTimeField(null=True,blank=True,verbose_name='Valido Hasta')
    programa_f=models.ForeignKey(programa_Formacion, on_delete=models.CASCADE, null=False,blank=False, verbose_name='Programa')
    instructores_f=models.ForeignKey(instructor, on_delete=models.CASCADE, null=False,blank=False, verbose_name='Instructores')
    
    class Meta:

        verbose_name='Agenda '
        verbose_name_plural='Agendas'
    


    def save(self, *args, **kwargs):
        self.fecha_Vencimiento = self.fecha_Creacion + timedelta(days=self.cantidad_dias)
        super().save(*args, **kwargs)