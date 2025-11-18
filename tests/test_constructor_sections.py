import sys
import os
# Добавляем корневую папку в путь поиска
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import SectionData


class TestConstructorSections:
    """Тесты переключения разделов конструктора"""

    def test_initial_section_is_buns(self, driver):
        """По умолчанию активен раздел 'Булки'"""
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_MAIN)
        )
        assert driver.find_element(*TestLocators.ACTIVE_SECTION).text == SectionData.NAMES["buns"]

    def test_switch_buns_to_sauces(self, driver):
        """Переход из 'Булки' в 'Соусы'"""
        self._switch_section(driver, TestLocators.SECTION_SAUCES, SectionData.NAMES["sauces"])

    def test_switch_buns_to_fillings(self, driver):
        """Переход из 'Булки' в 'Начинки'"""
        self._switch_section(driver, TestLocators.SECTION_FILLINGS, SectionData.NAMES["fillings"])

    def test_switch_sauces_to_buns(self, driver):
        """Переход из 'Соусы' в 'Булки'"""
        driver.find_element(*TestLocators.SECTION_SAUCES).click()
        self._wait_for_section_active(driver, SectionData.NAMES["sauces"])
        self._switch_section(driver, TestLocators.SECTION_BUNS, SectionData.NAMES["buns"])

    def test_switch_sauces_to_fillings(self, driver):
        """Переход из 'Соусы' в 'Начинки'"""
        driver.find_element(*TestLocators.SECTION_SAUCES).click()
        self._wait_for_section_active(driver, SectionData.NAMES["sauces"])
        self._switch_section(driver, TestLocators.SECTION_FILLINGS, SectionData.NAMES["fillings"])

    def test_switch_fillings_to_buns(self, driver):
        """Переход из 'Начинки' в 'Булки'"""
        driver.find_element(*TestLocators.SECTION_FILLINGS).click()
        self._wait_for_section_active(driver, SectionData.NAMES["fillings"])
        self._switch_section(driver, TestLocators.SECTION_BUNS, SectionData.NAMES["buns"])

    def test_switch_fillings_to_sauces(self, driver):
        """Переход из 'Начинки' в 'Соусы'"""
        driver.find_element(*TestLocators.SECTION_FILLINGS).click()
        self._wait_for_section_active(driver, SectionData.NAMES["fillings"])
        self._switch_section(driver, TestLocators.SECTION_SAUCES, SectionData.NAMES["sauces"])

    def test_sections_with_login(self, driver, login):
        """Переключение разделов после авторизации"""
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER)
        )
        
        # Проверяем все переходы после логина
        self._switch_section(driver, TestLocators.SECTION_SAUCES, SectionData.NAMES["sauces"])
        self._switch_section(driver, TestLocators.SECTION_FILLINGS, SectionData.NAMES["fillings"])
        self._switch_section(driver, TestLocators.SECTION_BUNS, SectionData.NAMES["buns"])

    def test_section_content_changes(self, driver):
        """Контент раздела меняется при переключении"""
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_MAIN)
        )
        
        # Булки → Соусы
        assert driver.find_element(*TestLocators.TEXT_BUNS).is_displayed()
        self._switch_section(driver, TestLocators.SECTION_SAUCES, SectionData.NAMES["sauces"])
        assert driver.find_element(*TestLocators.TEXT_SAUCES).is_displayed()
        
        # Соусы → Начинки
        self._switch_section(driver, TestLocators.SECTION_FILLINGS, SectionData.NAMES["fillings"])
        assert driver.find_element(*TestLocators.TEXT_FILLINGS).is_displayed()

    def _switch_section(self, driver, section_locator, expected_section):
        """Вспомогательный метод для переключения раздела"""
        driver.find_element(*section_locator).click()
        self._wait_for_section_active(driver, expected_section)
        assert driver.find_element(*TestLocators.ACTIVE_SECTION).text == expected_section

    def _wait_for_section_active(self, driver, section_name):
        """Ожидание активации раздела"""
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(TestLocators.ACTIVE_SECTION, section_name)
        )