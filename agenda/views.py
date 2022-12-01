from django.shortcuts import render, get_object_or_404, redirect
from programa.models import  programa_Formacion
from .models import agenda, integracion
from .forms import FormHorario, FormIntegracion
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def more_Agenda(request, agenda_id):
    agendas=get_object_or_404(programa_Formacion, id=agenda_id)
    agendas=programa_Formacion.objects.filter(id=agenda_id).order_by('id')
    return render(request, 'mostrarAgenda.html',{
        'agendas':agendas
    })
    
@login_required
def mostrarHorario(request):
    horarios=agenda.objects.all()

    return render(request, 'mostrarHorario.html',
    {'horarios': horarios })

@login_required
def createHorario(request):
    if request.method == 'GET':
        return render(request, 'createAgenda.html',{
        'form': FormHorario
    })
    else:
        try:
            form=FormHorario(request.POST)
            new_Horario=form.save(commit=False)
            new_Horario.save()
            return redirect('horario')

        except ValueError:
            return render (request, 'createAgenda.html',{
                'form': FormHorario,
                'error': 'Por favor proporciona los datos'
            })

@login_required
def editarHorario(request, horario_id):
    horario=get_object_or_404(agenda, id=horario_id)

    data={
        'form': FormHorario(instance=horario)
    }

    if request.method== 'POST':
        formulario=FormHorario(data=request.POST, instance=horario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('horario')
        data['form']=formulario    
    return render(request, 'actualizarAgenda.html', data)

@login_required
def eliminarHorario(request, horario_id):
    horario=get_object_or_404(agenda, id=horario_id)
    horario.delete()
    return redirect('horario')


@login_required
def mostrarAsignar(request):
    asignar=integracion.objects.all()

    return render(request, 'asignar/mostrarAsignar.html',
    {'asignar': asignar })

@login_required
def createAsignar(request):
    if request.method == 'GET':
        return render(request, 'asignar/createAsignar.html',{
        'form': FormIntegracion
    })
    else:
        try:
            form=FormIntegracion(request.POST)
            new_asignar=form.save(commit=False)
            new_asignar.save()
            return redirect('asignar')

        except ValueError:
            return render (request, 'asignar/createAsignar.html',{
                'form': FormIntegracion,
                'error': 'Por favor proporciona los datos'
            })

@login_required
def editarAsignar(request, asignar_id):
    asignar=get_object_or_404(integracion, id=asignar_id)

    data={
        'form': FormIntegracion(instance=asignar)
    }

    if request.method== 'POST':
        formulario=FormIntegracion(data=request.POST, instance=asignar, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('asignar')
        data['form']=formulario    
    return render(request, 'asignar/actualizarAsignar.html', data)

@login_required
def eliminarAsignar(request, asignar_id):
    asignar=get_object_or_404(integracion, id=asignar_id)
    asignar.delete()
    return redirect('asignar')
