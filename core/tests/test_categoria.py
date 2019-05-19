import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Categoria


@pytest.fixture
def create_despensa():
    nome = 'Congelados'
    Categoria.objects.create(nome=nome)


@pytest.fixture
def client(create_despensa):
    client = APIClient()
    return client


@pytest.mark.django_db
def test_categoria_create(create_despensa):
    assert Categoria.objects.exists()


@pytest.mark.django_db
def test_status_code(client):
    resp = client.get('/categorias/')
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_categoria(client):
    expect = {'id': 1, 'nome': 'Congelados'}
    resp = client.get('/categorias/')
    assert resp.data[0] == expect
