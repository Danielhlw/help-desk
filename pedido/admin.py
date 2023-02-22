from django.contrib import admin
from .models import Pedido, Ticket, Tag

admin.site.register(Pedido)
admin.site.register(Ticket)
admin.site.register(Tag)