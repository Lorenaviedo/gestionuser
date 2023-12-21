# usuarios/urls.py
from django.urls import path, include
from .views import UsuarioView

urlpatterns = [
    path('user/', UsuarioView.as_view(), name='Listar Usuarios'),
    path('user/<int:id>/', UsuarioView.as_view(), name='User Detail by ID'),
]
