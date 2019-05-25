from rest_framework import viewsets

from core.models import Categoria, Medida, Produto, Despensa, ProdutoDespensa, Cliente
from core.serializers import CategoriaSerializer, MedidaSerializer, \
    ProdutoSerializer, DespensaSerializer, ProdutoDespensaSerializer, ClienteSerializer


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
