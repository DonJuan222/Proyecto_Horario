from django.shortcuts import render
from .models import programa_Formacion,trimestre_uno,trimestre_dos,trimestre_tres,trimestre_cuatro


# def programa_formacion(request, programa_id):
#     programa=get_object_or_404(programa_Formacion, pk=programa_id)
#     return render(request, 'programa_f.html',{
#         'programa': programa
#     })

def programa_formacion(request):
    programa = programa_Formacion.objects.all()
    return render(request, 'programa_f.html', {
        'programa': programa
    })


def home(request):
    Trimestre_Uno = trimestre_uno.objects.all()
    Trimestre_Dos = trimestre_dos.objects.all()
    Trimestre_Tres = trimestre_tres.objects.all()
    Trimestre_Cuatro = trimestre_cuatro.objects.all()
    return render(request, 'home.html', {
        'Trimestre_Uno': Trimestre_Uno,
        'Trimestre_Dos': Trimestre_Dos,
        'Trimestre_Tres': Trimestre_Tres,
        'Trimestre_Cuatro': Trimestre_Cuatro,

    })