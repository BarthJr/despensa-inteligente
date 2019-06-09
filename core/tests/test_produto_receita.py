import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import ProdutoReceita


@pytest.fixture
def create_produto_receita(produto_receita_obj):
    ProdutoReceita.objects.create(**produto_receita_obj)


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
def test_get_produto_receita(create_produto_receita, client, expected_produto_receita):
    resp = client.get('/produtos_receitas/')
    expected_produto_receita['id'] = 1
    assert resp.data[0] == expected_produto_receita


@pytest.mark.django_db
def test_post_status_code_produto_receita(client, create_produto_receita, produto_receita):
    resp = client.post('/produtos_receitas/', produto_receita)
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_produto_receita(client, create_produto_receita, produto_receita, expected_produto_receita):
    resp = client.post('/produtos_receitas/', produto_receita)
    assert resp.data == expected_produto_receita
