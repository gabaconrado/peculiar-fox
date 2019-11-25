'''
@file:     test_marketlist.py (unit)
@author:   Gaba <gabaconrado@gmail.com>
@brief:    Unit tests for the marketlists
@date:     2019
'''
import pytest
from django.urls import reverse
from marketlist import views
from marketlist.models import Item

METHOD_GET = 0
METHOD_POST = 1


@pytest.fixture
def item(db):
    return Item.objects.create(name='Milk')


@pytest.fixture
def response(db, client, path, method, data):
    if method == METHOD_GET:
        return client.get(reverse(path))
    return client.post(reverse(path), data)


@pytest.mark.parametrize('path,method,data', [('marketlist:marketlist', METHOD_GET, None)])
def test_list_route(response):
    assert response.status_code == 200
    assert response.resolver_match.func == views.marketlist
    assert response.templates[0].name == 'marketlist.html'


@pytest.mark.parametrize('path,method,data', [('marketlist:home', METHOD_GET, None)])
def test_home_redir_to_marketlist(response):
    assert response.status_code == 302
    assert response.get('location') == reverse('marketlist:marketlist')

@pytest.mark.parametrize(
    'path,method,data', [('marketlist:marketlist', METHOD_POST, {'name': 'Milk'})])
def test_add_new_item_and_redirect(response):
    assert Item.objects.count() == 1, 'Object not inserted'
    assert Item.objects.first().name == 'Milk', 'Wrong object inserted'
    assert response.status_code == 302
    assert response.get('location') == reverse('marketlist:marketlist')

@pytest.mark.parametrize('path,method,data', [('marketlist:marketlist', METHOD_GET, None)])
def test_add_new_item_and_show(item, response):
    assert item.name in response.content.decode()


def test_clear_list_and_redirect(item, client):
    response = client.post(reverse('marketlist:clean'), follow=True)
    assert item.name not in response.content.decode()
