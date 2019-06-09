import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Produto, Categoria


@pytest.fixture
def create_produto(produto):
    categoria_obj = Categoria.objects.create(nome='Doces')
    produto['categoria'] = categoria_obj
    Produto.objects.create(nome=produto.get('nome'),
                           marca=produto.get('marca'),
                           tipo=produto.get('tipo'),
                           peso=produto.get('peso'),
                           categoria=produto.get('categoria'),
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
def test_get_produtos(create_produto, client, expected_produto):
    resp = client.get('/produtos/')
    assert resp.data[0] == expected_produto


@pytest.mark.django_db
def test_post_status_code_produtos(client, produto):
    Categoria.objects.create(nome='Doces')
    resp = client.post('/produtos/', produto)
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_produtos(client, produto, expected_produto):
    Categoria.objects.create(nome='Doces')
    resp = client.post('/produtos/', produto)
    assert resp.data == expected_produto
