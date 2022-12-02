from django.db import models

# Create your models here.

class municipio(models.Model):
    nom_municipio=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del Municipio')

    class Meta:
        verbose_name='Municipio'
        verbose_name_plural='Municipios'
     

    def __str__(self):
        return self.nom_municipio

class sede(models.Model):
    nom_Sede=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre de la Sede')

    class Meta:
        verbose_name='Sede'
        verbose_name_plural='Sedes'
     

    def __str__(self):
        return self.nom_Sede

class ambiente(models.Model):
    nom_ambiente=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del ambiente ')

    class Meta:
        verbose_name='Ambiente'
        verbose_name_plural='Ambientes'
    

    def __str__(self):
        return self.nom_ambiente

class tipoInstructor(models.Model):
    tipo_Instructor=models.CharField(max_length=200,blank=False,null=False, verbose_name='Tipo de instructor')
    class Meta:
        verbose_name='Tipo de Instructor'
        verbose_name_plural='Tipo de Instructor'
    

    def __str__(self):
        return self.tipo_Instructor

class tipoPrograma(models.Model):
    tipo_Programa=models.CharField(max_length=200,blank=False,null=False, verbose_name='Tipo de programa')
    class Meta:
        verbose_name='Tipo de Programa'
        verbose_name_plural='Tipos de Programa'
    

    def __str__(self):
        return self.tipo_Programa


class instructor(models.Model):
    nombre=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del Instructor')
    apellido=models.CharField(max_length=200,blank=False,null=False, verbose_name='Apellido de instructor')
    tipoInstructor=models.ForeignKey(tipoInstructor, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Tipo de Instructor')

    class Meta:
        verbose_name='Instructor'
        verbose_name_plural='Instructores'
        
    def __str__(self):
        return self.nombre