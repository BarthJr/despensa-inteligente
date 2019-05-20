import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Produto


@pytest.fixture
def create_produto():
    produto = {
        'nome': 'Chocolate',
        'marca': 'Nestle',
        'tipo': 'Meio Amargo',
        'peso': 250
    }
    Produto.objects.create(nome=produto.get('nome'),
                           marca=produto.get('marca'),
                           tipo=produto.get('tipo'),
                           peso=produto.get('peso'),
                           )


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.mark.django_db
def test_produto_create(create_produto):
    assert Produto.objects.exists()


@pytest.mark.django_db
def test_status_code(client):
    resp = client.get('/produtos/')
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_produtos(create_produto, client):
    expect = {
        'id': 1,
        'nome': 'Chocolate',
        'marca': 'Nestle',
        'tipo': 'Meio Amargo',
        'peso': 250
    }
    resp = client.get('/produtos/')
    assert resp.data[0] == expect


@pytest.mark.django_db
def test_post_status_code_produtos(client):
    resp = client.post('/produtos/', {
        'nome': 'Chocolate',
        'marca': 'Nestle',
        'tipo': 'Meio Amargo',
        'peso': 250
    })
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_produtos(client):
    expect = {
        'id': 1,
        'nome': 'Chocolate',
        'marca': 'Nestle',
        'tipo': 'Meio Amargo',
        'peso': 250
    }
    resp = client.post('/produtos/', {
        'nome': 'Chocolate',
        'marca': 'Nestle',
        'tipo': 'Meio Amargo',
        'peso': 250
    })
    assert resp.data == expect
