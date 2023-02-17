from django.shortcuts import render
from django.http import HttpResponse

def novo_pedido(request):
    return HttpResponse('Estou no novo_pedido')