# Решение Задачи 8.1.1

class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, wheels):
        if wheels == 2:
            return f"Это мотоцикл марки {self.name}."
        elif wheels == 3:
            return f"Это трицикл марки {self.name}."
        elif wheels == 4:
            return f"Это автомобиль марки {self.name}."
        else:
            return f"Я не знаю таких ТС с {wheels} колесами."

    def get_vehicle_advice(self):
        if self.mileage < 50000:
            return f"Неплохо, {self.name} можно брать."
        elif 50001 <= self.mileage <= 100000:
            return f"{self.name} надо внимательно проверить."
        elif 100001 <= self.mileage <= 150000:
            return f"{self.name} надо провести полную диагностику."
        else:
            return f"{self.name} лучше не покупать."

# Создаем экземпляры класса
vehicle1 = Vehicle("BMW", 45000)
vehicle2 = Vehicle("Audi", 75000)
vehicle3 = Vehicle("Toyota", 120000)
vehicle4 = Vehicle("Lada", 160000)

# Проверяем методы
vehicles = [vehicle1, vehicle2, vehicle3, vehicle4]

for vehicle in vehicles:
    print(vehicle.get_vehicle_type(4))  # Все примеры с 4 колесами
    print(vehicle.get_vehicle_advice())

# Вывод:
#
# Это автомобиль марки BMW.
# Неплохо, BMW можно брать.
# Это автомобиль марки Audi.
# Audi надо внимательно проверить.
# Это автомобиль марки Toyota.
# Toyota надо провести полную диагностику.
# Это автомобиль марки Lada.
# Lada лучше не покупать.
#
# Решение Задачи 8.1.2
#
# Создадим класс Smartphone, который представляет смартфон.

class Smartphone:
    def __init__(self, brand, model, battery_life, storage):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # Время работы в часах
        self.storage = storage  # Память в ГБ

    def check_battery(self):
        if self.battery_life > 20:
            return f"{self.brand} {self.model}: Батарея в порядке, заряда хватает на {self.battery_life} часов."
        elif 10 <= self.battery_life <= 20:
            return f"{self.brand} {self.model}: Заряд батареи средний, заряда хватает на {self.battery_life} часов."
        else:
            return f"{self.brand} {self.model}: Батарея слабая, заряда хватает всего на {self.battery_life} часов."

    def check_storage(self):
        if self.storage >= 128:
            return f"{self.brand} {self.model}: Достаточно памяти, {self.storage} ГБ."
        elif 64 <= self.storage < 128:
            return f"{self.brand} {self.model}: Места хватает, {self.storage} ГБ."
        else:
            return f"{self.brand} {self.model}: Память ограничена, всего {self.storage} ГБ."

# Создаем экземпляры класса
smartphone1 = Smartphone("Apple", "iPhone 13", 25, 256)
smartphone2 = Smartphone("Samsung", "Galaxy S21", 15, 64)

# Проверяем методы
print(smartphone1.check_battery())
print(smartphone1.check_storage())
print(smartphone2.check_battery())
print(smartphone2.check_storage())

# Вывод:
#
# Apple iPhone 13: Батарея в порядке, заряда хватает на 25 часов.
# Apple iPhone 13: Достаточно памяти, 256 ГБ.
# Samsung Galaxy S21: Заряд батареи средний, заряда хватает на 15 часов.
# Samsung Galaxy S21: Места хватает, 64 ГБ.