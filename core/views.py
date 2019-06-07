from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.filters import ClienteFilter, DespensaFilter, ProdutoFilter
from core.models import Categoria, Medida, Produto, Despensa, ProdutoDespensa, Cliente, Receita, ProdutoReceita, \
    Favorita
from core.serializers import CategoriaSerializer, MedidaSerializer, \
    ProdutoSerializer, DespensaSerializer, ProdutoDespensaSerializer, ClienteSerializer, ReceitaSerializer, \
    ProdutoReceitaSerializer, FavoritaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MedidaViewSet(viewsets.ModelViewSet):
    queryset = Medida.objects.all()
    serializer_class = MedidaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_class = ProdutoFilter


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_class = ClienteFilter


class DespensaViewSet(viewsets.ModelViewSet):
    queryset = Despensa.objects.all()
    serializer_class = DespensaSerializer
    filter_class = DespensaFilter


class ProdutoDespensaViewSet(viewsets.ModelViewSet):
    queryset = ProdutoDespensa.objects.all()
    serializer_class = ProdutoDespensaSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


class ProdutoReceitaViewSet(viewsets.ModelViewSet):
    queryset = ProdutoReceita.objects.all()
    serializer_class = ProdutoReceitaSerializer


class FavoritaViewSet(viewsets.ModelViewSet):
    queryset = Favorita.objects.all()
    serializer_class = FavoritaSerializer


class FazerReceitaViewSet(viewsets.ModelViewSet):
    queryset = ProdutoDespensa.objects.all()
    serializer_class = ProdutoDespensaSerializer

    @action(detail=False, methods=['put'])
    def desconta_quantidade_produto(self, request):
        produto = request.query_params.get('produto', None)
        despensa = request.query_params.get('despensa', None)
        quantidade = int(request.query_params.get('quantidade', 0))
        produtos = ProdutoDespensa.objects.filter(despensa=despensa, produto=produto).order_by('validade')
        quantidadeDespensas = produtos.aggregate(Sum('quantidade'))
        quantidadeDespensas = quantidadeDespensas.get('quantidade__sum', 0)
        if quantidade <= quantidadeDespensas:
            produtos = ProdutoDespensa.objects.filter(despensa=despensa, produto=produto).order_by('validade')
            for produto in produtos:
                if quantidade > produto.quantidade:
                    quantidade -= produto.quantidade
                    produto.quantidade = 0
                    produto.delete()
                elif quantidade < produto.quantidade:
                    produto.quantidade -= quantidade
                    produto.save()
                    break
                else:
                    produto.delete()
                    break
        serializer = self.get_serializer(produtos, many=True)
        return Response(serializer.data)
