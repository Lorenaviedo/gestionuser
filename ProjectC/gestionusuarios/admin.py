from django.contrib import admin
from .models import Usuario

# Registra el modelo Usuario
admin.site.register(Usuario)

#class UsuarioAdmin(admin.ModelAdmin):
#    list_display = ('id', 'nombre', 'email', 'edad')  # Personaliza los campos a mostrar en la lista
