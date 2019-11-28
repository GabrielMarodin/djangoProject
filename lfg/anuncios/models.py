from django.db import models

from datetime import datetime
from user.models import User

class Anuncio(models.Model):
    user = models.ForeignKey(user, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=200)
    plataforma = models.CharField(max_length=100)
    jogo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    vagas = models.IntegerField()
    foto_principal = models.ImageField('')
    publicado = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.titulo
        