class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет, и я живу в {self.location}.")


class Teenager(Person):
    def __init__(self, name, age, location, school):
        super().__init__(name, age, location)
        self.school = school

    def study(self):
        print(f"Я учусь в {self.school} и учусь очень старательно!")


class Adult(Person):
    def __init__(self, name, age, location, job):
        super().__init__(name, age, location)
        self.job = job

    def work(self):
        print(f"Я работаю {self.job} и стремлюсь стать мидл разработчиком.")
