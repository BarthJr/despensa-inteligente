import pytest


@pytest.fixture()
def cliente():
    return {
        'nome': 'Junior Barth',
        'login': 'barth',
        'senha': 'b07c153de98af7e6ecda7ebf6d1a5e25',
    }


@pytest.fixture()
def expected_cliente():
    return {
        'id': 1,
        'nome': 'Junior Barth',
        'login': 'barth',
        'senha': 'b07c153de98af7e6ecda7ebf6d1a5e25',
    }
