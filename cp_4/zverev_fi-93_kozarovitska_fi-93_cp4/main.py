import scipy.stats as sps
import math
import vectors as v
def L1(x_i, x_i1, x_i4, x_i6):
    return x_i^ x_i1^ x_i4^ x_i6

def L2(y_i, y_i3):
    return y_i^ y_i3

def L3(s_i,s_i1, s_i2, s_i3, s_i5, s_i7 ):
    return s_i^ s_i1^ s_i2^ s_i3^ s_i5^ s_i7

def F(x, y, s):
    return (s and x) ^(1 ^ s) ^ y



def get_betta(n1):
    return (1 / (2**n1) - 0.001)

def count_N_C(n1,alpha, p1 = 0.25, p2 = 0.25):
    betta = get_betta(n1)
    t_betta = norm.ppf(1-betta, loc=0, scale=1)
    t_alpha = norm.ppf(1-alpha, loc=0, scale=1)
    N = t_betta*math.sqrt(p2*(1-p2)) + t_alpha*math.sqrt(p1*(1-p1))
    N /= (p2 - p1)
    N = N **2
    C = N*p1 + t_alpha * math.sqrt(N*p1*(1-p1))
    return N, C

def count_R(zi, n1):
    for i in range(n1):
        

arr = [1,0,1,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,1]
print(Geffe(arr, 10))