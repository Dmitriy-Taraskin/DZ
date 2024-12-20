class Teacher:
    def __init__(self, name, education, experience):
        self._name = name
        self._education = education
        self._experience = experience

    # Геттеры для всех атрибутов
    def get_name(self):
        return self._name

    def get_education(self):
        return self._education

    def get_experience(self):
        return self._experience

    # Сеттер для атрибута "опыт работы"
    def set_experience(self, experience):
        self._experience = experience

    # Метод get_teacher_data
    def get_teacher_data(self):
        return f"{self._name}, образование {self._education}, опыт работы {self._experience} года."

    # Метод add_mark
    def add_mark(self, student_name, mark):
        return f"{self._name} поставил оценку {mark} студенту {student_name}."

    # Метод remove_mark
    def remove_mark(self, student_name, mark):
        return f"{self._name} удалил оценку {mark} студенту {student_name}."

    # Метод give_a_consultation
    def give_a_consultation(self, class_name):
        return f"{self._name} провел консультацию в классе {class_name}."


# Создаем экземпляр класса Teacher
teacher = Teacher("Иван Петров", "БГПУ", 4)

# Проверяем методы
print(teacher.get_teacher_data())  # Иван Петров, образование БГПУ, опыт работы 4 года.
print(teacher.add_mark("Петр Сидоров", 4))  # Иван Петров поставил оценку 4 студенту Петр Сидоров.
print(teacher.remove_mark("Дмитрий Степанов", 3))  # Иван Петров удалил оценку 3 студенту Дмитрий Степанов.
print(teacher.give_a_consultation("9 Б"))  # Иван Петров провел консультацию в классе 9 Б.

# Решение Задачи 2

class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self._discipline = discipline
        self._job_title = job_title

    # Геттеры для новых атрибутов
    def get_discipline(self):
        return self._discipline

    def get_job_title(self):
        return self._job_title

    # Сеттер для атрибута "должность"
    def set_job_title(self, job_title):
        self._job_title = job_title

    # Адаптированный метод get_teacher_data
    def get_teacher_data(self):
        base_data = super().get_teacher_data()
        return f"{base_data}\nПредмет {self._discipline}, должность {self._job_title}"

    # Адаптированный метод add_mark
    def add_mark(self, student_name, mark):
        base_result = super().add_mark(student_name, mark)
        return f"{base_result}\nПредмет: {self._discipline}"

    # Адаптированный метод remove_mark
    def remove_mark(self, student_name, mark):
        base_result = super().remove_mark(student_name, mark)
        return f"{base_result}\nПредмет: {self._discipline}"

    # Адаптированный метод give_a_consultation
    def give_a_consultation(self, class_name):
        base_result = super().give_a_consultation(class_name)
        return f"{base_result}\nПо предмету {self._discipline} как {self._job_title}"


# Создаем экземпляр класса DisciplineTeacher
discipline_teacher = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "Директор")

# Проверяем методы
print(discipline_teacher.get_teacher_data())
# Иван Петров, образование БГПУ, опыт работы 4 года.
# Предмет Химия, должность Директор

print(discipline_teacher.add_mark("Николай Иванов", 4))
# Иван Петров поставил оценку 4 студенту Николай Иванов.
# Предмет: Химия

print(discipline_teacher.remove_mark("Дмитрий Сидоров", 3))
# Иван Петров удалил оценку 3 студенту Дмитрий Сидоров.
# Предмет: Химия

print(discipline_teacher.give_a_consultation("10 Б"))
# Иван Петров провел консультацию в классе 10 Б.
# По предмету Химия как Директор