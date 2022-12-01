from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Q
from .models import programa_Formacion, instructor,centro_Formacion
from .forms import FormPrograma, FormInstructor, FormCentro
from django.core.paginator import Paginator
from django.http import Http404


def mostrar_programa_formacion(request):
    busqueda=request.POST.get("buscar")
    programa = programa_Formacion.objects.all()
    page=request.GET.get('page',1)
    try:
        paginator=Paginator(programa, 10)
        programa=paginator.page(page)
    except:
        raise Http404
    if busqueda:
        programa=programa_Formacion.objects.filter(
            Q(ficha__icontains = busqueda)|
            Q(nombre_Programa__icontains = busqueda)
           
        ).distinct()

    return render(request, 'programa/programa_f.html',
    {'programa': programa, 'paginator':paginator})

def create_Programa(request):
    if request.method == 'GET':
        return render(request, 'programa/createPrograma.html',{
        'form': FormPrograma
    })
    else:
        try:
            form=FormPrograma(request.POST)
            new_programa=form.save(commit=False)
            new_programa.save()
            return redirect('programa')

        except ValueError:
            return render (request, 'programa/createPrograma.html',{
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
    return render(request, 'programa/programaUpdate.html', data)

def eliminarPrograma(request, programa_id):
    programa=get_object_or_404(programa_Formacion, id=programa_id)
    programa.delete()
    return redirect('programa')


def mostrar_Instructores(request):
    busqueda=request.POST.get("buscar")
    instructores=instructor.objects.all()
    page=request.GET.get('page',1)
    try:
        paginator=Paginator(instructores, 10)
        instructores=paginator.page(page)
    except:
        raise Http404

    if busqueda:
        instructores=instructor.objects.filter(
            Q(nombre__icontains = busqueda)|
            Q(apellido__icontains = busqueda)

        ).distinct()

    return render(request, 'instructores/instructores.html',
    {'instructores': instructores,'paginator':paginator} )

def create_Instructor(request):
    if request.method == 'GET':
        return render(request, 'instructores/createInstructores.html',{
        'form': FormInstructor
    })
    else:
        try:
            form=FormInstructor(request.POST)
            new_Instructor=form.save(commit=False)
            new_Instructor.save()
            return redirect('instructores')

        except ValueError:
            return render (request, 'instructores/createInstructores.html',{
                'form': FormInstructor,
                'error': 'Por favor proporciona los datos'
            })

def editarInstructor(request, instructor_id):
    instructores=get_object_or_404(instructor, id=instructor_id)

    data={
        'form': FormInstructor(instance=instructores)
    }

    if request.method== 'POST':
        formulario=FormInstructor(data=request.POST, instance=instructores, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('instructores')
        data['form']=formulario    
    return render(request, 'instructores/actualizarInstructores.html', data)

def eliminarInstructor(request, instructor_id):
    instructores=get_object_or_404(instructor, id=instructor_id)
    instructores.delete()
    return redirect('instructores')

def mostrar_Centros(request):
    centros =centro_Formacion.objects.all()
    return render(request, 'centros/mostrarCentros.html',
    {'centros': centros})

def create_Centros(request):
    if request.method == 'GET':
        return render(request, 'centros/createCentros.html',{
        'form': FormCentro
    })
    else:
        try:
            form=FormCentro(request.POST)
            new_Centro=form.save(commit=False)
            new_Centro.save()
            return redirect('centros')

        except ValueError:
            return render (request, 'centros/createCentros.html',{
                'form': FormCentro,
                'error': 'Por favor proporciona los datos'
            })

def editarCentros(request, centros_id):
    centros=get_object_or_404(centro_Formacion, id=centros_id)
    data={
        'form': FormCentro(instance=centros)
    }
    if request.method== 'POST':
        formulario=FormCentro(data=request.POST, instance=centros, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('centros')
        data['form']=formulario    
    return render(request, 'centros/actualizarCentros.html', data)

def eliminarCentros(request, centros_id):
    instructores=get_object_or_404(centro_Formacion, id=centros_id)
    instructores.delete()
    return redirect('centros')
