import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Receita, Cliente


@pytest.fixture
def create_receita():
    cliente = Cliente.objects.create(nome='Mo', login='mo', senha='b07c153de98af7e6ecda7ebf6d1a5e25')
    receita = {
        'titulo': 'Fricasse de Frango',
        'modoPreparo': 'Desfiar o frango, bater os ingredientes liquidos, refogar no frango, distribuir o queijo',
        'tempoExecucao': '01:30:00',
        'quantidade': 4,
        'cliente': cliente
    }
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
def test_get_receitas(create_receita, client):
    expected = {
        'id': 1,
        'titulo': 'Fricasse de Frango',
        'modoPreparo': 'Desfiar o frango, bater os ingredientes liquidos, refogar no frango, distribuir o queijo',
        'tempoExecucao': '01:30:00',
        'quantidade': 4,
        'cliente': 1
    }
    resp = client.get('/receitas/')
    assert resp.data[0] == expected


@pytest.mark.django_db
def test_post_status_code_receitas(client):
    Cliente.objects.create(nome='Mo', login='mo', senha='b07c153de98af7e6ecda7ebf6d1a5e25')
    resp = client.post('/receitas/', {
        'titulo': 'Fricasse de Frango',
        'modoPreparo': 'Desfiar o frango, bater os ingredientes liquidos, refogar no frango, distribuir o queijo',
        'tempoExecucao': '01:30:00',
        'quantidade': 4,
        'cliente': 1
    })
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_receitas(client):
    expected = {
        'id': 1,
        'titulo': 'Fricasse de Frango',
        'modoPreparo': 'Desfiar o frango, bater os ingredientes liquidos, refogar no frango, distribuir o queijo',
        'tempoExecucao': '01:30:00',
        'quantidade': 4,
        'cliente': 1
    }
    Cliente.objects.create(nome='Mo', login='mo', senha='b07c153de98af7e6ecda7ebf6d1a5e25')
    resp = client.post('/receitas/', {
        'titulo': 'Fricasse de Frango',
        'modoPreparo': 'Desfiar o frango, bater os ingredientes liquidos, refogar no frango, distribuir o queijo',
        'tempoExecucao': '01:30:00',
        'quantidade': 4,
        'cliente': 1
    })
    assert resp.data == expected
