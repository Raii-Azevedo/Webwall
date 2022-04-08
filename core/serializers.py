from rest_framework import serializers
from .models import Ciclo


class CicloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciclo
        fields = (
            'id',
            'titulo',
            'url',
            'indicador',
            'criacao',
            'atualizacao',
            'ativo'
        )
