import django_filters

from core.models import Cliente, Despensa


class ClienteFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Cliente
        fields = ['nome', 'login']


class DespensaFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Despensa
        fields = ['nome', 'localizacao']
