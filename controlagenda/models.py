from django.db import models
from django.utils.translation import gettext_lazy as _

class Agendamento(models.Model):
    class PersonType(models.TextChoices):
        FISICA = 'PF', _('Pessoa Física')
        JURIDICA = 'PJ', _('Pessoa Jurídica')

    class YesOrNo(models.TextChoices):
        SIM = 'SIM', _('Sim')
        NAO = 'NÃO', _('Não')

    nome = models.CharField(max_length=40)
    endereco = models.CharField(max_length=120)
    loginCliente = models.CharField(max_length=20)
    senhaCliente = models.CharField(max_length=30)
    cadastradoPor = models.CharField(max_length=30)
    informServico = models.CharField(max_length=240)
    solucao = models.CharField(max_length=200, default='A inserir')
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    tipoPessoa = models.CharField(max_length=3,choices=PersonType.choices,default=PersonType.FISICA)
    isEncerrado = models.CharField(max_length=3,choices=YesOrNo.choices,default=YesOrNo.NAO)
    isReagendado = models.CharField(max_length=3,choices=YesOrNo.choices,default=YesOrNo.NAO)


    def __str__(self):
        return self.nome