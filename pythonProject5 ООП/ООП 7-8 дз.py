# Решение с использованием множественного наследования

# Компоненты ПК реализованы как отдельные классы

class PowerSupply:
    def __init__(self, power):
        self._power = power

    def get_power(self):
        return self._power

    def supply_power(self):
        return f"Подается напряжение мощностью {self._power} Вт."


class Motherboard:
    def __init__(self, chipset):
        self._chipset = chipset

    def get_chipset(self):
        return self._chipset

    def redistribute_power(self):
        return f"Материнская плата ({self._chipset}) перераспределяет напряжение."


class CPU:
    def __init__(self, frequency, cores):
        self._frequency = frequency
        self._cores = cores

    def get_cpu_info(self):
        return f"{self._cores}-ядерный процессор с частотой {self._frequency} ГГц."

    def activate_turbo_mode(self):
        return "Активирован турбо-режим процессора!"


class RAM:
    def __init__(self, capacity, frequency):
        self._capacity = capacity
        self._frequency = frequency

    def get_ram_info(self):
        return f"Оперативная память: {self._capacity} ГБ, частота {self._frequency} МГц."

    def load_data(self):
        return "Данные загружены в оперативную память."

    def unload_data(self):
        return "Данные выгружены из оперативной памяти."


class SSD:
    def __init__(self, capacity):
        self._capacity = capacity

    def get_ssd_info(self):
        return f"SSD накопитель объемом {self._capacity} ГБ."

    def save_data(self):
        return "Данные сохранены на SSD."

    def delete_data(self):
        return "Данные удалены с SSD."


class GPU:
    def __init__(self, model, memory):
        self._model = model
        self._memory = memory

    def get_gpu_info(self):
        return f"Видеокарта {self._model}, объем памяти {self._memory} ГБ."

    def render_image(self):
        return "Изображение выведено на экран."


class PersonalComputer(PowerSupply, Motherboard, CPU, RAM, SSD, GPU):
    def __init__(self, power, chipset, cpu_frequency, cpu_cores, ram_capacity, ram_frequency, ssd_capacity, gpu_model, gpu_memory):
        PowerSupply.__init__(self, power)
        Motherboard.__init__(self, chipset)
        CPU.__init__(self, cpu_frequency, cpu_cores)
        RAM.__init__(self, ram_capacity, ram_frequency)
        SSD.__init__(self, ssd_capacity)
        GPU.__init__(self, gpu_model, gpu_memory)

    def get_pc_info(self):
        return "\n".join([
            self.supply_power(),
            self.redistribute_power(),
            self.get_cpu_info(),
            self.get_ram_info(),
            self.get_ssd_info(),
            self.get_gpu_info()
        ])


# Пример использования
pc = PersonalComputer(
    power=650,
    chipset="Intel Z590",
    cpu_frequency=3.5,
    cpu_cores=8,
    ram_capacity=16,
    ram_frequency=3200,
    ssd_capacity=1024,
    gpu_model="NVIDIA RTX 3080",
    gpu_memory=10
)

print(pc.get_pc_info())
print(pc.activate_turbo_mode())
print(pc.render_image())

# Решение с использованием композиции

# Компоненты как отдельные классы

class PowerSupply:
    def __init__(self, power):
        self._power = power

    def supply_power(self):
        return f"Подается напряжение мощностью {self._power} Вт."


class Motherboard:
    def __init__(self, chipset):
        self._chipset = chipset

    def redistribute_power(self):
        return f"Материнская плата ({self._chipset}) перераспределяет напряжение."


class CPU:
    def __init__(self, frequency, cores):
        self._frequency = frequency
        self._cores = cores

    def activate_turbo_mode(self):
        return "Активирован турбо-режим процессора!"


class RAM:
    def __init__(self, capacity, frequency):
        self._capacity = capacity
        self._frequency = frequency

    def load_data(self):
        return "Данные загружены в оперативную память."


class SSD:
    def __init__(self, capacity):
        self._capacity = capacity

    def save_data(self):
        return "Данные сохранены на SSD."


class GPU:
    def __init__(self, model, memory):
        self._model = model
        self._memory = memory

    def render_image(self):
        return "Изображение выведено на экран."


class PersonalComputer:
    def __init__(self, power, chipset, cpu_frequency, cpu_cores, ram_capacity, ram_frequency, ssd_capacity, gpu_model, gpu_memory):
        self.power_supply = PowerSupply(power)
        self.motherboard = Motherboard(chipset)
        self.cpu = CPU(cpu_frequency, cpu_cores)
        self.ram = RAM(ram_capacity, ram_frequency)
        self.ssd = SSD(ssd_capacity)
        self.gpu = GPU(gpu_model, gpu_memory)

    def get_pc_info(self):
        return "\n".join([
            self.power_supply.supply_power(),
            self.motherboard.redistribute_power(),
            f"Процессор: {self.cpu._cores}-ядерный, частота {self.cpu._frequency} ГГц.",
            f"ОЗУ: {self.ram._capacity} ГБ, частота {self.ram._frequency} МГц.",
            f"SSD: объем {self.ssd._capacity} ГБ.",
            f"Видеокарта: {self.gpu._model}, объем памяти {self.gpu._memory} ГБ."
        ])


# Пример использования
pc = PersonalComputer(
    power=750,
    chipset="AMD X570",
    cpu_frequency=4.2,
    cpu_cores=12,
    ram_capacity=32,
    ram_frequency=3600,
    ssd_capacity=2048,
    gpu_model="AMD Radeon RX 6800 XT",
    gpu_memory=16
)

print(pc.get_pc_info())
print(pc.cpu.activate_turbo_mode())
print(pc.gpu.render_image())