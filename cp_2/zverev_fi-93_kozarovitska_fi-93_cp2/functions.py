from alphabets import alphabets


def get_blocks(text, r):
    Y=[]
    n = len(text)
    i = 0
    for i in range(r):
        y = []
        Y.append(y)

    for i in range(n):
        index = i % r
        if text[i]!= '\n':
            Y[index].append(text[i])


    return Y

def get_D(r, y):
    D = 0
    for i in range (1,len(y)-r):
        if (y[i] == y[i+r]):
            D += 1
    return D

def get_r(y):
    max = 0
    r = 0
    arr_d = []
    for i in range (6,30):
        D = get_D(i, y)
        if D > max:
            max =D
            arr_d.append(D)
            r = i
    print('d is ', arr_d)
    return r

def get_key_w_M(text):
    r = get_r(text)
    Y = get_blocks(text,r)
    v = alphabets()
    dict_frequency = v.count_frequency(text, 'rus')
    #print(dict_frequency)
    arr_frequency = []
    for elem in dict_frequency:
        arr_frequency.append(dict_frequency[elem])
    k = []

    for y in Y:
        dict_frequency = v.count_frequency(y, 'rus')
        arr_frequency = []
        for elem in dict_frequency:
            arr_frequency.append(dict_frequency[elem])
        M = [0] * len(Y)
        max_g = 0
        for g in range(32):
            sum = 0
            for t in range (32):
                sum += list(v.dict_russian_freq.items())[t][1]*arr_frequency[(t+g)%32]
            if sum >  M[Y.index(y)]:
                max_g = g
                M[Y.index(y)] = sum
        k.append(max_g)
    return k

def get_key_w_freq(text):
    r = get_r(text)
    Y = get_blocks(text, r)
    v = alphabets()
    k= []
    print(v.dict_rus_alph)
    for y in Y:
        dict_freq = v.count_frequency(y, 'rus')
        max = 0
        letter_o = ''
        for elem in dict_freq:
            if dict_freq[elem] > max:
                max = dict_freq[elem]
                letter_o = elem
        k_i = (v.russ_alphabet.index(letter_o) - 8) % 32
        k.append(k_i)
    return (k)

def code_test(text):
    v = alphabets()
    print(v.dict_rus_alph)
    arr = []
    for elem in text:
        ind = v.russ_alphabet.index(elem)
        arr.append(ind)
    return arr

def decode_text(arr):
    v =  alphabets()

    result = ''
    for elem in arr:
        result+=v.russ_alphabet[elem]
    return result

def get_orig_text(key_arr, text_arr):
    r = len(key_arr)
    orig_arr = []
    for i in range (len(text_arr)):
        ind = i%r
        new_elem = (text_arr[i]- key_arr[ind])%32
        orig_arr.append(new_elem)
    orig_text = decode_text( orig_arr)
    return orig_text

def cypher(text, k):
    r = len(k)
    n = len(text)
    a =alphabets()
    arr_k = []
    arr_sypher = []
    arr_open = []
    for elem in text:
        index = a.dict_rus_alph[elem]
        arr_open.append(index)
    for elem in k:
        index = a.dict_rus_alph[elem]
        arr_k.append(index)
    for i in range(n):
        j = i % r
        index = (arr_open[i] + arr_k[j])%32
        arr_sypher.append(index)
    string_sypher=''
    for elem in arr_sypher:
        letter =a.russ_alphabet[elem]
        string_sypher+= letter
    return string_sypher


def count_I(y):
    a = alphabets()
    n = len(y)
    dict_y_frequency = a.count_frequency(y)
    I = 0
    for elem in dict_y_frequency:
        N = dict_y_frequency[elem]
        I += N*(N-1)
    I /= n*(n-1)
    return I
