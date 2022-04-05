class Viginer:
    def __init__(self, text):
        self.alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя '
        self.dict_alph = {}
        for elem in self.alphabet:
            self.dict_alph[elem] = self.alphabet.index(elem)
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

    def count_frequency(self, y):
        dict_y_frequency = {}
        for elem in self.alphabet:
            dict_y_frequency[elem] = 0
        for i in y:
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