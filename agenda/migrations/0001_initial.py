# Generated by Django 4.1.3 on 2022-11-21 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        ('programa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_dias', models.SmallIntegerField(verbose_name='Cantidad de dias a Reservar')),
                ('fecha_Creacion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('fecha_Vencimiento', models.DateTimeField(blank=True, null=True, verbose_name='Valido Hasta')),
                ('instructores_f', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.instructor', verbose_name='Instructores')),
                ('programa_f', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programa.programa_formacion', verbose_name='Programa')),
            ],
            options={
                'verbose_name': 'Agenda ',
                'verbose_name_plural': 'Agendas',
            },
        ),
    ]
