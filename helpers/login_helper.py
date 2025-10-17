from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.test_data import TestData

def login(driver):
    """Вспомогательная функция для входа в аккаунт"""
    # Нажимаем кнопку "Войти в аккаунт"
    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    
    # Ждем появления полей ввода
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='name']"))
    )
    password_field = driver.find_element(By.XPATH, "//input[@name='Пароль']")
    
    # Вводим тестовые данные
    email_field.send_keys(TestData.EMAIL)
    password_field.send_keys(TestData.PASSWORD)
    
    # Нажимаем кнопку входа
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    
    # Ждем завершения входа
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//button[text()='Войти в аккаунт']"))
    )