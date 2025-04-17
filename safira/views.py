from django.shortcuts import render, redirect, get_object_or_404
from .models import Quarto, Paciente, Acompanhante
from .forms import QuartoForm, PacienteForm, AcompanhanteForm

def menu_principal(request):
    return render(request, 'menu_principal.html')

# Views para Quarto
def listar_quartos(request):
    quartos = Quarto.objects.all()
    return render(request, 'listar_quartos.html', {'quartos': quartos})

def criar_quarto(request):
    if request.method == 'POST':
        form = QuartoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_quartos')
    else:
        form = QuartoForm()
    return render(request, 'criar_quarto.html', {'form': form})

def editar_quarto(request, pk):
    quarto = get_object_or_404(Quarto, pk=pk)
    if request.method == 'POST':
        form = QuartoForm(request.POST, instance=quarto)
        if form.is_valid():
            form.save()
            return redirect('listar_quartos')
    else:
        form = QuartoForm(instance=quarto)
    return render(request, 'editar_quarto.html', {'form': form})

def excluir_quarto(request, pk):
    quarto = get_object_or_404(Quarto, pk=pk)
    if request.method == 'POST':
        quarto.delete()
        return redirect('listar_quartos')
    return render(request, 'excluir_quarto.html', {'quarto': quarto})

# Views para Paciente
def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'listar_pacientes.html', {'pacientes': pacientes})

def criar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'criar_paciente.html', {'form': form})

def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'editar_paciente.html', {'form': form})

def excluir_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('listar_pacientes')
    return render(request, 'excluir_paciente.html', {'paciente': paciente})

# Views para Acompanhante
def listar_acompanhantes(request):
    acompanhantes = Acompanhante.objects.all()
    return render(request, 'listar_acompanhantes.html', {'acompanhantes': acompanhantes})

def criar_acompanhante(request):
    if request.method == 'POST':
        form = AcompanhanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_acompanhantes')
    else:
        form = AcompanhanteForm()
    return render(request, 'criar_acompanhante.html', {'form': form})

def editar_acompanhante(request, pk):
    acompanhante = get_object_or_404(Acompanhante, pk=pk)
    if request.method == 'POST':
        form = AcompanhanteForm(request.POST, instance=acompanhante)
        if form.is_valid():
            form.save()
            return redirect('listar_acompanhantes')
    else:
        form = AcompanhanteForm(instance=acompanhante)
    return render(request, 'editar_acompanhante.html', {'form': form})

def excluir_acompanhante(request, pk):
    acompanhante = get_object_or_404(Acompanhante, pk=pk)
    if request.method == 'POST':
        acompanhante.delete()
        return redirect('listar_acompanhantes')
    return render(request, 'excluir_acompanhante.html', {'acompanhante': acompanhante})