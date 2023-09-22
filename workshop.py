class Translator_dict:
    def __init__(self, word='program'):
        self.word = word
        self.russian_dict = {"я": "I", "яблоко": "apple", 'банан': "banana", 'город': 'city', 'человек': 'human'}
        self.english_dict = {'program': 'программа', 'technology': 'технология', 'innovation': 'инновация',
                        'super man': 'супермен'}

    def translate_text(self):
        if self.word in self.english_dict:
                translate_word = self.english_dict[self.word]
                return translate_word
        if self.word in self.russian_dict:
                translate_word = self.russian_dict[self.word]
                return translate_word
        else:
            return 'No word in the dictionary'

obj = Translator_dict('яблоко')
print(obj.translate_text())