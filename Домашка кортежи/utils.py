
import re

# Функция возвращает список паттернов для проверки данных
def get_reg_data():
    return {
        "name": r"^[A-Za-zА-Яа-я\s]{2,30}$",  # Имя: буквы и пробелы, длина от 2 до 30 символов
        "email": r"^[\w.-]+@[\w.-]+\.\w{2,}$",  # Email: стандартный формат
        "phone": r"^\+?[78]\d{10}$",  # Телефон: российский номер, начиная с +7 или 8
        "password": r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",  # Пароль: минимум 8 символов, буквы и цифры
    }

# Функция проверки уникальности данных (телефона и email)
def check_unique_data(user_data, data_to_check):
    return user_data not in data_to_check

# Основная функция проверки данных
def reg_check(user_data, reg_pattern, users_list, data_to_check=None):
    # Проверка формата данных
    if not re.match(reg_pattern, user_data):
        return False

    # Проверка уникальности, если это требуется
    if data_to_check is not None and not check_unique_data(user_data, data_to_check):
        return False

    return True