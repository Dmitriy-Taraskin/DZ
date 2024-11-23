
# Ваши вещи
my_items = {"нож", "спички", "фонарик", "веревка", "котелок", "аптечка", "карта", "тент", "еда", "вода"}

# Вещи близкого человека
close_items = {"фонарик", "вода", "аптечка", "удочка", "топор", "спальник", "еда", "компас", "палатка", "карта"}

# Анализ множеств
both_items = my_items & close_items  # Общие вещи
only_my_items = my_items - close_items  # Вещи только у вас
only_close_items = close_items - my_items  # Вещи только у близкого человека

# Вывод
print(f"Вещи, которые бы взяли вы двое: {both_items}")
print(f"Вещи, которые взяли бы только вы: {only_my_items}")
print(f"Вещи, которые взял бы близкий человек: {only_close_items}")