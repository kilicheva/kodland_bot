class Project:
    def __init__(self, name, description):
        self.__name = name  # Приватная переменная, доступная только внутри класса
        self.__description = description  # Приватная переменная, доступная только внутри класса
        self.__status = "В процессе выполнения"  # Приватная переменная, доступная только внутри класса

    def name(self):
        return self.__name  # Свойство для получения значения приватной переменной name

    @property
    def status(self):
        return self.__status  # Свойство для получения значения приватной переменной status

    @status.setter
    def status(self, new_status):
        if new_status in ["В процессе выполнения", "Завершен"]:
            self.__status = new_status  # Свойство для установки значения приватной переменной status

    def __str__(self):
        return f"Проект: {self.__name}, Статус: {self.__status}"

# Пример использования
project = Project("Веб-приложение", "Разработка онлайн-платформы")
print(project.name())  # Выводит: "Веб-приложение"
print(project.__status)  # Ошибка: AttributeError (приватная переменная недоступна вне класса)
project.status = "Завершен"
print(project)  # Выводит: "Проект: Веб-приложение, Статус: Завершен"
