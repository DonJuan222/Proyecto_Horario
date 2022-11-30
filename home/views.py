from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from home.models import ambiente,municipio,tipoInstructor,tipoPrograma,sede
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q
from .forms import FormAmbiente, FormMunicipio

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
                return redirect('/')
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



def mostrar_ambiente(request):
    busqueda=request.POST.get("buscar")
    ambientes = ambiente.objects.all()
    page=request.GET.get('page',1)
    try:
        paginator=Paginator(ambientes, 1)
        ambientes=paginator.page(page)
    except:
        raise Http404
    if busqueda:
        ambientes=ambiente.objects.filter(
            Q(nom_ambiente__icontains = busqueda)
           
        ).distinct()

    return render(request, 'ambiente/mostrarAmbiente.html',
    {'ambientes': ambientes, 'paginator':paginator})

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

def eliminarAmbiente(request, ambiente_id):
    ambientes=get_object_or_404(ambiente, id=ambiente_id)
    ambientes.delete()
    return redirect('ambiente')


def mostrar_Municipio(request):
    municipios = municipio.objects.all()

    return render(request, 'municipio/mostrarMunicipio.html',
    {'municipios': municipios})

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

def editarMunicipio(request, municipio_id):
    municipios=get_object_or_404(municipio, id=municipio_id)

    data={
        'form': FormMunicipio(instance=municipios)
    }

    if request.method== 'POST':
        formulario=FormAmbiente(data=request.POST, instance=municipio, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('municipio')
        data['form']=formulario    
    return render(request, 'municipio/actualizarMunicipio.html', data)

def eliminarMunicipio(request, municipio_id):
    municipios=get_object_or_404(ambiente, id=municipio_id)
    municipios.delete()
    return redirect('municipio')
