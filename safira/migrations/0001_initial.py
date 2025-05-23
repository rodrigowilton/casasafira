# Generated by Django 5.2 on 2025-04-17 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanhante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Acompanhante')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('rg', models.CharField(max_length=20, unique=True, verbose_name='RG')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True, verbose_name='Número do Quarto')),
                ('capacidade_camas', models.IntegerField(verbose_name='Número de Camas')),
                ('localizacao', models.CharField(choices=[('superior', 'Superior'), ('inferior', 'Inferior')], max_length=10, verbose_name='Localização na Casa')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Paciente')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('rg', models.CharField(max_length=20, unique=True, verbose_name='RG')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('data_entrada', models.DateField(verbose_name='Data de Entrada')),
                ('data_saida', models.DateField(blank=True, null=True, verbose_name='Data de Saída')),
                ('hospital_tratamento', models.CharField(max_length=100, verbose_name='Hospital de Tratamento')),
                ('acompanhante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='safira.acompanhante', verbose_name='Acompanhante')),
                ('quarto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='safira.quarto', verbose_name='Quarto')),
            ],
        ),
    ]
