import random

# Шаг 0: Словари слов
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

# Уровни рангов
levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

# Шаг 1: Получение уровня сложности
difficulty = input("Выберите уровень сложности: легкий, средний, тяжелый (по умолчанию легкий): ").strip().lower()

if difficulty == "средний":
    words = words_medium
elif difficulty == "тяжелый":
    words = words_hard
else:
    words = words_easy

print(f"Выбран уровень сложности: {difficulty if difficulty in ['легкий', 'средний', 'тяжелый'] else 'легкий'}.\n")

# Шаг 2: Угадывание слов
answers = {}  # Словарь для хранения результатов
for english_word, russian_word in words.items():
    print(f"Переведите слово: {english_word}, {len(russian_word)} букв, начинается на {russian_word[0]}...")
    user_answer = input("Ваш ответ: ").strip().lower()

    if user_answer == russian_word:
        print(f"Верно, {english_word.capitalize()} — это {russian_word}.\n")
        answers[english_word] = True
    else:
        print(f"Неверно. {english_word.capitalize()} — это {russian_word}.\n")
        answers[english_word] = False

# Шаг 3: Вывод результатов
correct_words = [word for word, result in answers.items() if result]
incorrect_words = [word for word, result in answers.items() if not result]

print("Правильно отвечены слова:")
print("\n".join(correct_words) if correct_words else "Нет.")

print("\nНеправильно отвечены слова:")
print("\n".join(incorrect_words) if incorrect_words else "Нет.")

# Шаг 4: Ранг пользователя
correct_count = sum(answers.values())
user_rank = levels[correct_count]

print(f"\nВаш ранг: {user_rank}")