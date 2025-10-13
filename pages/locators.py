from selenium.webdriver.common.by import By

# Главная страница
class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")

# Страница входа
class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    
    # Ссылки на другие формы
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

# Страница регистрации  
class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@name='name' and preceding-sibling::label[contains(text(),'Имя')]]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name' and preceding-sibling::label[contains(text(),'Email')]]")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")

# Личный кабинет
class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")

# Восстановление пароля
class PasswordRecoveryLocators:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")