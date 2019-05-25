import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Favorita, Receita, Cliente


@pytest.fixture
def create_favorita():
    cliente_body = {
        'nome': 'Junior Barth',
        'login': 'barth',
        'senha': 'b07c153de98af7e6ecda7ebf6d1a5e25',
    }
    cliente = Cliente.objects.create(**cliente_body)
    receita_body = {
        'titulo': 'Fricasse de Frango',
        'modoPreparo': 'Desfiar o frango, bater os ingredientes liquidos, refogar no frango, distribuir o queijo',
        'tempoExecucao': '01:30:00',
        'quantidade': 4,
        'cliente': cliente
    }
    receita = Receita.objects.create(**receita_body)
    favorita = {
        'receita': receita,
        'cliente': cliente
    }
    Favorita.objects.create(**favorita)


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.mark.django_db
def test_favorita_create(create_favorita):
    assert Favorita.objects.exists()


@pytest.mark.django_db
def test_status_code(client):
    resp = client.get('/favoritas/')
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_favoritas(create_favorita, client):
    expected = {
        'id': 1,
        'receita': 1,
        'cliente': 1
    }
    resp = client.get('/favoritas/')
    assert resp.data[0] == expected


@pytest.mark.django_db
def test_post_status_code_favoritas(client):
    cliente_body = {
        'nome': 'Junior Barth',
        'login': 'barth',
        'senha': 'b07c153de98af7e6ecda7ebf6d1a5e25',
    }
    cliente = Cliente.objects.create(**cliente_body)
    receita_body = {
        'titulo': 'Fricasse de Frango',
        'modoPreparo': 'Desfiar o frango, bater os ingredientes liquidos, refogar no frango, distribuir o queijo',
        'tempoExecucao': '01:30:00',
        'quantidade': 4,
        'cliente': cliente
    }
    Receita.objects.create(**receita_body)
    resp = client.post('/favoritas/', {
        'receita': 1,
        'cliente': 1
    })
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_favoritas(client):
    cliente_body = {
        'nome': 'Junior Barth',
        'login': 'barth',
        'senha': 'b07c153de98af7e6ecda7ebf6d1a5e25',
    }
    cliente = Cliente.objects.create(**cliente_body)
    receita_body = {
        'titulo': 'Fricasse de Frango',
        'modoPreparo': 'Desfiar o frango, bater os ingredientes liquidos, refogar no frango, distribuir o queijo',
        'tempoExecucao': '01:30:00',
        'quantidade': 4,
        'cliente': cliente
    }
    Receita.objects.create(**receita_body)
    expected = {
        'id': 1,
        'receita': 1,
        'cliente': 1
    }
    resp = client.post('/favoritas/', {
        'receita': 1,
        'cliente': 1
    })
    assert resp.data == expected
