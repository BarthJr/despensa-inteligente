from rest_framework import serializers

from core.models import Categoria, Medida


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome')


class MedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medida
        fields = ('id', 'nome', 'valor')
