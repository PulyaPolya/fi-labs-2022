import lab_1 as l
import functions as func
from sypher import Sypher
probab_dict = {}
syph = Sypher()

count = len(syph.text)
for i in syph.alphabet:
    for j in syph.alphabet:
        word = i + j
        probab_dict[word] = 0
for j in range(0, count-1, 1):
    if syph.text[j] + syph.text[j + 1] in probab_dict:
        probab_dict[syph.text[j] + syph.text[j + 1]] += 1
for i in probab_dict:
   probab_dict[i] = probab_dict[i] / count


arr_syph = l.get_max(5, probab_dict)
arr_bi_true = ['ст', 'но', 'то', 'на', 'ен']
print(arr_syph)

i = 0
j = 0
arr_code = l.code()
def solve():
    for i in range(len(arr_bi_true)):
        m = len(syph.alphabet)
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
                        if a!= ':(':
                            if isinstance(a, list):
                                for el in a:
                                    b = (y1 - el * x1) % mod
                                    arr_numb = l.decode(arr_code, el, b, mod)
                                    try:
                                        txt = l.decode_text(arr_numb, syph.mod)
                                    except:
                                        break
                                    real = l.check_if_real(txt)
                                    if real != 'no':
                                        print(i, j, k, t, txt)
                                        print(el, b)
                            else:
                                b = (y1 - a * x1) % mod
                                arr_numb = l.decode(arr_code, a, b, mod)
                                if arr_numb !=':(':
                                    txt = l.decode_text(arr_numb, syph.mod)
                                    real = l.check_if_real(txt)
                                    if real != 'no':
                                        print(i, j, k, t, txt)
                                        print(a, b)


solve()