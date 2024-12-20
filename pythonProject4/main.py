
import os
from functions import load_data, get_user_level, base_program, get_result, save_results

# Шаг 0: Загружаем данные
words_data = load_data("words.json")
levels_data = load_data("levels.json")

# Шаг 1: Спрашиваем имя пользователя
username = input("Введите ваше имя: ").strip()

# Шаг 2: Выбираем уровень сложности
user_lvl = input("Выберите уровень сложности: легкий, средний, сложный.\n").lower()
test_words = get_user_level(user_lvl, words_data)

# Шаг 3: Запускаем тест
test_answers = base_program(test_words)

# Шаг 4: Получаем результат
result = get_result(test_answers, levels_data)

# Шаг 5: Сохраняем результат
results_folder = "results"
os.makedirs(results_folder, exist_ok=True)
result_filepath = os.path.join(results_folder, f"{username}.json")
save_results(username, test_answers, result_filepath)

# Шаг 6: Выводим итог
print(f"\nВаш ранг: {result}")
print(f"Результаты сохранены в файле: {result_filepath}")