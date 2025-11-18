import sys
import os
# Добавляем текущую директорию в путь поиска модулей
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# импорты должны работать
from data import TestUser
from locators import TestLocators
from urls import MAIN_PAGE

@pytest.fixture(scope='function')
def driver():
    # Настройка опций Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)
    driver.get(MAIN_PAGE)
    
    yield driver
    # Закрытие драйвера после теста
    driver.quit()


@pytest.fixture
def login(driver):
    
    # Переход к форме авторизации
    driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()

def go_to_login_form(driver):
    driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_REGISTER)
    )


def fill_login_credentials(driver):
    driver.find_element(*TestLocators.INPUT_EMAIL_AUTH).send_keys(TestUser.EXISTING_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD_AUTH).send_keys(TestUser.EXISTING_PASSWORD)


def submit_login(driver):
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()


def wait_for_successful_login(driver):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
    )