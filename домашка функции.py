# Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа между ними
def print_even_numbers(start, end):
    for num in range(start + 1, end):
        if num % 2 == 0:
            print(num)

# Пример использования
print_even_numbers(5, 15)

# Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа
def print_square(size, symbol, filled=True):
    for i in range(size):
        if filled:
            print(symbol * size)
        else:
            if i == 0 or i == size - 1:
                print(symbol * size)
            else:
                print(symbol + ' ' * (size - 2) + symbol)

# Пример использования
print_square(5, '*', True)   # Заполненный квадрат
print_square(5, '*', False)  # Пустой квадрат

from rich import print
from rich.align import Align
from rich.text import Text


# Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
def display_quote():
    # Создаем текст курсивом
    quote = Text("“Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.”",
                 style="italic")

    # Выводим текст с выравниванием по центру
    print(Align.center(quote))

    # Имя автора, выравненное вправо
    author = Text("Bill Gates", style="italic")
    print(Align.right(author))


# Вызов функции
display_quote()

# Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров.
def find_min_of_five(a, b, c, d, e):
    return min(a, b, c, d, e)

# Пример использования
print(find_min_of_five(10, 5, 7, 3, 9))


# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне
def product_in_range(start, end):
    # Меняем местами границы, если нужно
    if start > end:
        start, end = end, start
    product = 1
    for num in range(start, end + 1):
        product *= num
    return product

# Пример использования
print(product_in_range(5, 2))  # Произведение чисел от 2 до 5



def count_digits(number):
    return len(str(abs(number)))

# Пример использования
print(count_digits(3456))  # Вывод: 4


# 7. Функция для проверки, является ли число палиндромом:

def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]

# Пример использования
print(is_palindrome(123321))  # Вывод: True
print(is_palindrome(421987))  # Вывод: False