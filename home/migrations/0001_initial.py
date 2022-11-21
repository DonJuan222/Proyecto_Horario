# Generated by Django 4.1.3 on 2022-11-19 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ambiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ambiente', models.CharField(max_length=200, verbose_name='Nombre del ambiente ')),
            ],
            options={
                'verbose_name': 'Ambiente',
                'verbose_name_plural': 'Ambientes',
            },
        ),
        migrations.CreateModel(
            name='municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_municipio', models.CharField(max_length=200, verbose_name='Nombre del Municipio')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
            },
        ),
        migrations.CreateModel(
            name='sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_Sede', models.CharField(max_length=200, verbose_name='Nombre de la Sede')),
            ],
            options={
                'verbose_name': 'Sede',
                'verbose_name_plural': 'Sedes',
            },
        ),
        migrations.CreateModel(
            name='tipoInstructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_Instructor', models.CharField(max_length=200, verbose_name='Tipo de instructor')),
            ],
            options={
                'verbose_name': 'Tipo de Instructor',
                'verbose_name_plural': 'Tipo de Instructor',
            },
        ),
        migrations.CreateModel(
            name='tipoPrograma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_Programa', models.CharField(max_length=200, verbose_name='Tipo de programa')),
            ],
            options={
                'verbose_name': 'Tipo de Programa',
                'verbose_name_plural': 'Tipos de Programa',
            },
        ),
        migrations.CreateModel(
            name='instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre del Instructor')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellido de instructor')),
                ('tipoInstructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.tipoinstructor', verbose_name='Tipo de Instructor')),
            ],
            options={
                'verbose_name': 'Instructor',
                'verbose_name_plural': 'Instructores',
            },
        ),
    ]
