import math
alpSpace = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#alpWSpace = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

f = open('3.txt', encoding = "UTF-8")
text = f.read()
for i in text:
    if i.isupper():
        text = text.replace(i, i.lower())
        i = i.lower()
    if i not in alpSpace:
        text = text.replace(i, '')
count = len(text)
def get_monodick():
    MonoDick = dict()
    for a in alpSpace:
        MonoDick[a] = 0

    for i in text:
        MonoDick[i] = MonoDick[i] + 1


    #count = 34
    for i in MonoDick:
        MonoDick[i] = MonoDick[i] / count
    return MonoDick




def get_Bidick(jump = 1):
    BiDick = dict()
    for i in alpSpace:
        for j in alpSpace:
            word = i + j
            BiDick[word] = 0
    numb = 0
    for j in range(0, count-1, jump):

        if text[j] + text[j + 1] in BiDick:
            BiDick[text[j] + text[j + 1]] += 1

    for i in BiDick:
        numb+= BiDick[i]
    for i in BiDick:
       BiDick[i] = BiDick[i] / (numb)
    return BiDick
def count_H(Dick):
    n = len(Dick)
    H=0
    for elem in Dick:
        if Dick[elem]!=0.0:
            H=H-Dick[elem]*math.log(Dick[elem],2)
            #print(Dick[elem],H, elem)
    return H

#print(MonoDick)
BiDick_w_croses = get_Bidick(jump=2)
print(BiDick_w_croses)
print(BiDick_w_croses)
MonoDick = get_monodick()
print(count_H(MonoDick))
#print(count_H(BiDick))
print(count_H(BiDick_w_croses))
f.close()


