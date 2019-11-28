'''
@file:     test_marketlist.py (functional)
@author:   Gaba <gabaconrado@gmail.com>
@brief:    Functional tests for the marketlist module
@date:     2019
'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


MAX_TIMEOUT = 3
BROWSER_TITLE = 'Peculiar fox'
PAGE_TITLE = 'Market list'
TITLE_ID = 'content_title'
INPUT_ID = 'txt_item'
TABLE_ID = 'table_list'
BTN_SUBMIT_ID = 'btn_submit'
ITEM_NAME_A = 'Milk'
ITEM_NAME_B = 'Sauce'
ITEM_ID_A = 'item_1'
ITEM_ID_B = 'item_2'
BTN_CLEAN_ID = 'btn_clean'


@pytest.fixture()
def browser(live_server):
    _browser = webdriver.Firefox()
    _browser.get(live_server.url + '/marketlist')
    yield _browser
    _browser.quit()


def is_homepage_clean(browser):
    return (
        browser.title == BROWSER_TITLE and
        browser.find_element_by_id(TITLE_ID).text == PAGE_TITLE and
        not browser.find_element_by_id(INPUT_ID).text and
        not len(browser.find_element_by_id(TABLE_ID).find_elements_by_tag_name('td')))


def insert_item(browser, item_name, item_id, use_button=True):
    browser.find_element_by_id(INPUT_ID).send_keys(item_name)
    if use_button:
        browser.find_element_by_id(BTN_SUBMIT_ID).click()
    else:
        browser.find_element_by_id(INPUT_ID).send_keys(Keys.ENTER)
    WebDriverWait(browser, MAX_TIMEOUT).until(
        EC.text_to_be_present_in_element((By.ID, item_id), item_name)
    )


def test_user_can_add_item_and_check(browser):
    # # Everytime the page is refreshed, the elements fetched get staled, thats why
    # # we need to find them again
    # Letício enter the website and notice a "Market list" blank page with a textfield and a button
    # The textfield and the list are clear
    assert is_homepage_clean(browser)
    # Letício type an item and presses the button, the added item is shown and the field is cleared
    insert_item(browser, ITEM_NAME_A, ITEM_ID_A)
    # Letício then tries to add a new item using enter instead of clicking the button
    # He sees that it works and the new item is also added to the list
    insert_item(browser, ITEM_NAME_B, ITEM_ID_B, use_button=False)


def test_user_can_delete_list(browser):
    # Letício enter the website and notice a "Market list" blank page with a textfield and a button
    # The textfield and the list are clear
    assert is_homepage_clean(browser)
    # He add two items to his list
    insert_item(browser, ITEM_NAME_A, ITEM_ID_A)
    # Letício then tries to add a new item using enter instead of clicking the button
    # He sees that it works and the new item is also added to the list
    insert_item(browser, ITEM_NAME_B, ITEM_ID_B)
    # Letício then goes to the supermarket and buy everything he needs, when he comes back
    # he decides to clear his list, he notices a button "Clean list" and presses it
    item_a = browser.find_element_by_id(ITEM_ID_A)
    browser.find_element_by_id(BTN_CLEAN_ID).click()
    WebDriverWait(browser, MAX_TIMEOUT).until(
        EC.staleness_of(item_a)
    )
    # Letício then sees that all the items were removed from the list
    assert is_homepage_clean(browser)
