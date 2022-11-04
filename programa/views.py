from django.shortcuts import render
from .models import programa_Formacion


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