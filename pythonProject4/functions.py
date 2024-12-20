import json

# Загружаем данные из JSON
def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

# Получение уровня сложности
def get_user_level(user_lvl, words_data):
    user_lvl = user_lvl.strip().lower()
    if user_lvl in ["легкий", "easy"]:
        return words_data["easy"]
    elif user_lvl in ["средний", "medium"]:
        return words_data["medium"]
    elif user_lvl in ["тяжелый", "сложный", "hard"]:
        return words_data["hard"]
    else:
        print("Уровень сложности не выбран, устанавливается уровень по умолчанию: легкий")
        return words_data["easy"]

# Базовая программа тестирования
def base_program(words):
    answers = {}
    for word, translation in words.items():
        hint = f"{word}, {len(translation)} букв, начинается на {translation[0]}..."
        print(f"Программа: {hint}")
        user_answer = input("Ваш ответ: ").strip().lower()
        if user_answer == translation:
            print(f"Программа: Верно, {word.capitalize()} — это {translation}.")
            answers[word] = True
        else:
            print(f"Программа: Неверно. {word.capitalize()} — это {translation}.")
            answers[word] = False
    return answers

# Получение результатов
def get_result(answers, levels_data):
    correct_words = [word for word, correct in answers.items() if correct]
    incorrect_words = [word for word, correct in answers.items() if not correct]

    print("\nПравильно отвечены слова:", " ".join(correct_words) if correct_words else "Нет")
    print("Неправильно отвечены слова:", " ".join(incorrect_words) if incorrect_words else "Нет")

    correct_count = len(correct_words)
    user_level = levels_data.get(str(correct_count), "Нулевой")
    return user_level

# Сохранение результатов
def save_results(username, answers, filepath):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump({"username": username, "answers": answers}, file, ensure_ascii=False, indent=4)