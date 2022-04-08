from django.contrib import admin
from .models import Ciclo


@admin.register(Ciclo)
class CicloAdmin(admin.ModelAdmin):
    list_display = ('titulo', "url", 'indicador', 'criacao', 'atualizacao', 'ativo')

