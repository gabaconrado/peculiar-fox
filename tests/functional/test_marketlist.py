'''
@file:     test_marketlist.py (functional)
@author:   Gaba <gabaconrado@gmail.com>
@brief:    Functional tests for the marketlist module
@date:     2019
'''

import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    _browser = webdriver.Firefox()
    _browser.get('http://localhost:8000')
    yield _browser
    _browser.quit()


def test_user_can_add_item(browser):
    # Letício enter the website and notice a "Market list" blank page with a textfield and a button
    assert browser.title == 'Peculiar fox'
    assert browser.find_elements_by_id('div_header').text == 'Market list'
    assert not browser.find_elements_by_id('div_list')
    # Letício type an item and presses the button, the added item is shown and the field is cleared
    assert 1 == 2
