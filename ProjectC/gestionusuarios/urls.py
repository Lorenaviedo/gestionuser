# usuarios/urls.py
from django.urls import path, include
from .views import UsuarioView, home

urlpatterns = [
    path('home/', home, name="Users Home"),
    # /usuario/: maneja las operaciones GET y POST que obtienen la lista de usuarios o crean un nuevo usuario
    path('usuarios/', UsuarioView.as_view(), name='Listar Usuarios'),
    # /usuario/id/: maneja las operaciones GET, PUT, DELETE, las cuales obtienen, actualizan y eliminan un usuario específico según su ID
    path('usuarios/<int:id>/', UsuarioView.as_view(), name='User Detail by ID'),
]

