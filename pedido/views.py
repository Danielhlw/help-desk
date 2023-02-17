from django.contrib.messages import constants
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pedido, Ticket
from django.contrib.auth.decorators import login_required

@login_required
def novo_pedido(request):
    if request.method == "GET":
        return render(request, 'novo_pedido.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
    
    pedido = Pedido(
        usuario=request.user,
        nome=nome
    )

    pedido.save()
    messages.add_message(request, constants.SUCCESS, 'Novo pet cadastrado')
