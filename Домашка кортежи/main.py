from utils import get_reg_data, reg_check

def main():
    # Храним данные о всех пользователях
    users_list = []

    # Запускаем цикл до тех пор, пока количество пользователей меньше 3
    while len(users_list) < 3:
        print(f"\nРегистрация пользователя {len(users_list) + 1}")
        user_data = []  # Данные текущего пользователя
        reg_data = get_reg_data()  # Получаем паттерны проверки

        # Цикл для ввода 4 данных: имя, email, телефон, пароль
        while len(user_data) < 4:
            if len(user_data) == 0:
                field = "name"
            elif len(user_data) == 1:
                field = "email"
            elif len(user_data) == 2:
                field = "phone"
            elif len(user_data) == 3:
                field = "password"

            # Запрашиваем данные у пользователя
            user_input = input(f"Введите {field}: ")

            # Проверяем уникальность для email и телефона
            if field in ["email", "phone"]:
                all_data = [u[len(user_data)] for u in users_list]
                is_valid = reg_check(user_input, reg_data[field], users_list, all_data)
            else:
                is_valid = reg_check(user_input, reg_data[field], users_list)

            # Если данные валидны, добавляем их, иначе просим ввести заново
            if is_valid:
                user_data.append(user_input)
                print(f"{field.capitalize()} успешно добавлен.")
            else:
                print(f"{field.capitalize()} введен некорректно или уже используется. Попробуйте снова.")

        # После ввода всех данных добавляем пользователя в список
        users_list.append(user_data)
        print(f"Пользователь {len(users_list)} успешно зарегистрирован!")

    print("\nРегистрация завершена. Список пользователей:")
    for i, user in enumerate(users_list, start=1):
        print(f"{i}. {user}")

if __name__ == "__main__":
    main()