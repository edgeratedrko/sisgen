# Generated by Django 3.0.7 on 2021-12-06 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controluser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Administrador'),
        ),
    ]