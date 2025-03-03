from django.contrib import admin
from .models import Usuario  # Solo importa el modelo, no lo redefinas

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active')
