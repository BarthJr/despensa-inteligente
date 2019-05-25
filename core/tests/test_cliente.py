import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Cliente, Categoria


@pytest.fixture
def create_cliente():
    cliente = {
        'nome': 'Junior Barth',
        'login': 'barth',
        'senha': 'b07c153de98af7e6ecda7ebf6d1a5e25',
    }
    Cliente.objects.create(**cliente)


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.mark.django_db
def test_cliente_create(create_cliente):
    assert Cliente.objects.exists()


@pytest.mark.django_db
def test_status_code(client):
    resp = client.get('/clientes/')
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_clientes(create_cliente, client):
    expected = {
        'id': 1,
        'nome': 'Junior Barth',
        'login': 'barth',
        'senha': 'b07c153de98af7e6ecda7ebf6d1a5e25',
    }
    resp = client.get('/clientes/')
    assert resp.data[0] == expected


@pytest.mark.django_db
def test_post_status_code_clientes(client):
    Categoria.objects.create(nome='Doces')
    resp = client.post('/clientes/', {
        'nome': 'Junior Barth',
        'login': 'barth',
        'senha': 'b07c153de98af7e6ecda7ebf6d1a5e25',
    })
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_clientes(client):
    expected = {
        'id': 1,
        'nome': 'Junior Barth',
        'login': 'barth',
        'senha': 'b07c153de98af7e6ecda7ebf6d1a5e25',
    }
    Categoria.objects.create(nome='Doces')
    resp = client.post('/clientes/', {
        'nome': 'Junior Barth',
        'login': 'barth',
        'senha': 'b07c153de98af7e6ecda7ebf6d1a5e25',
    })
    assert resp.data == expected
