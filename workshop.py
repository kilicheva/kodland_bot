import string

from googletrans import Translator


class Translator_dict:
    # Инициализация объекта(конструктор)
    def __init__(self, word='program'):
        # Поля или атрибуты класса
        self.word = word
        # Экземпляр класса из библиотеки googletrans
        self.translator = Translator()

    # Метод класса
    def translate_text(self):
        if self.word[0].upper() in string.ascii_uppercase:
            translate_word = self.translator.translate(self.word, dest='ru').text
            return translate_word
        elif self.word[0].upper() not in string.ascii_uppercase:
            translate_word = self.translator.translate(self.word, dest='en').text
            return translate_word


obj = Translator_dict('How are you?')
print(obj.translate_text())
