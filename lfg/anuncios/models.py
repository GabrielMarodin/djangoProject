from django.db import models

from datetime import datetime
from user.models import User
from .choices import jogo_choices, plataforma_choices, vagas_choices

class Anuncio(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=200)
    plataforma = models.CharField(max_length=200, choices=plataforma_choices)
    jogo = models.CharField(max_length=100, choices=jogo_choices)
    descricao = models.TextField()
    vagas = models.IntegerField(choices=vagas_choices)
    foto_principal = models.ImageField(upload_to='images/')
    publicado = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.titulo
        