from django.db import models

# Create your models here.

class trimestre(models.Model):
    nom_Trimestres=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del Trimestre')

    class Meta:
        verbose_name='Trimestre'
        verbose_name_plural='Trimestres'


    def __str__(self):
        return self.nom_Trimestres


class municipio(models.Model):
    nom_municipio=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del Municipio')

    class Meta:
        verbose_name='Municipio'
        verbose_name_plural='Municipios'
     

    def __str__(self):
        return self.nom_municipio

class ambiente(models.Model):
    nom_ambiente=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del ambiente ')

    class Meta:
        verbose_name='Ambiente'
        verbose_name_plural='Ambientes'
    

    def __str__(self):
        return self.nom_ambiente

class horario(models.Model):
    fecha_Inicio=models.DateField(null=False, verbose_name='Fecha de Inicio')
    fecha_Fin=models.DateField(null=False, verbose_name='Fecha Fin')
    hora_Inicio_Fin=models.CharField(max_length=200,blank=False,null=False, verbose_name='Hora de Inicio y Fin')
    dias_Semana=models.CharField(max_length=200,blank=False,null=False, verbose_name='Dias semana')

    class Meta:
        verbose_name='Horario'
        verbose_name_plural='Horarios'



class instructor(models.Model):
    nombre=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del Instructor')
    apellido=models.CharField(max_length=200,blank=False,null=False, verbose_name='Apellido de instructor')

    class Meta:
        verbose_name='Instructor'
        verbose_name_plural='Instructores'
        
