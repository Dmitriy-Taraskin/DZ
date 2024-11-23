
# Исходный кортеж
cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")

# Заменяем "Экшн" на "Боевик"
updated_genres = list(cinema_genres)
updated_genres[1] = "Боевик"

# Добавляем новый жанр (например, "Фэнтези") между "Боевик" и "Пеплум"
updated_genres.insert(2, "Фэнтези")

# Преобразуем обратно в кортеж
cinema_genres_updated = tuple(updated_genres)

# Преобразуем кортеж в строку
cinema_genres_str = ", ".join(cinema_genres_updated)

# Вывод
print(f"Обновленные жанры кино: {cinema_genres_updated}")
print(f"Обновленные жанры кино: {cinema_genres_str}")