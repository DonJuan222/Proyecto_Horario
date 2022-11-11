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

class tipo_Instructor(models.Model):
    tipo_Instructores=models.CharField(max_length=200,blank=False,null=False, verbose_name='Tipo de Instructor')
    id_Instructor=models.ForeignKey(instructor, on_delete=models.CASCADE,null=True,blank=True, verbose_name='Id de Instructor')
    
 
 
    class Meta:

        verbose_name='Tipo Instructor'
        verbose_name_plural='Tipo Instructores'


class programa_Formacion(models.Model):
    ficha= models.IntegerField(primary_key = True) 
    nombre_Programa=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del Programa')
    id_Horario=models.ForeignKey(horario, on_delete=models.CASCADE,null=True,blank=True, verbose_name='Id de Horario')
    id_Centro_Formacion=models.ForeignKey(centro_Formacion, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Id de Centro de Formacion')
    id_Tipo_Instructor=models.ForeignKey(tipo_Instructor, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Id del Tipo de Instructor')
    
    class Meta:

        verbose_name='Programa de Formacion'
        verbose_name_plural='Programas de Formacion'



class trimestre_uno(models.Model):
    nom_Trimestres_Uno=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del Trimestre')
    id_Programa_Formacion_Uno=models.ForeignKey(programa_Formacion, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Id Programa Formacion Uno')


    class Meta:
        verbose_name='Trimestre Uno'
        verbose_name_plural='Trimestres Uno'


    def __str__(self):
        return self.nom_Trimestres_Uno

        
class trimestre_dos(models.Model):
    nom_Trimestres_Dos=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del Trimestre')
    id_Programa_Formacion_Dos=models.ForeignKey(programa_Formacion, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Id Programa Formacion Dos')

    class Meta:
        verbose_name='Trimestre Dos'
        verbose_name_plural='Trimestres Dos'


    def __str__(self):
        return self.nom_Trimestres_Dos


        
class trimestre_tres(models.Model):
    nom_Trimestres_Tres=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del Trimestre')
    id_Programa_Formacion_Tres=models.ForeignKey(programa_Formacion, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Id Programa Formacion Tres')

    class Meta:
        verbose_name='Trimestre Tres'
        verbose_name_plural='Trimestres Tres'


    def __str__(self):
        return self.nom_Trimestres_Tres



        
class trimestre_cuatro(models.Model):
    nom_Trimestres_Cuatro=models.CharField(max_length=200,blank=False,null=False, verbose_name='Nombre del Trimestre')
    id_Programa_Formacion_Cuatro=models.ForeignKey(programa_Formacion, on_delete=models.CASCADE, null=True,blank=True, verbose_name='Id Programa Formacion Cuatro')

    class Meta:
        verbose_name='Trimestre Cuatro'
        verbose_name_plural='Trimestres Cuatro'


    def __str__(self):
        return self.nom_Trimestres_Cuatro

