import pytest

from core.models import Cliente, Receita


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


@pytest.fixture()
def favoritaObj(receita, cliente):
    receitaObj = Receita.objects.create(**receita)
    # clienteObj = Cliente.objects.create(**cliente)
    return {
        'receita': receitaObj,
        'cliente': receitaObj.cliente
    }


@pytest.fixture()
def favorita(receita, cliente):
    receita = Receita.objects.create(**receita)
    return {
        'receita': receita.pk,
        'cliente': receita.cliente.pk
    }


@pytest.fixture()
def expected_favorita(cliente):
    return {
        'id': 1,
        'receita': 1,
        'cliente': 1
    }