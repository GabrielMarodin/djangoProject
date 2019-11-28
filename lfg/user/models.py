from django.db import models
from datetime import datetime

class User(models.Model):
    anuncio = models.CharField(max_length=200)
    anuncio_id = models.IntegerField()
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    fone = models.CharField(max_length=20)
    mensagem = models.TextField(blank=True)
    data_user = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.nome