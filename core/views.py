from rest_framework import viewsets

from core.models import Categoria, Medida, Produto, Despensa, ProdutoDespensa, Cliente, Receita
from core.serializers import CategoriaSerializer, MedidaSerializer, \
    ProdutoSerializer, DespensaSerializer, ProdutoDespensaSerializer, ClienteSerializer, ReceitaSerializer


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


class DespensaViewSet(viewsets.ModelViewSet):
    queryset = Despensa.objects.all()
    serializer_class = DespensaSerializer


class ProdutoDespensaViewSet(viewsets.ModelViewSet):
    queryset = ProdutoDespensa.objects.all()
    serializer_class = ProdutoDespensaSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
