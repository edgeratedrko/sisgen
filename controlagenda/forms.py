from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome', 'endereco', 'loginCliente', 'senhaCliente', 'cadastradoPor', 'informServico', 'solucao', 'valor',
                  'tipoPessoa', 'isEncerrado', 'isReagendado']