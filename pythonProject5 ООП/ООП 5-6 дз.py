import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def circumference(self):
        return 2 * math.pi * self._radius

    def area(self):
        return math.pi * (self._radius ** 2)


class Square:
    def __init__(self, diameter):
        self._diameter = diameter

    def get_diameter(self):
        return self._diameter

    def set_diameter(self, diameter):
        self._diameter = diameter

    def side(self):
        return self._diameter

    def area(self):
        return self._diameter ** 2


class InscribedCircleInSquare(Circle, Square):
    def __init__(self, radius):
        Circle.__init__(self, radius)
        Square.__init__(self, radius * 2)


# Пример использования
shape = InscribedCircleInSquare(5)

print(f"Радиус окружности: {shape.get_radius()}")
print(f"Длина окружности: {shape.circumference():.2f}")
print(f"Площадь окружности: {shape.area():.2f}")
print(f"Сторона квадрата: {shape.side()}")
print(f"Площадь квадрата: {shape.area()}")

# Задача 8.2: «Автомобиль»

class Wheels:
    def __init__(self, material):
        self._material = material

    def get_material(self):
        return self._material

    def set_material(self, material):
        self._material = material


class Engine:
    def __init__(self, power):
        self._power = power

    def get_power(self):
        return self._power

    def set_power(self, power):
        self._power = power


class Doors:
    def __init__(self, count):
        self._count = count

    def get_count(self):
        return self._count

    def set_count(self, count):
        self._count = count


class Car(Wheels, Engine, Doors):
    def __init__(self, material, power, count):
        Wheels.__init__(self, material)
        Engine.__init__(self, power)
        Doors.__init__(self, count)


# Пример использования
car = Car("резина", "200 л.с.", 4)

print(f"Материал колес: {car.get_material()}")
print(f"Мощность двигателя: {car.get_power()}")
print(f"Количество дверей: {car.get_count()}")

# Задача 8.3: «Домашние животные»

class Pet:
    def __init__(self, name, pet_type):
        self._name = name
        self._type = pet_type

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в дочернем классе.")


class Dog(Pet):
    def __init__(self, name):
        super().__init__(name, "Собака")

    def get_sound(self):
        return "Гав-гав"


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Кошка")

    def get_sound(self):
        return "Мяу"


class Parrot(Pet):
    def __init__(self, name):
        super().__init__(name, "Попугай")

    def get_sound(self):
        return "Чирик-чирик"


class Hamster(Pet):
    def __init__(self, name):
        super().__init__(name, "Хомяк")

    def get_sound(self):
        return "Писк-писк"


# Пример использования
dog = Dog("Бобик")
print(f"{dog.get_name()} ({dog.get_type()}): {dog.get_sound()}")

cat = Cat("Мурка")
print(f"{cat.get_name()} ({cat.get_type()}): {cat.get_sound()}")

parrot = Parrot("Кеша")
print(f"{parrot.get_name()} ({parrot.get_type()}): {parrot.get_sound()}")

hamster = Hamster("Шустрик")
print(f"{hamster.get_name()} ({hamster.get_type()}): {hamster.get_sound()}")

# Задача 8.4: «Служащий»

class Employer:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    def print(self):
        return "This is Employer class."


class President(Employer):
    def print(self):
        return f"Президент {self._first_name} {self._last_name}, возраст: {self._age}"


class Manager(Employer):
    def print(self):
        return f"Менеджер {self._first_name} {self._last_name}, возраст: {self._age}"


class Worker(Employer):
    def print(self):
        return f"Работник {self._first_name} {self._last_name}, возраст: {self._age}"


# Пример использования
president = President("Иван", "Иванов", 50)
manager = Manager("Петр", "Петров", 35)
worker = Worker("Сергей", "Сергеев", 25)

print(president.print())
print(manager.print())
print(worker.print())

# Задача 8.5: Магические методы

class Employer:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    def __str__(self):
        return f"Служащий {self._first_name} {self._last_name}, возраст: {self._age}"

    def __int__(self):
        return self._age


class President(Employer):
    def __str__(self):
        return f"Президент {self._first_name} {self._last_name}, возраст: {self._age}"


class Manager(Employer):
    def __str__(self):
        return f"Менеджер {self._first_name} {self._last_name}, возраст: {self._age}"


class Worker(Employer):
    def __str__(self):
        return f"Работник {self._first_name} {self._last_name}, возраст: {self._age}"


# Пример использования
president = President("Иван", "Иванов", 50)
manager = Manager("Петр", "Петров", 35)
worker = Worker("Сергей", "Сергеев", 25)

print(str(president))  # Президент Иван Иванов, возраст: 50
print(int(manager))    # 35
print(str(worker))     # Работник Сергей Сергеев, возраст: 25