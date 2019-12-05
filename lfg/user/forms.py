from django import forms
from .choices import plataforma_choices,jogo_choices,vagas_choices
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'senha']
        widgets = {
            'username': forms.TextInput(),
            'email': forms.TextInput(),
            'senha': forms.PasswordInput()
        }
    erros_messages = {
        'username':{
            'required': 'Este campo é obrigatorio'
        }
        'email':{
            'required': 'Insira um email valido'
        }
        'password':{
            'required': 'este campo é obrigatorio'
        }
    }