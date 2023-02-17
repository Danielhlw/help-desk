from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('novo_pedido/', views.novo_pedido, name="novo_pedido"),
]