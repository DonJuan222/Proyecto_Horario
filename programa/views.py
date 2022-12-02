from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import programa_Formacion, instructor,centro_Formacion, tipoPrograma
from .forms import FormPrograma, FormInstructor, FormCentro, FormTipoPrograma
from django.core.paginator import Paginator
from django.http import Http404

@login_required
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

@login_required
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

@login_required
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

@login_required
def eliminarPrograma(request, programa_id):
    programa=get_object_or_404(programa_Formacion, id=programa_id)
    programa.delete()
    return redirect('programa')

@login_required
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

@login_required
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

@login_required
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

@login_required
def eliminarInstructor(request, instructor_id):
    instructores=get_object_or_404(instructor, id=instructor_id)
    instructores.delete()
    return redirect('instructores')

@login_required
def mostrar_Centros(request):
    centros =centro_Formacion.objects.all()
    return render(request, 'centros/mostrarCentros.html',
    {'centros': centros})

@login_required
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

@login_required
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

@login_required
def eliminarCentros(request, centros_id):
    instructores=get_object_or_404(centro_Formacion, id=centros_id)
    instructores.delete()
    return redirect('centros')

@login_required
def mostrarTipoPrograma(request):
    tipoprograma =tipoPrograma.objects.all()
    return render(request, 'tipoPrograma/mostrarTipoPrograma.html',
    {'tipoprograma': tipoprograma})

@login_required
def createTipoPrograma(request):
    if request.method == 'GET':
        return render(request, 'tipoPrograma/createTipoPrograma.html',{
        'form': FormTipoPrograma
    })
    else:
        try:
            form=FormTipoPrograma(request.POST)
            new_TipoPrograma=form.save(commit=False)
            new_TipoPrograma.save()
            return redirect('tipoprograma')

        except ValueError:
            return render (request, 'tipoPrograma/createTipoPrograma.html',{
                'form': FormTipoPrograma,
                'error': 'Por favor proporciona los datos'
            })

@login_required
def editarTipoPrograma(request, tipop_id):
    tipoprogama=get_object_or_404(tipoPrograma, id=tipop_id)
    data={
        'form': FormTipoPrograma(instance=tipoprogama)
    }
    if request.method== 'POST':
        formulario=FormTipoPrograma(data=request.POST, instance=tipoprogama, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('tipoprograma')
        data['form']=formulario    
    return render(request, 'tipoPrograma/actualizarTipoPrograma.html', data)
    
@login_required
def eliminarTipoPrograma(request, tipop_id):
    tipoprogama=get_object_or_404(tipoPrograma, id=tipop_id)
    tipoprogama.delete()
    return redirect('tipoprograma')
