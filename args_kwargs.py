
# Пример 1: Использование *args для передачи произвольного количества аргументов
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))  # 6
print(sum_numbers(4, 5, 6, 7, 8))  # 30

# Пример 2: Использование **kwargs для передачи произвольного количества именованных аргументов
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=30, city="New York")

# Пример 3: Совмещение *args и **kwargs в одной функции
def mixed_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

mixed_function(1, 2, 3, name="Bob", age=25)

# Пример 4: Распаковка *args и **kwargs при вызове функции
def display_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

person_info = ("Alice", 30, "New York")
display_info(*person_info)

person_details = {"name": "Bob", "age": 25, "city": "Los Angeles"}
display_info(**person_details)
