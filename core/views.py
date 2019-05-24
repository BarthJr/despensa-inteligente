from rest_framework import viewsets

from core.models import Categoria, Medida, Produto, Despensa, ProdutoDespensa
from core.serializers import CategoriaSerializer, MedidaSerializer, \
    ProdutoSerializer, DespensaSerializer, ProdutoDespensaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MedidaViewSet(viewsets.ModelViewSet):
    queryset = Medida.objects.all()
    serializer_class = MedidaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class DespensaViewSet(viewsets.ModelViewSet):
    queryset = Despensa.objects.all()
    serializer_class = DespensaSerializer


class ProdutoDespensaViewSet(viewsets.ModelViewSet):
    queryset = ProdutoDespensa.objects.all()
    serializer_class = ProdutoDespensaSerializer
