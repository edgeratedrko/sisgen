from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome', 'endereco', 'data', 'loginCliente', 'senhaCliente', 'cadastradoPor', 'informServico', 'solucao', 'valor', 'encSla',
                  'tipoPessoa', 'isEncerrado', 'isReagendado']

class dateAgendamento(forms.ModelForm):
    datesearch = forms.DateField(label="Pesquisar por Data:",required=False)
    class Meta:
        model = Agendamento
        fields = ['datesearch']
