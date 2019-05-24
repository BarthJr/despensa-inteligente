import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import ProdutoDespensa, Produto, Despensa, Categoria


@pytest.fixture
def create_produto_despensa():
    categoria = Categoria.objects.create(nome='Doces')
    produto_body = {
        'nome': 'Chocolate',
        'marca': 'Nestle',
        'tipo': 'Meio Amargo',
        'peso': 250,
        'categoria': categoria
    }
    produto = Produto.objects.create(**produto_body)
    despensa_body = {
        'nome': 'Casa',
        'localizacao': 'Tangamandapio',
    }
    despensa = Despensa.objects.create(**despensa_body)
    produto_despensa_body = {
        'produto': produto,
        'despensa': despensa,
        'validade': '2019-10-30',
        'quantidade': 2
    }
    ProdutoDespensa.objects.create(**produto_despensa_body)


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.mark.django_db
def test_produto_despensa_create(create_produto_despensa):
    assert ProdutoDespensa.objects.exists()


@pytest.mark.django_db
def test_status_code(client):
    resp = client.get('/produtos_despensas/')
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_produto_despensa(create_produto_despensa, client):
    expected = {
        'id': 1,
        'produto': 1,
        'despensa': 1,
        'validade': '2019-10-30',
        'quantidade': 2
    }
    resp = client.get('/produtos_despensas/')
    assert resp.data[0] == expected


@pytest.mark.django_db
def test_post_status_code_produto_despensa(client, create_produto_despensa):
    produto_despensa_body = {
        'produto': 1,
        'despensa': 1,
        'validade': '2019-10-29',
        'quantidade': 2
    }
    resp = client.post('/produtos_despensas/', produto_despensa_body)
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_produto_despensa(client, create_produto_despensa):
    expected = {
        'id': 2,
        'produto': 1,
        'despensa': 1,
        'validade': '2019-10-30',
        'quantidade': 2
    }
    resp = client.post('/produtos_despensas/', {
        'produto': 1,
        'despensa': 1,
        'validade': '2019-10-30',
        'quantidade': 2
    })
    assert resp.data == expected
