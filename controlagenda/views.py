from django.db.models import Sum
from django.shortcuts import render, redirect
from .models import Agendamento
from .forms import AgendamentoForm, dateAgendamento
from django.contrib.auth.decorators import login_required
import datetime

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

@login_required()
def infoDashboard(request):
    agendamentosDone = Agendamento.objects.filter(isEncerrado='Sim').count()
    agendamentosDoing = Agendamento.objects.filter(isEncerrado='Não').count()
    contSla = Agendamento.objects.filter(isEncerrado='Não').exclude(encSla__isnull=True).count()
    latestAgs = Agendamento.objects.filter(isEncerrado='Não').order_by('-data')[: 4]

    return render(request, 'homepage.html', {'agentamentosdone': agendamentosDone, 'agendamentosdoing': agendamentosDoing, 'latestags': latestAgs, 'contslas': contSla})

@login_required()
def searchByDate(request):
    if 'q' in request.GET:
        q=request.GET['q']
        financeiro=Agendamento.objects.filter(data__exact=q)
        somaTotal= financeiro.aggregate(Sum('valor'))
    else:
        financeiro=Agendamento.objects.all()
        somaTotal = Agendamento.objects.aggregate(Sum('valor'))

    return render(request, 'relatorios.html', {'financeiro': financeiro, 'somatotal': somaTotal})

def relatSla(request):
     slaAtivos = Agendamento.objects.filter(isEncerrado='Não').exclude(encSla__isnull=True)

     return render(request, 'relatsla.html', {'slaativos': slaAtivos})