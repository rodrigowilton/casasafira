from django import forms
from .models import Quarto, Paciente, Acompanhante

class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields = '__all__'

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'rg', 'cpf', 'endereco', 'cidade', 'estado', 'data_entrada', 'data_saida', 'hospital_tratamento', 'quarto', 'acompanhante']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'data_entrada': forms.DateInput(attrs={'type': 'date'}),
            'data_saida': forms.DateInput(attrs={'type': 'date'}),
        }

class AcompanhanteForm(forms.ModelForm):
    class Meta:
        model = Acompanhante
        fields = ['nome', 'data_nascimento', 'rg', 'cpf', 'endereco', 'cidade', 'estado']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }