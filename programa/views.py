from django.shortcuts import render


def programa_formacion(request):
    return render(request, 'programa_f.html')