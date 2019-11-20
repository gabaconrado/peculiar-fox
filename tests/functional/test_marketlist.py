'''
@file:     test_marketlist.py (functional)
@author:   Gaba <gabaconrado@gmail.com>
@brief:    Functional tests for the marketlist module
@date:     2019
'''

import pytest
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

MAX_TIMEOUT = 5


@pytest.fixture
def browser():
    _browser = webdriver.Firefox()
    _browser.get('http://localhost:8000/marketlist')
    yield _browser
    _browser.quit()


def test_user_can_add_item(browser):
    # Letício enter the website and notice a "Market list" blank page with a textfield and a button
    # The textfield and the list are clear
    content_title = browser.find_element_by_id('content_title')
    item_input = browser.find_element_by_id('txt_item')
    btn_submit = browser.find_element_by_id('btn_submit')
    table_list = browser.find_element_by_id('table_list')
    rows_list = table_list.find_elements_by_tag_name('tr')
    assert browser.title == 'Peculiar fox'
    assert content_title.text == 'Market list'
    assert not item_input.text
    assert btn_submit
    assert table_list
    assert len(rows_list) == 0
    # Letício type an item and presses the button, the added item is shown and the field is cleared
#    browser.find_element_by_id('txt_item').sendKeys('Milk')
#    browser.find_element_by_id('btn_submit').click()
