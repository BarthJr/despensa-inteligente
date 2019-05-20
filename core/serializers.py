from rest_framework import serializers

from core.models import Categoria, Medida, Produto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome')


class MedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medida
        fields = ('id', 'nome', 'valor')


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'nome', 'marca', 'tipo', 'peso')
