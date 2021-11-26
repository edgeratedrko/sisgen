from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date

class Agendamento(models.Model):

    STATUS = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )

    class PersonType(models.TextChoices):
        FISICA = 'PF', _('Pessoa Física')
        JURIDICA = 'PJ', _('Pessoa Jurídica')

    nome = models.CharField(max_length=40)
    endereco = models.CharField(max_length=120)
    data = models.DateField(_("Date"), default=date.today)
    loginCliente = models.CharField(max_length=20)
    senhaCliente = models.CharField(max_length=30)
    cadastradoPor = models.CharField(max_length=30)
    informServico = models.CharField(max_length=240)
    solucao = models.CharField(max_length=200, default='A inserir')
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    tipoPessoa = models.CharField(max_length=3,choices=PersonType.choices,default=PersonType.FISICA)
    isEncerrado = models.CharField(max_length=3,choices=STATUS, default='Não')
    isReagendado = models.CharField(max_length=3,choices=STATUS,default='Não')


    def __str__(self):
        return self.nome