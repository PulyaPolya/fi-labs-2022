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

# initial_arr = [0]*30
# start = time.time()
# res = add_one(initial_arr)
# while res != 'end':
#     res = add_one(initial_arr)
#     print(''.join(str(e) for e in res))
#
# end = time.time()
# print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(end-start)))