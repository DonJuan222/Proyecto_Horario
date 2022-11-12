from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Q
from .models import programa_Formacion
from .filters import filtrarTrimestre
from .forms import FormAmbiente,FormCentro,FormMunicipio,FormPrograma


# def programa_formacion(request, programa_id):
#     programa=get_object_or_404(programa_Formacion, pk=programa_id)
#     return render(request, 'programa_f.html',{
#         'programa': programa
#     })

def mostrar_programa_formacion(request):
    busqueda=request.POST.get("buscar")
    programa = programa_Formacion.objects.all()

    if busqueda:
        programa=programa_Formacion.objects.filter(
            Q(ficha__icontains = busqueda)|
            Q(nombre_Programa__icontains = busqueda)|
            Q(trimestre__icontains = busqueda)
        ).distinct()

    return render(request, 'programa_f.html',
    {'programa': programa} )


def filtrar_programa_formacion(request):
    filtro=filtrarTrimestre(request.GET, queryset=programa_Formacion.objects.all())
    return render(request, 'programa_f.html',
    {'filtro':filtro} )


def create_Programa(request):
    if request.method == 'GET':
        return render(request, 'createPrograma.html',{
        'form': FormPrograma
    })
    else:
        try:
            form=FormPrograma(request.POST)
            new_programa=form.save(commit=False)
            new_programa.save()
            return redirect('programa')

        except ValueError:
            return render (request, 'createPrograma.html',{
                'form': FormPrograma,
                'error': 'Por favor proporciona los datos'
            })

def editarPrograma(request, programa_id):
    programa=get_object_or_404(programa_Formacion, id=programa_id)

    data={
        'form': FormPrograma(instance=programa)
    }

    if request.method== 'POST':
        formulario=FormPrograma(data=request.POST, instance=programa, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('programa')
        data['form']=formulario    
    return render(request, 'programaUpdate.html', data)

def eliminarPrograma(request, programa_id):
    programa=get_object_or_404(programa_Formacion, id=programa_id)
    programa.delete()
    return redirect('programa')