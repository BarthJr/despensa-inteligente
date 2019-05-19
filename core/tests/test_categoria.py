import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Categoria


@pytest.fixture
def create_despensa():
    nome = 'Congelados'
    Categoria.objects.create(nome=nome)


@pytest.fixture
def client():
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
def test_get_categorias(create_despensa, client):
    expect = {'id': 1, 'nome': 'Congelados'}
    resp = client.get('/categorias/')
    assert resp.data[0] == expect


@pytest.mark.django_db
def test_post_status_code_categorias(client):
    resp = client.post('/categorias/', {'nome': 'Higiene'})
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_categorias(client):
    expect = {'id': 1, 'nome': 'Higiene'}
    resp = client.post('/categorias/', {'nome': 'Higiene'})
    assert resp.data == expect
