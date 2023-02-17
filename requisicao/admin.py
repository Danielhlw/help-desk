from django.contrib import admin

from .models import Requisicao, Ticket, Pedido

admin.site.register(Requisicao)
admin.site.register(Ticket)
admin.site.register(Pedido)