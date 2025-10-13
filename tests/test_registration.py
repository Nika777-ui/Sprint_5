import pytest
from selenium.webdriver.common.by import By
from data.generators import generate_email, generate_password, generate_name
import time

class TestRegistration:
    def test_successful_registration(self, driver):
        try:
            # Переходим на страницу регистрации
            driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
            driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()
            
            # Заполняем форму регистрации
            name_field = driver.find_element(By.XPATH, "//input[@name='name']")
            email_field = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input")
            password_field = driver.find_element(By.XPATH, "//input[@name='Пароль']")
            
            # Используем генераторы
            name_field.send_keys(generate_name())
            email_field.send_keys(generate_email())
            password_field.send_keys(generate_password(6))
            
            # Нажимаем кнопку регистрации
            driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
            
            time.sleep(3)
            
            # Проверяем что перешли на страницу входа
            login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
            assert login_button.is_displayed()
        finally:
            driver.quit()

    def test_registration_with_short_password_error(self, driver):
        try:
            # Переходим на страницу регистрации
            driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
            driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()
            
            # Заполняем форму с коротким паролем
            name_field = driver.find_element(By.XPATH, "//input[@name='name']")
            email_field = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input")
            password_field = driver.find_element(By.XPATH, "//input[@name='Пароль']")
            
            # Используем генераторы
            name_field.send_keys(generate_name())
            email_field.send_keys(generate_email())
            password_field.send_keys(generate_password(5))  # короткий пароль
            
            # Нажимаем кнопку регистрации
            driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
            
            # Проверяем что появилась ошибка
            error_message = driver.find_element(By.XPATH, "//p[contains(@class, 'input__error')]")
            assert error_message.is_displayed()
            assert "Некорректный пароль" in error_message.text
        finally:
            driver.quit()