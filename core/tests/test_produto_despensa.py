import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import ProdutoDespensa


@pytest.fixture
def create_produto_despensa(produto_despensa_obj):
    ProdutoDespensa.objects.create(**produto_despensa_obj)


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
def test_get_produto_despensa(create_produto_despensa, client, expected_produto_despensa):
    resp = client.get('/produtos_despensas/')
    assert resp.data[0] == expected_produto_despensa


@pytest.mark.django_db
def test_post_status_code_produto_despensa(client, create_produto_despensa, produto_despensa):
    resp = client.post('/produtos_despensas/', produto_despensa)
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_produto_despensa(client, create_produto_despensa, produto_despensa, expected_produto_despensa):
    resp = client.post('/produtos_despensas/', produto_despensa)
    expected_produto_despensa['id'] = 2
    assert resp.data == expected_produto_despensa
