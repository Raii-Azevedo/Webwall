from django.contrib import admin
from .models import Ciclo


@admin.register(Ciclo)
class CicloAdmin(admin.ModelAdmin):
    list_display = ('criacao', 'atualizacao', 'data_atual', 'tipo_kmep_id', 'tkm_d', 'parada_d','kmep_d','tkm_acum','parada_acum', 'kmep_acum')

