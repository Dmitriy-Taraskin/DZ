class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self, stack_size=5, top=None):
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    def push(self, data):
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            print("Стэк переполнен")
            return "Стэк переполнен"

    def pop(self):
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    def is_empty(self):
        if self.top:
            return False
        else:
            return True

    def is_full(self):
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    def clear_stack(self):
        while self.top:
            self.pop()

    def get_data(self, index):
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    def size_stack(self):
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter


stack = Stack()
stack.push(1)
stack.push("sta")
stack.push(2)
stack.push(2.5)
stack.push("sta")
print(stack.counter_int())




class Node:
    """
    Класс для представления узла в связном списке.

    Атрибуты:
        data: Данные, хранящиеся в узле.
        next_node: Ссылка на следующий узел.
    """
    def __init__(self, data, next_node=None):
        """
        Инициализация узла.

        Аргументы:
            data: Данные для хранения в узле.
            next_node: Ссылка на следующий узел (по умолчанию None).
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """
    Класс для представления стека с фиксированным размером.

    Атрибуты:
        stack_size: Максимальный размер стека.
        top: Ссылка на верхний узел стека.
    """
    def __init__(self, stack_size=5):
        """
        Инициализация стека.

        Аргументы:
            stack_size: Максимальный размер стека (по умолчанию 5).
        """
        self.stack_size = stack_size
        self.top = None

    def push(self, data):
        """
        Добавление элемента в стек.

        Аргументы:
            data: Данные для добавления в стек.

        Возвращает:
            Сообщение об ошибке, если стек переполнен.
        """
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top
            self.top = new_node
        else:
            print("Стэк переполнен")
            return "Стэк переполнен"

    def pop(self):
        """
        Удаление элемента с вершины стека.

        Возвращает:
            Данные удаленного элемента или сообщение, если стек пуст.
        """
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    def is_empty(self):
        """
        Проверка, пуст ли стек.

        Возвращает:
            True, если стек пуст, иначе False.
        """
        return self.top is None

    def is_full(self):
        """
        Проверка, заполнен ли стек.

        Возвращает:
            True, если стек заполнен, иначе False.
        """
        return self.stack_size == self.size_stack()

    def clear_stack(self):
        """
        Очистка стека, удаляя все элементы.
        """
        while self.top:
            self.pop()

    def get_data(self, index):
        """
        Получение данных по индексу.

        Аргументы:
            index: Индекс элемента (начиная с вершины стека).

        Возвращает:
            Данные по указанному индексу или сообщение, если индекс вне диапазона.
        """
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return "Out of range"

    def size_stack(self):
        """
        Получение текущего размера стека.

        Возвращает:
            Количество элементов в стеке.
        """
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        """
        Подсчет количества целых чисел в стеке.

        Возвращает:
            Количество целых чисел в стеке.
        """
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter

# Написание тестов (используя unittest)

import unittest


class TestStack(unittest.TestCase):
    def setUp(self):
        """
        Настройка тестового окружения.
        """
        self.stack = Stack(stack_size=3)

    def test_push(self):
        """
        Тестирование метода push.
        """
        self.stack.push(1)
        self.assertEqual(self.stack.get_data(0), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.get_data(0), 2)
        self.assertEqual(self.stack.get_data(1), 1)
    def test_pop(self):
        """
        Тестирование метода pop.
        """
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), "Стэк пуст")

    def test_is_empty(self):
        """
        Тестирование метода is_empty.
        """
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_is_full(self):
        """
        Тестирование метода is_full.
        """
        self.stack.push(1)
        self.stack.push(2)
        self.assertFalse(self.stack.is_full())
        self.stack.push(3)
        self.assertTrue(self.stack.is_full())

    def test_clear_stack(self):
        """
        Тестирование метода clear_stack.
        """
        self.stack.push(1)
        self.stack.push(2)
        self.stack.clear_stack()
        self.assertTrue(self.stack.is_empty())

    def test_get_data(self):
        """
        Тестирование метода get_data.
        """
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.get_data(0), 2)
        self.assertEqual(self.stack.get_data(1), 1)
        self.assertEqual(self.stack.get_data(2), "Out of range")

    def test_size_stack(self):
        """
        Тестирование метода size_stack.
        """
        self.assertEqual(self.stack.size_stack(), 0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size_stack(), 2)

    def test_counter_int(self):
        """
        Тестирование метода counter_int.
        """
        self.stack.push(1)
        self.stack.push("test")
        self.stack.push(3)
        self.assertEqual(self.stack.counter_int(), 2)


if __name__ == "__main__":
    unittest.main()
