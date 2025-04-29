from django.urls import path
from . import views

urlpatterns = [
    path('menu', views.menu_principal, name='menu_principal'),
    path('login/', views.login, name='login'),

    path('quartos/', views.listar_quartos, name='listar_quartos'),
    path('quartos/criar/', views.criar_quarto, name='criar_quarto'),
    path('quartos/editar/<int:pk>/', views.editar_quarto, name='editar_quarto'),
    path('quartos/excluir/<int:pk>/', views.excluir_quarto, name='excluir_quarto'),

    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pacientes/criar/', views.criar_paciente, name='criar_paciente'),
    path('pacientes/editar/<int:pk>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/excluir/<int:pk>/', views.excluir_paciente, name='excluir_paciente'),

    path('acompanhantes/', views.listar_acompanhantes, name='listar_acompanhantes'),
    path('acompanhantes/criar/', views.criar_acompanhante, name='criar_acompanhante'),
    path('acompanhantes/editar/<int:pk>/', views.editar_acompanhante, name='editar_acompanhante'),
    path('acompanhantes/excluir/<int:pk>/', views.excluir_acompanhante, name='excluir_acompanhante'),
    path('gerar_termo/', views.gerar_termo, name='gerar_termo'),
    path('presentes/', views.listar_presentes, name='listar_presentes'),

]