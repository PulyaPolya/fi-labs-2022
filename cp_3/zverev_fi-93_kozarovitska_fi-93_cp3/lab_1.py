import functions as func
from sypher import Sypher
syph = Sypher()
def get_max(numb, d):
    arr = []
    dick = d.copy()
    for i in range(numb):
        m = max(dick, key=dick.get)
        arr.append(m)
        dick.pop(m)
    return arr

def code_bigramm(s):
    m = syph.mod
    first_dig = syph.letter_dict[s[0]]
    second_dig = syph.letter_dict[s[1]]
    res = (first_dig*m +second_dig) % m**2
    return (res)

def code():

    text = syph.text
    for i in text:
        if i.isupper():
            i = i.lower()
        if i not in syph.alphabet:
            text = text.replace(i, '')
    n = len(text)
    arr = []
    for i in range(0,n-1, 2):
        bigramm = text[i] + text[i+1]
        res = code_bigramm(bigramm)
        arr.append(res)
    return arr

def decode(arr_code, a, b, mod):
    arr_text = []
    a_minus = func.get_minus(a, mod)
    if a_minus != ':(':
        for elem in arr_code:
            t = a_minus*(elem - b)
            t = t %mod
            arr_text.append(t)
        return arr_text
    else:
        return ':('
def decode_bigramm(k, mod):
    x2 = k % mod
    x1 = int((k - x2) / mod)
    keys = list(syph.letter_dict.keys())

    return (keys[x1]+keys[x2])

def decode_text(arr_numb, mod):
    text = ''
    for elem in arr_numb:
        char =  decode_bigramm(elem, mod)
        text += char
    return text


def check_if_real(text):

    freq_text = {}

    for a in syph.alphabet:
        freq_text[a] = 0

    for i in text:
        freq_text[i] = freq_text[i] + 1

    count = len(text)
    for i in freq_text:
        freq_text[i] = freq_text[i] / count
    d ={'а': 0.07603640040444894, 'б': 0.011324570273003034, 'в': 0.04186046511627907, 'г': 0.014560161779575328, 'д': 0.0301314459049545, 'е': 0.0897876643073812, 'ё': 0.0, 'ж': 0.007077856420626896, 'з': 0.017189079878665317, 'и': 0.08270980788675429, 'й': 0.012740141557128413, 'к': 0.02891809908998989, 'л': 0.04044489383215369, 'м': 0.030940343781597573, 'н': 0.07421638018200202, 'о': 0.10637007077856421, 'п': 0.0224469160768453, 'р': 0.05055611729019211, 'с': 0.06188068756319515, 'т': 0.06895854398382205, 'у': 0.02062689585439838, 'ф': 0.0028311425682507585, 'х': 0.011122345803842264, 'ц': 0.007280080889787664, 'ч': 0.013346814964610718, 'ш': 0.005662285136501517, 'щ': 0.0034378159757330637, 'ъ': 0.0, 'ы': 0.01941354903943377, 'ь': 0.01820020222446916, 'э': 0.004651162790697674, 'ю': 0.0074823053589484325, 'я': 0.017795753286147624}
    if abs(freq_text['а'] -d['а'] )> 0.01 or abs(freq_text['о'] -d['о'] ) >0.01:
        return 'no'



