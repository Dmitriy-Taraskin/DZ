# Исходный список
cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия", "пеплум"]

# Преобразуем список в множество
cinema_genres_set = set(cinema_genres)

# Добавляем 2 новых жанра
cinema_genres_set.add("драма")
cinema_genres_set.add("фэнтези")

# Удаляем жанр (например, "пеплум")
cinema_genres_set.discard("пеплум")

# Удаляем случайный жанр
cinema_genres_set.pop()

# Преобразуем множество обратно в список
cinema_genres_list = list(cinema_genres_set)

# Вывод
print(f"Обновленный список жанров: {cinema_genres_list}")