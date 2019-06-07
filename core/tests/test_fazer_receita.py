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
    produto_despensa_body1 = {
        'produto': produto,
        'despensa': despensa,
        'validade': '2019-08-10',
        'quantidade': 2
    }

    ProdutoDespensa.objects.create(**produto_despensa_body)
    ProdutoDespensa.objects.create(**produto_despensa_body1)


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.mark.django_db
def test_status_code(create_produto_despensa, client):
    assert ProdutoDespensa.objects.all()
    resp = client.put('/fazer_receita/desconta_quantidade_produto/?produto=1&despensa=1')
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_fazer_receita_retirando_quantidade_e_restando_produto(create_produto_despensa, client):
    expected = [
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
            'validade': '2019-10-30',
            'quantidade': 2
        },
    ]
    resp = client.put('/fazer_receita/desconta_quantidade_produto/?produto=1&despensa=1&quantidade=1')
    assert resp.data == expected


@pytest.mark.django_db
def test_fazer_receita_retirando_quantidade_e_produto_acabando(create_produto_despensa, client):
    expected = [
        {
            'id': None,
            'produto': 1,
            'despensa': 1,
            'validade': '2019-08-10',
            'quantidade': 2
        },
        {
            'id': 1,
            'produto': 1,
            'despensa': 1,
            'validade': '2019-10-30',
            'quantidade': 2
        },
    ]
    resp = client.put('/fazer_receita/desconta_quantidade_produto/?produto=1&despensa=1&quantidade=3')
    assert resp.data[0]['id'] == expected[0]['id']


@pytest.mark.django_db
def test_fazer_receita_com_todos_produtos_acabando(create_produto_despensa, client):
    expected = [
        {
            'id': None,
            'produto': 1,
            'despensa': 1,
            'validade': '2019-08-10',
            'quantidade': 2
        },
        {
            'id': None,
            'produto': 1,
            'despensa': 1,
            'validade': '2019-10-30',
            'quantidade': 2
        },
    ]
    resp = client.put('/fazer_receita/desconta_quantidade_produto/?produto=1&despensa=1&quantidade=4')
    assert resp.data[0]['id'] == expected[0]['id']
    assert resp.data[1]['id'] == expected[1]['id']
