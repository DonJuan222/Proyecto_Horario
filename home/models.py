from django.db import models

# Create your models here.

class trimestre(models.Model):
    nom_Trimestres=models.CharField(max_length=200,blank=False,null=False)

    class Meta:
        verbose_name='Trimestre'
        verbose_name_plural='Trimestres'
        ordering=['nom_Trimestres']

    def __str__(self):
        return self.nom_Trimestres