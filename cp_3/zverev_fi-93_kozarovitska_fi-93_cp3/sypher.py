class Sypher:
    def __init__(self):
        f = open('text', encoding="UTF-8")
        self.text = f.read()

        f.close()
        self.alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
        self.letter_dict = self.get_letter_dict()
        self.mod = len(self.alphabet)
        for i in self.text:
            if i.isupper():
                i = i.lower()
            if i not in self.alphabet:
                self.text =self.text.replace(i, '')
    def get_letter_dict(self):
        MonoDick = {}
        for a in self.alphabet:
            MonoDick[a] = self.alphabet.index(a)
        return MonoDick

    def code_bigramm(self, s):
        m = self.mod
        first_dig = self.letter_dict[s[0]]
        second_dig = self.letter_dict[s[1]]
        res = (first_dig * m + second_dig) % m ** 2
        return (res)