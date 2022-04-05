import functions as f
from viginer import Viginer
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

'''
v = Viginer('фбвнффрвшішвршіфріщшвіфєвфврйцщшкгитьжфєжмтигршщушкгцамвщьіхцхвзлузауауауауауі')
k = 'абві'
res = v.cypher(k)
arr_sypher = res[0]
y = res[1]
v.count_frequency(y)
print(v.count_I(y))