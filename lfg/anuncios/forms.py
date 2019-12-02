from django import forms
from .choices import plataforma_choices,jogo_choices,vagas_choices
from .models import Anuncio

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['titulo','plataforma','jogo', 'descricao', 'vagas', 'foto_principal']
        widgets = {
            'plataforma': forms.RadioSelect(choices=plataforma_choices),
            'jogo': forms.RadioSelect(choices=jogo_choices),
            'vagas': forms.RadioSelect(choices=vagas_choices)
        }