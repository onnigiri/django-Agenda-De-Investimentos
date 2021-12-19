from django import forms
from .models import *
from .models import Investimento

class InvestimentoForm(forms.ModelForm):
    class Meta:
        model = Investimento
        fields = ['nome_investimento','valor','fonte','data','lucro_mensal','lucro_anual']