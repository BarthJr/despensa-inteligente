import pytest
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Favorita


@pytest.fixture
def create_favorita(favoritaObj):
    Favorita.objects.create(**favoritaObj)


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
def test_get_favoritas(create_favorita, client, expected_favorita):
    resp = client.get('/favoritas/')
    assert resp.data[0] == expected_favorita


@pytest.mark.django_db
def test_post_status_code_favoritas(client, favorita):
    resp = client.post('/favoritas/', favorita)
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_favoritas(client, favorita, expected_favorita):
    resp = client.post('/favoritas/', favorita)
    assert resp.data == expected_favorita
