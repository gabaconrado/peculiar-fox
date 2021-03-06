'''
@file:     test_marketlist.py (functional)
@author:   Gaba <gabaconrado@gmail.com>
@brief:    Functional tests for the marketlist module
@date:     2019
'''

import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


MAX_TIMEOUT = 3
BROWSER_TITLE = 'Peculiar fox'
PAGE_TITLE = 'Market List'
TITLE_ID = 'content_title'
INPUT_ID = 'txt_item'
TABLE_ID = 'table_list'
ITEM_NAME_A = 'Milk'
ITEM_NAME_B = 'Sauce'
ITEM_ID_A = 'item_1'
ITEM_ID_B = 'item_2'
LINK_CLEAN_ID = 'link_clean'


@pytest.fixture()
def browser(live_server):
    options = Options()
    options.headless = bool(int(os.environ.get('NO_DISPLAY_MODE', '0')))
    _browser = webdriver.Firefox(options=options)
    _browser.get(live_server.url + '/')
    yield _browser
    _browser.quit()


def is_homepage_clean(browser):
    return (
        browser.title == BROWSER_TITLE and
        browser.find_element_by_id(TITLE_ID).text == PAGE_TITLE and
        not browser.find_element_by_id(INPUT_ID).text and
        not len(browser.find_element_by_id(TABLE_ID).find_elements_by_tag_name('td')))


def insert_item(browser, item_name, item_id):
    browser.find_element_by_id(INPUT_ID).send_keys(item_name)
    browser.find_element_by_id(INPUT_ID).send_keys(Keys.ENTER)
    WebDriverWait(browser, MAX_TIMEOUT).until(
        EC.text_to_be_present_in_element((By.ID, item_id), item_name)
    )


def test_user_can_add_item_and_check(browser):
    # # Everytime the page is refreshed, the elements fetched get staled, thats why
    # # we need to find them again
    # Letício enter the website and notice a "Market list" blank page with a textfield and a button
    # The textfield and the list are clear
    assert is_homepage_clean(browser), "Homepage is not clean or it is wrong"
    # Letício type an item and presses the button, the added item is shown and the field is cleared
    insert_item(browser, ITEM_NAME_A, ITEM_ID_A)


def test_user_can_delete_list(browser):
    # Letício enter the website and notice a "Market list" blank page with a textfield and a button
    # The textfield and the list are clear
    assert is_homepage_clean(browser), "Homepage is not clean or it is wrong"
    # He add two items to his list
    insert_item(browser, ITEM_NAME_A, ITEM_ID_A)
    insert_item(browser, ITEM_NAME_B, ITEM_ID_B)
    # Letício then goes to the supermarket and buy everything he needs, when he comes back
    # he decides to clear his list, he notices a button "Clean list" and presses it
    item_a = browser.find_element_by_id(ITEM_ID_A)
    browser.find_element_by_id(LINK_CLEAN_ID).click()
    WebDriverWait(browser, MAX_TIMEOUT).until(
        EC.staleness_of(item_a)
    )
    # Letício then sees that all the items were removed from the list
    assert is_homepage_clean(browser)
