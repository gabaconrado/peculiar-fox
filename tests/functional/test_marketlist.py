'''
@file:     test_marketlist.py (functional)
@author:   Gaba <gabaconrado@gmail.com>
@brief:    Functional tests for the marketlist module
@date:     2019
'''

import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

MAX_TIMEOUT = 5

BROWSER_TITLE = 'Peculiar fox'
PAGE_TITLE = 'Market list'
TITLE_ID = 'content_title'
INPUT_ID = 'txt_item'
TABLE_ID = 'table_list'
BTN_SUBMIT_ID = 'btn_submit'
ITEM_NAME_A = 'Milk'
ITEM_NAME_B = 'Sauce'


@pytest.fixture
def browser(live_server):
    _browser = webdriver.Firefox()
    _browser.get(live_server.url + '/marketlist')
    yield _browser
    _browser.quit()


def test_user_can_add_item(browser):
    # Letício enter the website and notice a "Market list" blank page with a textfield and a button
    # The textfield and the list are clear
    assert browser.title == BROWSER_TITLE
    assert browser.find_element_by_id(TITLE_ID).text == PAGE_TITLE
    assert not browser.find_element_by_id(INPUT_ID).text
    assert len(browser.find_element_by_id(TABLE_ID).find_elements_by_tag_name('tr')) == 0
    # Letício type an item and presses the button, the added item is shown and the field is cleared
    browser.find_element_by_id(INPUT_ID).send_keys(ITEM_NAME_A)
    browser.find_element_by_id(BTN_SUBMIT_ID).click()
    sleep(1)
    assert \
        len(browser.find_element_by_id(TABLE_ID).find_elements_by_tag_name('tr')) == 1, \
        'Element was not added to the list'
    # Letício then tries to add a new item using enter instead of clicking the button
    # He sees that it works and the new item is also added to the list
    browser.find_element_by_id(INPUT_ID).send_keys(ITEM_NAME_B)
    browser.find_element_by_id(INPUT_ID).send_keys(Keys.ENTER)
    sleep(1)
    assert \
        len(browser.find_element_by_id(TABLE_ID).find_elements_by_tag_name('tr')) == 2, \
        'New element was not added to the list'
