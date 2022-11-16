# Generated by Django 4.1.3 on 2022-11-16 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programa', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programa.centro_formacion', verbose_name='Centro de Formacion')),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ambiente', verbose_name='Ambiente')),
                ('fechas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.horario', verbose_name='Horario')),
                ('instructores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.instructor', verbose_name='Instructor')),
                ('municipios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.municipio', verbose_name='Municipio')),
                ('programas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programa.programa_formacion', verbose_name='Programa de Formacion')),
            ],
            options={
                'verbose_name': 'Agenda ',
                'verbose_name_plural': 'Agendas',
            },
        ),
    ]
