import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators

class TestConstructor:
    
    @pytest.mark.parametrize("section_locator,expected_text", [
        (MainPageLocators.BUNS_SECTION, "Булки"),
        (MainPageLocators.SAUCES_SECTION, "Соусы"), 
        (MainPageLocators.FILLINGS_SECTION, "Начинки")
    ])
    def test_switch_sections(self, driver, section_locator, expected_text):
        """Параметризованный тест переключения разделов конструктора"""
        # Ждем пока раздел станет кликабельным
        section = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(section_locator)
        )
        
        # Используем JavaScript клик для обхода перекрытия
        driver.execute_script("arguments[0].click();", section)
        
        # Ждем и проверяем активный раздел
        active_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ACTIVE_SECTION)
        )
        
        # Проверяем что раздел активен
        assert expected_text in active_section.text