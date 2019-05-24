from rest_framework import viewsets

from core.models import Categoria, Medida, Produto, Despensa
from core.serializers import CategoriaSerializer, MedidaSerializer, ProdutoSerializer, DespensaSerializer


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
