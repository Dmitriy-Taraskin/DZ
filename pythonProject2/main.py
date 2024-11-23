import os
import shutil

# 1. Указать в консоли нормализованный абсолютный путь к test_file_1.txt
file_1_path = os.path.abspath("data_path_1/test_file_1.txt")
print(f"Абсолютный путь к test_file_1.txt: {file_1_path}")

# 2. Содержимое проекта с использованием os.walk()
print("\nСодержимое проекта:")
for root, dirs, files in os.walk("."):
    print(f"Каталог: {root}")
    if dirs:
        print(f"Папки: {dirs}")
    if files:
        print(f"Файлы: {files}")

# 3. Составление абсолютного пути к test_file_3.txt
file_3_path = os.path.join(os.getcwd(), "data_path_2", "test_file_3.txt")
print(f"\nАбсолютный путь к test_file_3.txt: {file_3_path}")

# 4. Создание и удаление папки внутри data_path_2
new_folder_path = os.path.join("data_path_2", "new_folder")
os.makedirs(new_folder_path, exist_ok=True)  # Создать папку
print(f"\nПапка создана: {new_folder_path}")

# Удаление папки
if os.path.exists(new_folder_path):
    shutil.rmtree(new_folder_path)
    print(f"Папка удалена: {new_folder_path}")


# Задача 6.1.2: Работа с файлами

# Функция записи текста в файл
def write_poem_to_file(filepath):
    poem = """Если б мишки были пчелами,
То они бы нипочем,
Никогда и не подумали,
Так высоко строить дом."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(poem)

# Функция чтения текста из файла
def read_poem_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())

# Запись текста в test_file_1.txt
write_poem_to_file("data_path_1/test_file_1.txt")

# Чтение текста из test_file_1.txt
print("\nСодержимое test_file_1.txt:")
read_poem_from_file("data_path_1/test_file_1.txt")