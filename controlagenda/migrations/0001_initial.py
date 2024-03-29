# Generated by Django 3.0.7 on 2021-11-29 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('endereco', models.CharField(max_length=120)),
                ('data', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('loginCliente', models.CharField(max_length=20)),
                ('senhaCliente', models.CharField(max_length=30)),
                ('cadastradoPor', models.CharField(max_length=30)),
                ('informServico', models.CharField(max_length=240)),
                ('solucao', models.CharField(default='A inserir', max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipoPessoa', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], default='PF', max_length=3)),
                ('isEncerrado', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', max_length=3)),
                ('isReagendado', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', max_length=3)),
            ],
        ),
    ]
