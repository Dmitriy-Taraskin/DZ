
# Создаем кортежи
genres = ("Роман", "Новелла", "Фэнтези", "Научная Фантастика")
numbers = (3, 7, 9, 1, 6, 8, 2, 5, 4)

# Длины кортежей
length_genres = len(genres)
length_numbers = len(numbers)

# Максимальный и минимальный элемент
max_genre = max(genres)
min_genre = min(genres)
max_number = max(numbers)
min_number = min(numbers)

# Сумма элементов числового кортежа
sum_numbers = sum(numbers)

# Сортировка числового кортежа по возрастанию и убыванию
sorted_numbers_asc = tuple(sorted(numbers))
sorted_numbers_desc = tuple(sorted(numbers, reverse=True))

# Вывод
print(f"Длина кортежей: genres = {length_genres}, numbers = {length_numbers}")
print(f"Макс. и мин. в genres: {max_genre}, {min_genre}")
print(f"Макс. и мин. в numbers: {max_number}, {min_number}")
print(f"Сумма чисел: {sum_numbers}")
print(f"Сортировка по возрастанию: {sorted_numbers_asc}")
print(f"Сортировка по убыванию: {sorted_numbers_desc}")