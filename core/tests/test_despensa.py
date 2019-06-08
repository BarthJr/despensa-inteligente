import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Despensa, Categoria


@pytest.fixture()
def despensa():
    return {
        'nome': 'Casa',
        'localizacao': 'Tangamandapio',
    }


@pytest.fixture()
def expected_despensa():
    return {
        'id': 1,
        'nome': 'Casa',
        'localizacao': 'Tangamandapio',
    }


@pytest.fixture
def create_despensa(despensa):
    Despensa.objects.create(nome=despensa.get('nome'),
                            localizacao=despensa.get('localizacao'),
                            )


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.mark.django_db
def test_despensa_create(create_despensa):
    assert Despensa.objects.exists()


@pytest.mark.django_db
def test_status_code(client):
    resp = client.get('/despensas/')
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_despensas(create_despensa, client, expected_despensa):
    resp = client.get('/despensas/')
    assert resp.data[0] == expected_despensa


@pytest.mark.django_db
def test_post_status_code_despensas(client, despensa):
    Categoria.objects.create(nome='Doces')
    resp = client.post('/despensas/', despensa)
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_despensas(client, despensa, expected_despensa):
    resp = client.post('/despensas/', despensa)
    assert resp.data == expected_despensa
