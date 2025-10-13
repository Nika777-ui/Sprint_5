import pytest
from selenium.webdriver.common.by import By
import time

class TestLogin:
    def test_login_via_main_page_button(self, driver):
        try:
            """Вход по кнопке 'Войти в аккаунт' на главной"""
            driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
            
            email_field = driver.find_element(By.XPATH, "//input[@name='name']")
            password_field = driver.find_element(By.XPATH, "//input[@name='Пароль']")
            
            email_field.send_keys("Chasnaya_32@gmail.com")
            password_field.send_keys("Chasnaya_32@gmail.com")
            
            driver.find_element(By.XPATH, "//button[text()='Войти']").click()
            
            time.sleep(3)
            
            # Проверяем успешный вход
            login_buttons = driver.find_elements(By.XPATH, "//button[text()='Войти в аккаунт']")
            assert len(login_buttons) == 0, "Кнопка 'Войти в аккаунт' все еще отображается"
        finally:
            driver.quit()

    def test_login_via_personal_account_button(self, driver):
        try:
            """Вход через кнопку 'Личный кабинет'"""
            driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
            
            email_field = driver.find_element(By.XPATH, "//input[@name='name']")
            password_field = driver.find_element(By.XPATH, "//input[@name='Пароль']")
            
            email_field.send_keys("Chasnaya_32@gmail.com")
            password_field.send_keys("Chasnaya_32@gmail.com")
            
            driver.find_element(By.XPATH, "//button[text()='Войти']").click()
            
            time.sleep(3)
            
            login_buttons = driver.find_elements(By.XPATH, "//button[text()='Войти в аккаунт']")
            assert len(login_buttons) == 0
        finally:
            driver.quit()

    def test_login_via_register_page(self, driver):
        try:
            """Вход через кнопку в форме регистрации"""
            # Переходим на страницу регистрации
            driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
            driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()
            
            # Нажимаем "Войти" на странице регистрации
            driver.find_element(By.XPATH, "//a[text()='Войти']").click()
            
            # Заполняем форму входа
            email_field = driver.find_element(By.XPATH, "//input[@name='name']")
            password_field = driver.find_element(By.XPATH, "//input[@name='Пароль']")
            
            email_field.send_keys("Chasnaya_32@gmail.com")
            password_field.send_keys("Chasnaya_32@gmail.com")
            
            driver.find_element(By.XPATH, "//button[text()='Войти']").click()
            
            time.sleep(3)
            
            login_buttons = driver.find_elements(By.XPATH, "//button[text()='Войти в аккаунт']")
            assert len(login_buttons) == 0
        finally:
            driver.quit()

    def test_login_via_password_recovery(self, driver):
        try:
            """Вход через кнопку в форме восстановления пароля"""
            # Переходим на страницу входа
            driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
            
            # Нажимаем "Восстановить пароль"
            driver.find_element(By.XPATH, "//a[text()='Восстановить пароль']").click()
            
            # Нажимаем "Войти" на странице восстановления
            driver.find_element(By.XPATH, "//a[text()='Войти']").click()
            
            # Заполняем форму входа
            email_field = driver.find_element(By.XPATH, "//input[@name='name']")
            password_field = driver.find_element(By.XPATH, "//input[@name='Пароль']")
            
            email_field.send_keys("Chasnaya_32@gmail.com")
            password_field.send_keys("Chasnaya_32@gmail.com")
            
            driver.find_element(By.XPATH, "//button[text()='Войти']").click()
            
            time.sleep(3)
            
            login_buttons = driver.find_elements(By.XPATH, "//button[text()='Войти в аккаунт']")
            assert len(login_buttons) == 0
        finally:
            driver.quit()