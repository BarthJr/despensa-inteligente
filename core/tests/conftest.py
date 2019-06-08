import pytest

from core.models import Cliente


@pytest.fixture()
def cliente():
    return {
        'nome': 'Junior Barth',
        'login': 'barth',
        'senha': 'b07c153de98af7e6ecda7ebf6d1a5e25',
    }


@pytest.fixture()
def expected_cliente():
    return {
        'id': 1,
        'nome': 'Junior Barth',
        'login': 'barth',
        'senha': 'b07c153de98af7e6ecda7ebf6d1a5e25',
    }


@pytest.fixture()
def receita(cliente):
    clienteObj = Cliente.objects.create(**cliente)
    return {
        'titulo': 'Fricasse de Frango',
        'modoPreparo': 'Desfiar o frango, bater os ingredientes liquidos, refogar no frango, distribuir o queijo',
        'tempoExecucao': '01:30:00',
        'quantidade': 4,
        'cliente': clienteObj
    }


@pytest.fixture()
def expected_receita(cliente):
    return {
        'id': 1,
        'titulo': 'Fricasse de Frango',
        'modoPreparo': 'Desfiar o frango, bater os ingredientes liquidos, refogar no frango, distribuir o queijo',
        'tempoExecucao': '01:30:00',
        'quantidade': 4,
        'cliente': 1
    }
