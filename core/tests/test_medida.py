import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Medida


@pytest.fixture
def create_medida():
    medida = {
        'nome': 'Litros',
        'valor': 1
    }
    Medida.objects.create(nome=medida.get('nome'), valor=medida.get('valor'))


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.mark.django_db
def test_medida_create(create_medida):
    assert Medida.objects.exists()


@pytest.mark.django_db
def test_status_code(client):
    resp = client.get('/medidas/')
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_medidas(create_medida, client):
    expect = {'id': 1, 'nome': 'Litros', 'valor': 1}
    resp = client.get('/medidas/')
    assert resp.data[0] == expect


@pytest.mark.django_db
def test_post_status_code_medidas(client):
    resp = client.post('/medidas/', {'nome': 'Litros', 'valor': 1})
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_medidas(client):
    expect = {'id': 1, 'nome': 'Litros', 'valor': 1}
    resp = client.post('/medidas/', {'nome': 'Litros', 'valor': 1})
    assert resp.data == expect
