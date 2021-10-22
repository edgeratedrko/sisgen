from django.shortcuts import render, redirect
from .models import Agendamento
from .forms import AgendamentoForm
from django.contrib.auth.decorators import login_required

@login_required()
def listAgenda(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamentos.html', {'agendamentos': agendamentos})

@login_required()
def createAgendamento(request):
    form = AgendamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listAgenda')

    return render(request, 'cadastrar_agendamento.html', {'form': form})

@login_required()
def updateAgendamento(request, id):
    agendamento = Agendamento.objects.get(id=id)
    form = AgendamentoForm(request.POST or None, instance=agendamento)

    if form.is_valid():
        form.save()
        return redirect('listAgenda')

    return render(request, 'cadastrar_agendamento.html', {'form': form, 'agendamento': agendamento})

@login_required()
def deleteAgendamento(request, id):
    agendamento = Agendamento.objects.get(id=id)

    if request.method == 'POST':
        agendamento.delete()
        return redirect('listAgenda')

    return render(request, 'ag_delete_conf.html', {'agendamento': agendamento})