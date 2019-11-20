'''
@file:     test_marketlist.py (unit)
@author:   Gaba <gabaconrado@gmail.com>
@brief:    Unit tests for the marketlists
@date:     2019
'''
import pytest
from django.test import Client
from django.urls import reverse
from marketlist import views

@pytest.fixture
def client():
    return Client()


def test_list_route(client):
    path = reverse('marketlist')
    response = client.get(path)
    assert response.status_code == 200
    assert response.resolver_match.func == views.marketlist
    assert response.templates[0].name == 'marketlist.html'


def test_home_redir_to_marketlist(client):
    path = reverse('home')
    response = client.get(path)
    assert response.status_code == 302
    assert response.get('location') == reverse('marketlist')
