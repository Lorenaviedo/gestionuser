from django.contrib import admin
from .models import Usuario

# Register your models here.
#class UsuarioAdmin(admin.ModelAdmin):
#    list_display = ('id', 'nombre', 'email', 'edad')  # Personaliza los campos a mostrar en la lista

# Registra el modelo Usuario con la clase UsuarioAdmin
admin.site.register(Usuario)
