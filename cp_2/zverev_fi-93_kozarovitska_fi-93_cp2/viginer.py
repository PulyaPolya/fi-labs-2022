class Viginer:
    def __init__(self, text='фбвнффрвшішвршіфріщ'):
        self.alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя '
        self.russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        self.dict_russian_freq = {'а': 0.07998, 'б': 0.01592, 'в': 0.04533, 'г': 0.01687, 'д': 0.02977, 'е': 0.08483,  'ж':0.0094, 'з': 0.01641, 'и': 0.07367, 'й': 0.01208, 'к': 0.03486, 'л': 0.04343, 'м': 0.03203, 'н': 0.067, 'о': 0.10983, 'п': 0.02804, 'р': 0.04746, 'с': 0.05473, 'т': 0.06318, 'у': 0.02615, 'ф': 0.00267, 'х': 0.00966, 'ц': 0.00486, 'ч': 0.0145, 'ш': 0.00718, 'щ': 0.00361, 'ъ': 0.00037, 'ы': 0.01898, 'ь': 0.01735, 'э': 0.00331, 'ю': 0.00639, 'я': 0.02001, ' ': 0.145}
        self.arr_russ_freq = []
        for elem in self.dict_russian_freq:
            self.arr_russ_freq.append(self.dict_russian_freq[elem])
        self.dict_alph = {}
        for elem in self.alphabet:
            self.dict_alph[elem] = self.alphabet.index(elem)
        self.dict_rus_alph = {}
        for elem in self.russian_alphabet:
            self.dict_rus_alph[elem] = self.russian_alphabet.index(elem)
        self.open_text = text
        self.n = len(self.open_text)
        self.arr_open = []
        for elem in self.open_text:
            index = self.dict_alph[elem]
            self.arr_open.append(index)
    def cypher(self, k):
        r = len(k)
        arr_k = []
        arr_sypher = []
        for elem in k:
            index = self.dict_alph[elem]
            arr_k.append(index)
        for i in range(self.n):
            j = i % r
            index = (self.arr_open[i] + arr_k[j])%33
            arr_sypher.append(index)
        string_sypher=''
        for elem in arr_sypher:
            letter =self.alphabet[elem]
            string_sypher+= letter
        return (arr_sypher, string_sypher)

    def count_frequency(self, y, alph = 'ukr'):
        dict_y_frequency = {}
        if alph == 'rus':
            alph = self.russian_alphabet
        else:
            alph = self.alphabet
        for elem in alph:
            if elem != '\n':
                dict_y_frequency[elem] = 0
        for i in y:
            if i != '\n':
                dict_y_frequency[i] += 1
        return dict_y_frequency

    def count_I(self, y):
        dict_y_frequency = self.count_frequency(y)
        I = 0
        for elem in dict_y_frequency:
            N = dict_y_frequency[elem]
            I += N*(N-1)
        I /= self.n*(self.n-1)
        return I