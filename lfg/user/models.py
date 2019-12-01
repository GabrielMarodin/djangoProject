from django.db import models
from datetime import datetime

class User(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    data_user = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.nome