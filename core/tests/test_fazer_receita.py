import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import ProdutoDespensa


@pytest.fixture
def create_produto_despensa(produto, despensa, produto_despensa_obj):
    ProdutoDespensa.objects.create(**produto_despensa_obj)
    produto_despensa_obj['validade'] = '2019-08-10'
    ProdutoDespensa.objects.create(**produto_despensa_obj)


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
def test_fazer_receita_retirando_quantidade_e_restando_produto(create_produto_despensa, client, expected_fazer_receita):
    resp = client.put('/fazer_receita/desconta_quantidade_produto/?produto=1&despensa=1&quantidade=1')
    assert resp.data == expected_fazer_receita


@pytest.mark.django_db
def test_fazer_receita_retirando_quantidade_e_produto_acabando(create_produto_despensa, client, expected_fazer_receita):
    resp = client.put('/fazer_receita/desconta_quantidade_produto/?produto=1&despensa=1&quantidade=3')
    expected_fazer_receita[0]['id'] = None
    assert resp.data[0]['id'] == expected_fazer_receita[0]['id']


@pytest.mark.django_db
def test_fazer_receita_com_todos_produtos_acabando(create_produto_despensa, client, expected_fazer_receita):
    resp = client.put('/fazer_receita/desconta_quantidade_produto/?produto=1&despensa=1&quantidade=4')
    expected_fazer_receita[0]['id'] = None
    expected_fazer_receita[1]['id'] = None
    assert resp.data[0]['id'] == expected_fazer_receita[0]['id']
    assert resp.data[1]['id'] == expected_fazer_receita[1]['id']
