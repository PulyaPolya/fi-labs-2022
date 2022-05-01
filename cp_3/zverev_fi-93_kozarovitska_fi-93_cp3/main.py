import lab_1 as l
import functions as func
alpWSpace = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
probab_dict = dict()
f = open('text', encoding = "UTF-8")
text = f.read()
count = len(text)
for i in alpWSpace:
    for j in alpWSpace:
        word = i + j
        probab_dict[word] = 0
for j in range(0, count-1, 1):
    if text[j] + text[j + 1] in probab_dict:
        probab_dict[text[j] + text[j + 1]] += 1
for i in probab_dict:
   probab_dict[i] = probab_dict[i] / count

#print(BiDick)

BiDick = l.get_bidick()
#print(BiDick)
keys = list(BiDick.keys())
val =[]

for k in keys:
    val.append(BiDick[k])
'''
m = max(val)
ind = val.index(m)
print(keys[ind])
print(BiDick[keys[ind]])
'''

max_bi = []

dict_letters = {}
#arr_bi = l.get_max(5, BiDick)
arr_syph = l.get_max(5, probab_dict)
arr_bi_true = ['ст', 'но', 'то', 'на', 'ен']
print(arr_syph)
#print(l.get_monodick())
i = 0
j = 0
def solve():
    for i in range(len(arr_bi_true)):
        m = len(alpWSpace)
        mod  = m**2
        for j in range(len(arr_bi_true)):
            x1 = l.code_bigramm(arr_bi_true[i])
            y1 = l.code_bigramm(arr_syph[j])
            for k in range(len(arr_bi_true)):
                for t in range(len(arr_bi_true)):
                    if k != i and j != t:
                        x2 = l.code_bigramm(arr_bi_true[k])
                        y2 = l.code_bigramm(arr_syph[t])

                        a = func.solve_linear_mod(a = y1 - y2, b= x1 - x2, n = mod )
                        b = (y1 - a * x1) % mod

