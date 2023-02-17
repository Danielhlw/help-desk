from django.urls import path
from . import views

urlpatterns = [
    path('novo_pedido/', views.novo_pedido, name="novo_pedido"),
]