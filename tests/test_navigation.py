import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.login_helper import login
from pages.locators import MainPageLocators, ProfilePageLocators

class TestNavigation:
    def test_go_to_personal_account(self, driver):
        """Переход в личный кабинет"""
        # Используем вспомогательную функцию для входа
        login(driver)
        
        # Переходим в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Ждем загрузки с явным ожиданием
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )
        
        # Проверяем что перешли в личный кабинет
        assert driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).is_displayed()

    def test_go_from_account_to_constructor_via_button(self, driver):
        """Переход из личного кабинета в конструктор по кнопке"""
        # Входим и переходим в личный кабинет
        login(driver)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Ждем загрузки личного кабинета
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )
        
        # Нажимаем кнопку "Конструктор"
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        
        # Проверяем что вернулись на главную
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()

    def test_go_from_account_to_constructor_via_logo(self, driver):
        """Переход из личного кабинета в конструктор по логотипу"""
        # Входим и переходим в личный кабинет
        login(driver)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Ждем загрузки личного кабинета
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )
        
        # Нажимаем на логотип
        driver.find_element(By.XPATH, "//div[contains(@class, 'logo')]").click()
        
        # Проверяем что вернулись на главную
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()

    def test_logout(self, driver):
        """Выход из аккаунта"""
        # Входим и переходим в личный кабинет
        login(driver)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Ждем загрузки личного кабинета
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )
        
        # Нажимаем кнопку "Выход"
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
        
        # Проверяем что вернулись на страницу входа
        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Войти']"))
        )
        assert login_button.is_displayed()