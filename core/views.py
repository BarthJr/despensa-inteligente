from rest_framework import viewsets

from core.filters import ClienteFilter, DespensaFilter
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
