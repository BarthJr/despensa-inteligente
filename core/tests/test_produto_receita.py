import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import ProdutoReceita, Produto, Receita, Categoria, Cliente


@pytest.fixture
def create_produto_receita():
    categoria = Categoria.objects.create(nome='Doces')
    produto_body = {
        'nome': 'Chocolate',
        'marca': 'Nestle',
        'tipo': 'Meio Amargo',
        'peso': 250,
        'categoria': categoria
    }
    produto = Produto.objects.create(**produto_body)
    cliente_body = {
        'nome': 'Junior Barth',
        'login': 'barth',
        'senha': 'b07c153de98af7e6ecda7ebf6d1a5e25',
    }
    cliente = Cliente.objects.create(**cliente_body)
    receita_body = {
        'titulo': 'Fricasse de Frango',
        'modoPreparo': 'Desfiar o frango, bater os ingredientes liquidos, refogar no frango, distribuir o queijo',
        'tempoExecucao': '01:30:00',
        'quantidade': 4,
        'cliente': cliente
    }
    receita = Receita.objects.create(**receita_body)
    produto_receita_body = {
        'produto': produto,
        'receita': receita,
        'quantidade': 2
    }
    ProdutoReceita.objects.create(**produto_receita_body)


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.mark.django_db
def test_produto_receita_create(create_produto_receita):
    assert ProdutoReceita.objects.exists()


@pytest.mark.django_db
def test_status_code(client):
    resp = client.get('/produtos_receitas/')
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_produto_receita(create_produto_receita, client):
    expected = {
        'id': 1,
        'produto': 1,
        'receita': 1,
        'quantidade': 2
    }
    resp = client.get('/produtos_receitas/')
    assert resp.data[0] == expected


@pytest.mark.django_db
def test_post_status_code_produto_receita(client, create_produto_receita):
    produto_receita_body = {
        'produto': 1,
        'receita': 1,
        'quantidade': 2
    }
    resp = client.post('/produtos_receitas/', produto_receita_body)
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_produto_receita(client, create_produto_receita):
    expected = {
        'id': 2,
        'produto': 1,
        'receita': 1,
        'quantidade': 2
    }
    resp = client.post('/produtos_receitas/', {
        'produto': 1,
        'receita': 1,
        'quantidade': 2
    })
    assert resp.data == expected
