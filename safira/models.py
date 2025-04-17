from django.db import models

class Quarto(models.Model):
    numero = models.IntegerField(unique=True, verbose_name="Número do Quarto")
    capacidade_camas = models.IntegerField(verbose_name="Número de Camas")
    localizacao_choices = [
        ('superior', 'Superior'),
        ('inferior', 'Inferior'),
    ]
    localizacao = models.CharField(
        max_length=10,
        choices=localizacao_choices,
        verbose_name="Localização na Casa"
    )

    def __str__(self):
        return f"Quarto {self.numero} ({self.localizacao})"

class Paciente(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Paciente")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    rg = models.CharField(max_length=20, unique=True, verbose_name="RG")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    cidade = models.CharField(max_length=50, verbose_name="Cidade")
    estado = models.CharField(max_length=2, verbose_name="Estado")
    data_entrada = models.DateField(verbose_name="Data de Entrada")
    data_saida = models.DateField(null=True, blank=True, verbose_name="Data de Saída")
    hospital_tratamento = models.CharField(max_length=100, verbose_name="Hospital de Tratamento")
    quarto = models.ForeignKey(Quarto, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Quarto")
    acompanhante = models.ForeignKey('Acompanhante', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Acompanhante")

    def __str__(self):
        return self.nome

class Acompanhante(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Acompanhante")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    rg = models.CharField(max_length=20, unique=True, verbose_name="RG")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    cidade = models.CharField(max_length=50, verbose_name="Cidade")
    estado = models.CharField(max_length=2, verbose_name="Estado")

    def __str__(self):
        return self.nome