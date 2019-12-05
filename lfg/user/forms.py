from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'password': forms.PasswordInput()
        }
    erros_messages = {
        'username':{
            'required': 'Este campo é obrigatorio'
        },
        'email':{
            'required': 'Insira um email valido'
        },
        'password':{
            'required': 'este campo é obrigatorio'
        }
    }