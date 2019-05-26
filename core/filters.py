import django_filters

from core.models import Cliente


class ClienteFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Cliente
        fields = ['nome', ]
