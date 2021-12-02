# Generated by Django 3.0.7 on 2021-11-29 17:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('login', models.CharField(default='', max_length=30, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=120)),
                ('telefone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('cargo', models.CharField(max_length=120)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
