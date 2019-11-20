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
from marketlist.models import Item


@pytest.fixture
def client():
    return Client()


def test_list_route(client, db):
    path = reverse('marketlist:marketlist')
    response = client.get(path)
    assert response.status_code == 200
    assert response.resolver_match.func == views.marketlist
    assert response.templates[0].name == 'marketlist.html'


def test_home_redir_to_marketlist(client, db):
    path = reverse('marketlist:home')
    response = client.get(path)
    assert response.status_code == 302
    assert response.get('location') == reverse('marketlist:marketlist')


def test_add_new_item_and_redirect(client, db):
    path = reverse('marketlist:marketlist')
    data = {'name': 'Milk'}
    response = client.post(path, data)
    assert Item.objects.count() == 1, 'Object not inserted'
    assert Item.objects.first().name == 'Milk', 'Wrong object inserted'
    assert response.status_code == 302
    assert response.get('location') == reverse('marketlist:marketlist')


def test_add_new_item_and_show(client, db):
    new_item = Item.objects.create(name='Milk')
    path = reverse('marketlist:marketlist')
    response = client.get(path)
    assert new_item.name in response.content.decode()
