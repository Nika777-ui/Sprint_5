import pytest
from selenium.webdriver.common.by import By
import time

class TestNavigation:
    def _login(self, driver):
        """Вспомогательный метод для входа"""
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        
        email_field = driver.find_element(By.XPATH, "//input[@name='name']")
        password_field = driver.find_element(By.XPATH, "//input[@name='Пароль']")
        
        email_field.send_keys("Chasnaya_32@gmail.com")
        password_field.send_keys("Chasnaya_32@gmail.com")
        
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        time.sleep(2)

    def test_go_to_personal_account(self, driver):
        try:
            """Переход в личный кабинет"""
            # Сначала выполняем вход
            self._login(driver)
            
            # Переходим в личный кабинет
            driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
            
            # Ждем загрузки
            time.sleep(2)
            
            # Проверяем что перешли в личный кабинет
            logout_button = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/nav/ul/li[3]/button")
            assert logout_button.is_displayed()
        finally:
            driver.quit()

    def test_go_from_account_to_constructor_via_button(self, driver):
        try:
            """Переход из личного кабинета в конструктор по кнопке"""
            # Входим и переходим в личный кабинет
            self._login(driver)
            driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
            time.sleep(2)
            
            # Нажимаем кнопку "Конструктор"
            driver.find_element(By.XPATH, "//p[text()='Конструктор']").click()
            
            # Проверяем что вернулись на главную
            order_button = driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")
            assert order_button.is_displayed()
        finally:
            driver.quit()

    def test_go_from_account_to_constructor_via_logo(self, driver):
        try:
            """Переход из личного кабинета в конструктор по логотипу"""
            # Входим и переходим в личный кабинет
            self._login(driver)
            driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
            time.sleep(2)
            
            # Нажимаем на логотип
            driver.find_element(By.XPATH, "//div[contains(@class, 'logo')]").click()
            
            # Проверяем что вернулись на главную
            order_button = driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")
            assert order_button.is_displayed()
        finally:
            driver.quit()

    def test_logout(self, driver):
        try:
            """Выход из аккаунта"""
            # Входим и переходим в личный кабинет
            self._login(driver)
            driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
            time.sleep(2)
            
            # Нажимаем кнопку "Выход"
            driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/nav/ul/li[3]/button").click()
            time.sleep(2)
            
            # Проверяем что вернулись на страницу входа
            login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
            assert login_button.is_displayed()
        finally:
            driver.quit()