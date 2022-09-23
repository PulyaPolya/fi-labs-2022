import time

def add_one(vect):
    sum = 0
    for elem in vect:
        if elem == 1:
            sum += 1
    if sum == len(vect):
        return 'end'
    if vect[0] == 0:
        vect[0] = 1
        make_one = 0
        return vect
    else:
        i = 0
        while vect[i] != 0:
            if vect[i] == 0:
                vect[i] = 1
                #return vect
                break
            else:
                vect[i] = 0
                i += 1
                make_one = 1
        if make_one == 1:
            vect[i] = 1
        return vect

def count_F( s, x, y):
    return (s and x) ^ ((1 ^ s)and y)
# vector = [0]*3
# for i in range(8):
#     print(vector)
#     print(count_F(vector[0], vector[1], vector[2]))
#     vector = add_one(vector)
