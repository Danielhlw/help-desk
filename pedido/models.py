#from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    pedido = models.CharField(max_length=50)

    def __str__(self):
        return self.pedido

class Ticket(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    pedido = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.usuario