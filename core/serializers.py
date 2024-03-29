from rest_framework import serializers

from core.models import Categoria, Medida, Produto, Despensa, ProdutoDespensa, Cliente, Receita, ProdutoReceita, \
    Favorita


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


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'login', 'senha')


class DespensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despensa
        fields = ('id', 'nome', 'localizacao')


class ProdutoDespensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoDespensa
        fields = ('id', 'produto', 'despensa', 'validade', 'quantidade')


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ('id', 'titulo', 'modoPreparo', 'tempoExecucao', 'quantidade', 'cliente')


class ProdutoReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoReceita
        fields = ('id', 'produto', 'receita', 'quantidade')


class FavoritaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorita
        fields = ('id', 'receita', 'cliente')
