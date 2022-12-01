from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from home.models import ambiente,municipio,tipoInstructor,sede
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import FormAmbiente, FormMunicipio, FormTipo, FormSede


# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/login')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Contraseña no coinciden'
        })


def cerrarSesion(request):
    logout(request)
    return redirect('/')


def ingresar(request):
    if request.method == 'GET':
        return render(request, 'ingresar.html', {
            'form': AuthenticationForm
        })

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'ingresar.html', {
            'form': AuthenticationForm,
            'error': 'El usuario o contraseña es incorrecta'
        })
        else:
            login(request, user)
            return redirect('/')


@login_required
def mostrar_ambiente(request):
    busqueda=request.POST.get("buscar")
    ambientes = ambiente.objects.all()
    page=request.GET.get('page',1)
    try:
        paginator=Paginator(ambientes, 10)
        ambientes=paginator.page(page)
    except:
        raise Http404
    if busqueda:
        ambientes=ambiente.objects.filter(
            Q(nom_ambiente__icontains = busqueda)
           
        ).distinct()

    return render(request, 'ambiente/mostrarAmbiente.html',
    {'ambientes': ambientes, 'paginator':paginator})

@login_required
def create_Ambiente(request):
    if request.method == 'GET':
        return render(request, 'ambiente/crearAmbiente.html',{
        'form': FormAmbiente
    })
    else:
        try:
            form=FormAmbiente(request.POST)
            new_ambiente=form.save(commit=False)
            new_ambiente.save()
            return redirect('ambiente')

        except ValueError:
            return render (request, 'ambiente/crearAmbiente.html',{
                'form': FormAmbiente,
                'error': 'Por favor proporciona los datos'
            })

@login_required
def editarAmbiente(request, ambiente_id):
    ambientes=get_object_or_404(ambiente, id=ambiente_id)

    data={
        'form': FormAmbiente(instance=ambientes)
    }

    if request.method== 'POST':
        formulario=FormAmbiente(data=request.POST, instance=ambientes, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('ambiente')
        data['form']=formulario    
    return render(request, 'ambiente/actualizarAmbiente.html', data)

@login_required
def eliminarAmbiente(request, ambiente_id):
    ambientes=get_object_or_404(ambiente, id=ambiente_id)
    ambientes.delete()
    return redirect('ambiente')

@login_required
def mostrar_Municipio(request):
    municipios = municipio.objects.all()

    return render(request, 'municipio/mostrarMunicipio.html',
    {'municipios': municipios})

@login_required
def create_Municipio(request):
    if request.method == 'GET':
        return render(request, 'municipio/crearMunicipio.html',{
        'form': FormMunicipio
    })
    else:
        try:
            form=FormMunicipio(request.POST)
            new_municipio=form.save(commit=False)
            new_municipio.save()
            return redirect('municipio')

        except ValueError:
            return render (request, 'municipio/crearMunicipio.html',{
                'form': FormMunicipio,
                'error': 'Por favor proporciona los datos'
            })

@login_required
def editarMunicipio(request, municipio_id):
    municipios=get_object_or_404(municipio, id=municipio_id)

    data={
        'form': FormMunicipio(instance=municipios)
    }

    if request.method== 'POST':
        formulario=FormMunicipio(data=request.POST, instance=municipios, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('municipio')
        data['form']=formulario    
    return render(request, 'municipio/actualizarMunucipio.html', data)

@login_required
def eliminarMunicipio(request, municipio_id):
    municipios=get_object_or_404(municipio, id=municipio_id)
    municipios.delete()
    return redirect('municipio')  


@login_required
def mostrar_Tipo(request):
    tipo=tipoInstructor.objects.all()

    return render(request, 'tipoinstructor/mostrarTipo.html',
    {'tipo': tipo })

@login_required
def createTipo(request):
    if request.method == 'GET':
        return render(request, 'tipoinstructor/createTipo.html',{
        'form': FormTipo
    })
    else:
        try:
            form=FormTipo(request.POST)
            new_Tipo=form.save(commit=False)
            new_Tipo.save()
            return redirect('tipo')

        except ValueError:
            return render (request, 'tipoinstructor/createTipo.html',{
                'form': FormTipo,
                'error': 'Por favor proporciona los datos'
            })

@login_required
def editarTipo(request, tipo_id):
    tipo=get_object_or_404(tipoInstructor, id=tipo_id)

    data={
        'form': FormTipo(instance=tipo)
    }

    if request.method== 'POST':
        formulario=FormTipo(data=request.POST, instance=tipo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('tipo')
        data['form']=formulario    
    return render(request, 'tipoinstructor/actualizarTipo.html', data)

@login_required
def eliminarTipo(request, tipo_id):
    instructores=get_object_or_404(tipoInstructor, id=tipo_id)
    instructores.delete()
    return redirect('tipo')

@login_required
def mostrar_Sede(request):
    sedes=sede.objects.all()

    return render(request, 'sede/mostrarSede.html',
    {'sedes': sedes })

@login_required
def createSede(request):
    if request.method == 'GET':
        return render(request, 'sede/createSede.html',{
        'form': FormSede
    })
    else:
        try:
            form=FormSede(request.POST)
            new_Sede=form.save(commit=False)
            new_Sede.save()
            return redirect('sede')

        except ValueError:
            return render (request, 'sede/createSede.html',{
                'form': FormSede,
                'error': 'Por favor proporciona los datos'
            })

@login_required
def editarSede(request, sede_id):
    sedes=get_object_or_404(sede, id=sede_id)

    data={
        'form': FormTipo(instance=sedes)
    }

    if request.method== 'POST':
        formulario=FormTipo(data=request.POST, instance=sedes, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('sede')
        data['form']=formulario    
    return render(request, 'sede/actualizarSede.html', data)

@login_required
def eliminarSede(request, sede_id):
    instructores=get_object_or_404(sede, id=sede_id)
    instructores.delete()
    return redirect('sede')