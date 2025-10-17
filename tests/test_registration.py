import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.generators import generate_email, generate_password, generate_name
from pages.locators import MainPageLocators, LoginPageLocators, RegisterPageLocators

class TestRegistration:
    def test_successful_registration(self, driver):
        """Успешная регистрация"""
        # Переходим на страницу регистрации через локаторы
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        
        # Заполняем форму регистрации
        name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT)
        )
        email_field = driver.find_element(*RegisterPageLocators.EMAIL_INPUT)
        password_field = driver.find_element(*RegisterPageLocators.PASSWORD_INPUT)
        
        # Используем генераторы
        name_field.send_keys(generate_name())
        email_field.send_keys(generate_email())
        password_field.send_keys(generate_password(6))
        
        # Нажимаем кнопку регистрации
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        # Ждем перехода на страницу входа
        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        assert login_button.is_displayed()

    def test_registration_with_short_password_error(self, driver):
        """Регистрация с коротким паролем - ошибка"""
        # Переходим на страницу регистрации через локаторы
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        
        # Заполняем форму с коротким паролем
        name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT)
        )
        email_field = driver.find_element(*RegisterPageLocators.EMAIL_INPUT)
        password_field = driver.find_element(*RegisterPageLocators.PASSWORD_INPUT)
        
        # Используем генераторы
        name_field.send_keys(generate_name())
        email_field.send_keys(generate_email())
        password_field.send_keys(generate_password(5))  # короткий пароль
        
        # Нажимаем кнопку регистрации
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        # Проверяем что появилась ошибка
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegisterPageLocators.ERROR_MESSAGE)
        )
        assert error_message.is_displayed()
        assert "Некорректный пароль" in error_message.text