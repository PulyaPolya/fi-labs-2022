from viginer import alphabets
class Cypher:
    def __init__(self, text, alphabet):
        self.text = text
        self.alphabet = alphabet
        self.r = self.get_r()
        self.n = len(self.text)
        self.blocks = self.get_blocks()
        self.coded_text = self.code_text(self.text)
    def get_D(self,r):
        D = 0
        for i in range(1, len(self.text) - r):
            if (self.text[i] == self.text[i + r]):
                D += 1
        return D

    def get_blocks(self):
        Y = []
        i = 0
        for i in range(self.r):
            y = []
            Y.append(y)

        for i in range(self.n):
            index = i % self.r
            if self.text[i] != '\n':
                Y[index].append(self.text[i])

        return Y

    def get_r(self):
        max = 0
        r = 0
        arr_d = []
        for i in range(6, 30):
            D = self.get_D(i)
            if D > max:
                max = D
                arr_d.append(D)
                r = i
        print('d is ', arr_d)
        return r

    def get_key_w_M(self):
        dict_frequency = self.alphabet.count_frequency(self.text, 'rus')
        arr_frequency = []
        for elem in dict_frequency:
            arr_frequency.append(dict_frequency[elem])
        k = []

        for y in self.blocks:
            dict_frequency = self.alphabet.count_frequency(y, 'rus')
            arr_frequency = []
            for elem in dict_frequency:
                arr_frequency.append(dict_frequency[elem])
            M = [0] * len(self.blocks)
            max_g = 0
            for g in range(32):
                sum = 0
                for t in range(32):
                    sum += list(self.alphabet.dict_russian_freq.items())[t][1] * arr_frequency[(t + g) % 32]
                if sum > M[self.blocks.index(y)]:
                    max_g = g
                    M[self.blocks.index(y)] = sum
            k.append(max_g)
        return k

    def get_key_w_freq(self):
        k = []
        print(self.alphabet.dict_rus_alph)
        for y in self.blocks:
            dict_freq = self.alphabet.count_frequency(y, 'rus')
            max = 0
            letter_o = ''
            for elem in dict_freq:
                if dict_freq[elem] > max:
                    max = dict_freq[elem]
                    letter_o = elem
            k_i = (self.alphabet.russ_alphabet.index(letter_o) - 8) % 32
            k.append(k_i)


        return (k)

    def code_text(self, txt):
        arr = []
        for elem in txt:
            ind = self.alphabet.russ_alphabet.index(elem)
            arr.append(ind)
        return arr

    def decode_text(self, arr):
        result = ''
        for elem in arr:
            result += self.alphabet.russ_alphabet[elem]
        return result

    def get_orig_text(self, key_arr, text_arr):
        orig_arr = []
        for i in range(self.n):
            ind = i % self.r
            new_elem = (text_arr[i] - key_arr[ind]) % 32
            orig_arr.append(new_elem)
        orig_text = self.decode_text(orig_arr)
        return orig_text

    def get_key_w_M(self):
        dict_frequency = self.alphabet.count_frequency(text, 'rus')
        arr_frequency = []
        for elem in dict_frequency:
            arr_frequency.append(dict_frequency[elem])
        k = []

        for y in self.blocks:
            dict_frequency = v.count_frequency(y, 'rus')
            arr_frequency = []
            for elem in dict_frequency:
                arr_frequency.append(dict_frequency[elem])
            M = [0] * len(self.blocks)
            max_g = 0
            for g in range(32):
                sum = 0
                for t in range(32):
                    sum += list(v.dict_russian_freq.items())[t][1] * arr_frequency[(t + g) % 32]
                if sum > M[self.blocks.index(y)]:
                    max_g = g
                    M[self.blocks.index(y)] = sum
            k.append(max_g)
        return k


f = open('cc', encoding = "UTF-8")
text = f.read()
f.close()
v = alphabets()
c = Cypher(text, v)
key = 'улановсеребряныепули'
key_arr = c.code_text(key)
key_arr1= c.get_key_w_M()
print(c.decode_text(key_arr1))
#text_arr =c.code_test(text)
txt = c.get_orig_text(key_arr, c.coded_text)
for i in range(len(txt)):
    print(txt[i], end='')

#print(code_test(text))