from django.db import models
from datetime import datetime

class User(models.Model):
    username = models.CharField(max_length=200)
    id = models.IntegerField(primary_key='true')
    email = models.EmailField()
    password = models.CharField
    data_user = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.username