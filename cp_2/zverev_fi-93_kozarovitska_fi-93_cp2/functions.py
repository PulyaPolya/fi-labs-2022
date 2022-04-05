from viginer import alphabets


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


f = open('cc', encoding = "UTF-8")
text = f.read()
f.close()


#arr = get_key_w_freq(text)
#key = decode_text(arr)
#print(key)

key = 'улановсеребряныепули'
key_arr = code_test(key)
print(key_arr)
key_arr1= get_key_w_M(text)
print(key_arr1)
text_arr =code_test(text)
txt = get_orig_text(key_arr, text_arr)
for i in range(len(txt)):
    print(txt[i], end='')

print(code_test(text))