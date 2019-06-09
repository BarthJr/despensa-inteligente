import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Receita


@pytest.fixture
def create_receita(receita):
    Receita.objects.create(**receita)


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.mark.django_db
def test_receita_create(create_receita):
    assert Receita.objects.exists()


@pytest.mark.django_db
def test_status_code(client):
    resp = client.get('/receitas/')
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_receitas(create_receita, client, expected_receita):
    resp = client.get('/receitas/')
    assert resp.data[0] == expected_receita


@pytest.mark.django_db
def test_post_status_code_receitas(client, receita, expected_cliente):
    receita['cliente'] = expected_cliente.get('id')
    resp = client.post('/receitas/', receita)
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_receitas(client, receita, expected_receita, expected_cliente):
    receita['cliente'] = expected_cliente.get('id')
    resp = client.post('/receitas/', receita)
    assert resp.data == expected_receita
