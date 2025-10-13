import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Настройки Chrome
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # Создаем драйвер
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    # Переходим на сайт Stellar Burgers
    driver.get("https://stellarburgers.education-services.ru/")
    
    yield driver  # передаем драйвер в тест
    
    # Закрываем браузер после теста
    driver.quit()