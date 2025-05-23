import base64
from django.shortcuts import render, redirect, get_object_or_404
from .models import Quarto, Paciente, Acompanhante
from .forms import QuartoForm, PacienteForm, AcompanhanteForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import os
import logging
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'master' and password == '5&0$Safira':
            # Autenticação bem-sucedida, redirecionar para o menu principal
            return redirect('menu_principal')
        else:
            # Falha na autenticação, exibir mensagem de erro
            messages.error(request, 'Usuário ou senha incorretos.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def listar_presentes(request):
    pacientes_na_casa = Paciente.objects.filter(data_saida__isnull=True)
    return render(request, 'listar_presentes.html', {'pacientes_na_casa': pacientes_na_casa})

logger = logging.getLogger(__name__)

def gerar_termo(request):
    pacientes = Paciente.objects.all()
    acompanhantes = Acompanhante.objects.all()
    print(f"Método da requisição: {request.method}")

    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        acompanhante_id = request.POST.get('acompanhante')

        try:
            paciente = Paciente.objects.get(pk=paciente_id)
            acompanhante = Acompanhante.objects.get(pk=acompanhante_id)
        except ObjectDoesNotExist:
            logger.error(
                f"Paciente ou Acompanhante não encontrado: paciente_id={paciente_id}, acompanhante_id={acompanhante_id}")
            return HttpResponse("Paciente ou Acompanhante não encontrado.", status=404)

        try:
            image_path = os.path.join(settings.BASE_DIR, 'safira', 'img', 'img7.png')
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            logo_base64 = f"data:image/png;base64,{encoded_string}"
        except FileNotFoundError:
            logger.error(f"Arquivo de imagem não encontrado: {image_path}")
            logo_base64 = None

        template_path = 'termo_adesao.html'
        context = {'paciente': paciente, 'acompanhante': acompanhante, 'logo': logo_base64}
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="termo_adesao.pdf"'

        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            logger.error(f"Erro ao gerar PDF: {pisa_status.err}")
            return HttpResponse('Erro ao gerar PDF', status=500)
        return response

    else:
        print(f"Número de pacientes: {pacientes.count()}")
        print(f"Número de acompanhantes: {acompanhantes.count()}")
        return render(request, 'selecionar_pessoas.html', {'pacientes': pacientes, 'acompanhantes': acompanhantes})

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