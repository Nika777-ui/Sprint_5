import random
import string

def generate_email():
    """Генератор email-логинов в формате: имя_фамилия_номер_когорты_3цифры@домен"""
    names = ['ivan', 'alexey', 'dmitry', 'mikhail', 'sergey', 'andrey']
    surnames = ['ivanov', 'petrov', 'sidorov', 'smirnov', 'kuznetsov', 'popov']
    
    name = random.choice(names)
    surname = random.choice(surnames)
    cohort = "10"  # номер когорты
    digits = ''.join(random.choices(string.digits, k=3))
    
    domains = ['yandex.ru', 'ya.ru', 'gmail.com', 'mail.ru']
    domain = random.choice(domains)
    
    return f"{name}_{surname}_{cohort}_{digits}@{domain}"

def generate_password(length=6):
    """Генератор паролей"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_name():
    """Генератор имен"""
    names = ['Анна', 'Иван', 'Мария', 'Алексей', 'Екатерина', 'Дмитрий', 'Ольга', 'Сергей']
    return random.choice(names)