from django.db import models
from django.contrib.auth.models import User

class Requisicao(models.Model):
    requisicao = models.CharField(max_length=100)

    def __str__(self):
        return self.requisicao

class Ticket(models.Model):
    ticket = models.CharField(max_length=200)

    def __str__(self):
        return self.ticket

class Pedido(models.Model):
    choices_status = (('P', 'Para resolver'), 
                      ('R', 'Resolvido'))
    
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100)
    departamento = models.CharField(max_length=50)
    descricao = models.TextField()
    tickets = models.ManyToManyField(Ticket)
    requisicao = models.ForeignKey(Requisicao, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=choices_status, default='P')

    def __str__(self):
        return self.nome