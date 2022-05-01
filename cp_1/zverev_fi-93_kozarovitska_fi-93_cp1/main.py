import math
alpSpace = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#alpWSpace = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

f = open('TEXT.txt', encoding = "UTF-8")
text = f.read()
for i in text:
    if i.isupper():
        i = i.lower()
    if i not in alpSpace:
        text = text.replace(i, '')


MonoDick = dict()
for a in alpSpace:
    MonoDick[a] = 0

for i in text:
    MonoDick[i] = MonoDick[i] + 1

count = len(text)
#count = 34
for i in MonoDick:
    MonoDick[i] = MonoDick[i] / count

BiDick = dict()
for i in alpSpace:
    for j in alpSpace:
        word = i + j
        BiDick[word] = 0

for j in range(0, count-1, 1):
    if text[j] + text[j + 1] in BiDick:
        BiDick[text[j] + text[j + 1]] += 1
for i in BiDick:
   BiDick[i] = BiDick[i] / count
def count_H(Dick):
    n = len(Dick)
    H=0
    for elem in Dick:
        if Dick[elem]!=0.0:
            H=H-Dick[elem]*math.log(Dick[elem],2)
            #print(Dick[elem],H, elem)
    return H

#print(MonoDick)
print( BiDick)
#print(count_H(MonoDick))
#print(count_H(BiDick))
#print(count_H(BiDick,2))
f.close()
