from django.shortcuts import render, get_object_or_404
from programa.models import  programa_Formacion



# Create your views here.
def more_Agenda(request, agenda_id):
    agendas=get_object_or_404(programa_Formacion, id=agenda_id)
    agendas=programa_Formacion.objects.filter(id=agenda_id).order_by('id')
    return render(request, 'mostrarAgenda.html',{
        'agendas':agendas
    })
    


# def createAgenda(request):
#     if request.method == 'GET':
#         return render(request, 'createAgenda.html',{
#         'form': FormAgenda
#     })
#     else:
#         try:
#             form=FormAgenda(request.POST)
#             new_Agenda=form.save(commit=False)
#             new_Agenda.save()
#             return redirect('agenda')

#         except ValueError:
#             return render (request, 'createAgenda.html',{
#                 'form': FormAgenda,
#                 'error': 'Por favor proporciona los datos'
#             })

# def editarAgenda(request, agenda_id):
#     agendas=get_object_or_404(agenda, id=agenda_id)

#     data={
#         'form': FormAgenda(instance=agendas)
#     }

#     if request.method== 'POST':
#         formulario=FormAgenda(data=request.POST, instance=agendas, files=request.FILES)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect('mostrar_Agenda')
#         data['form']=formulario    
#     return render(request, 'actualizarAgenda.html', data)

# def eliminarAgenda(request, agenda_id):
#     agendas=get_object_or_404(agendas, id=agenda_id)
#     agendas.delete()
#     return redirect('mostrar_Agenda')