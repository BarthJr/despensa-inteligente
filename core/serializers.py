from rest_framework import serializers

from core.models import Categoria, Medida, Produto, Despensa


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
        fields = ('id', 'nome', 'marca', 'tipo', 'peso', 'categoria')


class DespensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despensa
        fields = ('id', 'nome', 'localizacao')
