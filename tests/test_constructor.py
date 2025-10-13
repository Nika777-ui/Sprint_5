import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators
import time

class TestConstructor:
    def test_switch_to_buns_section(self, driver):
        try:
            """Переход к разделу 'Булки'"""
            # Ждем пока раздел станет кликабельным
            buns_section = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(MainPageLocators.BUNS_SECTION)
            )
            
            # Используем JavaScript клик
            driver.execute_script("arguments[0].click();", buns_section)
            
            time.sleep(1)
            
            # Проверяем что раздел активен
            active_section = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
            assert "Булки" in active_section.text
        finally:
            driver.quit()

    def test_switch_to_sauces_section(self, driver):
        try:
            """Переход к разделу 'Соусы'"""
            sauces_section = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
            )
            
            driver.execute_script("arguments[0].click();", sauces_section)
            
            time.sleep(1)
            
            active_section = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
            assert "Соусы" in active_section.text
        finally:
            driver.quit()

    def test_switch_to_fillings_section(self, driver):
        try:
            """Переход к разделу 'Начинки'"""
            fillings_section = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION)
            )
            
            driver.execute_script("arguments[0].click();", fillings_section)
            
            time.sleep(1)
            
            active_section = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
            assert "Начинки" in active_section.text
        finally:
            driver.quit()