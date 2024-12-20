# Шаг 0: Создаем словари со словами
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

# Словарь уровней
levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

# Шаг 1: Получаем уровень сложности от пользователя
difficulty = input("Выберите уровень сложности: легкий, средний, тяжелый: ").strip().lower()

if difficulty == "легкий":
    words = words_easy
elif difficulty == "средний":
    words = words_medium
elif difficulty == "тяжелый":
    words = words_hard
else:
    print("Уровень сложности не выбран, устанавливается уровень по умолчанию: легкий")
    words = words_easy

# Шаг 2: Цикл по словам
answers = {}
print("\nНачнем игру!")
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

# Шаг 3: Выводим результаты
correct_words = [word for word, correct in answers.items() if correct]
incorrect_words = [word for word, correct in answers.items() if not correct]

print("\nПравильно отвечены слова:", " ".join(correct_words) if correct_words else "Нет")
print("Неправильно отвечены слова:", " ".join(incorrect_words) if incorrect_words else "Нет")

# Шаг 4: Выводим ранг пользователя
correct_count = len(correct_words)
user_level = levels.get(correct_count, "Нулевой")
print(f"\nВаш ранг: {user_level}")