import functions as func
from alphabets import alphabets
from cypher import Cypher
'''
alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя '
dict_alph = {}
for elem in alphabet:
    dict_alph[elem] = alphabet.index(elem)
print(dict_alph)
open_text = 'фбвнфі'
dict_open={}
arr_open = []
for elem in open_text:
    index= dict_alph[elem]
    dict_open[elem] = index
    arr_open.append(index)
print(dict_open)
print(arr_open)
k = 'абв'
dict_k={}
arr_k = []
for elem in k:
    index = dict_alph[elem]
    dict_k[elem] = index
    arr_k.append(index)
print(dict_k)
print(arr_k)
r = len(k)
n = len(open_text)
dict_sypher = {}
arr_sypher = []
keys_open = list(dict_open.keys())
keys_k = list(dict_k.keys())
for i in range (n):
    j = i %r
    index = arr_open[i] + arr_k[j]
    arr_sypher.append(index)
print(arr_sypher)
v = alphabets('фбвнффрвшішвршіфріщшвіфєвфврйцщшкгитьжфєжмтигршщушкгцамвщьіхцхвзлузауауауауауі')
k = 'абві'
res = v.cypher(k)
arr_sypher = res[0]
y = res[1]
v.count_frequency(y)
print(v.count_I(y))
f = open('cc', encoding = "UTF-8") ## getting text
text = f.read()
f.close()


'''


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

f = open('text', encoding = "UTF-8")
text = f.read()
f.close()
r_2 = "ок"
r_3 = "абв"
r_6 = "примат"
r_10 = "мандаринка"
r_18 = "машадождаласькогда"
print('\n')
cyphered_2 = func.cypher(text, r_2)
cyphered_18 = func.cypher(text, r_18)
cyphered_3 = func.cypher(text, r_3)
cyphered_10 = func.cypher(text, r_10)
cyphered_6 = func.cypher(text, r_6)
print(cyphered_2)
print(func.count_I(text))
print(func.count_I(cyphered_2))
print(func.count_I(cyphered_3))
print(func.count_I(cyphered_6))
print(func.count_I(cyphered_10))
print(func.count_I(cyphered_18))
print((cyphered_18))