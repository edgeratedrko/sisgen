# Generated by Django 3.0.7 on 2021-11-25 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlagenda', '0004_auto_20200902_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='isEncerrado',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', max_length=3),
        ),
    ]