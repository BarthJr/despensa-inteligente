import pytest

from core.models import Cliente, Receita, Produto, Despensa, Categoria


@pytest.fixture()
def categoria():
    return {'nome': 'Congelados'}


@pytest.fixture()
def expected_categoria():
    return {'id': 1, 'nome': 'Congelados'}


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
def despensa():
    return {
        'nome': 'Casa',
        'localizacao': 'Tangamandapio',
    }


@pytest.fixture()
def expected_despensa():
    return {
        'id': 1,
        'nome': 'Casa',
        'localizacao': 'Tangamandapio',
    }


@pytest.fixture()
def produto():
    return {
        'nome': 'Chocolate',
        'marca': 'Nestle',
        'tipo': 'Meio Amargo',
        'peso': 250,
        'categoria': 1
    }


@pytest.fixture()
def expected_produto():
    return {
        'id': 1,
        'nome': 'Chocolate',
        'marca': 'Nestle',
        'tipo': 'Meio Amargo',
        'peso': 250,
        'categoria': 1
    }


@pytest.fixture()
def produto_despensa_obj(produto, despensa):
    produto['categoria'] = Categoria.objects.create(nome='Doces')
    produto_obj = Produto.objects.create(**produto)
    despensa_obj = Despensa.objects.create(**despensa)
    return {
        'produto': produto_obj,
        'despensa': despensa_obj,
        'validade': '2019-10-29',
        'quantidade': 2
    }


@pytest.fixture()
def produto_despensa():
    return {
        'produto': 1,
        'despensa': 1,
        'validade': '2019-10-29',
        'quantidade': 2
    }


@pytest.fixture()
def expected_produto_despensa():
    return {
        'id': 1,
        'produto': 1,
        'despensa': 1,
        'validade': '2019-10-29',
        'quantidade': 2
    }


@pytest.fixture()
def produto_receita_obj(produto, receita, cliente):
    produto['categoria'] = Categoria.objects.create(nome='Doces')
    produto_obj = Produto.objects.create(**produto)
    receita_obj = Receita.objects.create(**receita)
    return {
        'produto': produto_obj,
        'receita': receita_obj,
        'quantidade': 2
    }


@pytest.fixture()
def produto_receita():
    return {
        'produto': 1,
        'receita': 1,
        'quantidade': 2
    }


@pytest.fixture()
def expected_produto_receita():
    return {
        'id': 2,
        'produto': 1,
        'receita': 1,
        'quantidade': 2
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


@pytest.fixture()
def fazer_receita(receita, cliente):
    receita = Receita.objects.create(**receita)
    return {
        'receita': receita.pk,
        'cliente': receita.cliente.pk
    }


@pytest.fixture()
def expected_fazer_receita(cliente):
    return [
        {
            'id': 2,
            'produto': 1,
            'despensa': 1,
            'validade': '2019-08-10',
            'quantidade': 1
        },
        {
            'id': 1,
            'produto': 1,
            'despensa': 1,
            'validade': '2019-10-29',
            'quantidade': 2
        },
    ]
