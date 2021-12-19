from django.urls import path
from .views import *

urlpatterns = [
    path('listar', listar_investimentos, name='listar_investimentos'),
    path('cadastrar', cadastrar_investimentos, name='cadastrar_investimentos'),
    path('listar/<int:id>',listar_investimento_id, name='listar_investimento_id'),
    path('editar/<int:id>',editar_investimento, name='editar_investimento'),
    path('remover/<int:id>',remover_investimento, name='remover_investimento')
]