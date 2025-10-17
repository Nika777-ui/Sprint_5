import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.test_data import TestData
from pages.locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, PasswordRecoveryLocators

class TestLogin:
    
    @pytest.mark.parametrize("login_method", [
        "main_page",
        "personal_account", 
        "register_page",
        "password_recovery"
    ])
    def test_login_different_methods(self, driver, login_method):
        """Параметризованный тест входа разными способами"""
        
        if login_method == "main_page":
            # Вход по кнопке на главной
            driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
            
        elif login_method == "personal_account":
            # Вход через личный кабинет
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            
        elif login_method == "register_page":
            # Вход через страницу регистрации
            driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
            driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
            driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
            
        elif login_method == "password_recovery":
            # Вход через восстановление пароля
            driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
            driver.find_element(*LoginPageLocators.RECOVER_PASSWORD_LINK).click()
            driver.find_element(*PasswordRecoveryLocators.LOGIN_LINK).click()
        
        # Заполняем форму входа
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        password_field = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        
        email_field.send_keys(TestData.EMAIL)
        password_field.send_keys(TestData.PASSWORD)
        
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверяем успешный вход (кнопка "Войти в аккаунт" исчезает)
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(MainPageLocators.LOGIN_BUTTON)
        )
        
        # Дополнительная проверка - кнопка "Оформить заказ" появляется
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()