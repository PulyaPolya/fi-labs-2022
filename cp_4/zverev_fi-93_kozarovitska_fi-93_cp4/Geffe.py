import vectors as v
from scipy.stats import norm
import math
class Geffe :
    def __init__(self, n1, n2, n3, z):
        self.z = ''
        self.cypher_length = n1+ n2+ n3
        self.n_arr =[n1, n2, n3]
        self.z = z
        self.C_Arr =[]
        self.N_arr =[]

    def L1(self, x_i, x_i1, x_i4, x_i6):
        return x_i ^ x_i1 ^ x_i4 ^ x_i6

    def L2(self, y_i, y_i3):
        return y_i ^ y_i3

    def L3(self, s_i, s_i1, s_i2, s_i3, s_i5, s_i7):
        return s_i ^ s_i1 ^ s_i2 ^ s_i3 ^ s_i5 ^ s_i7

    def F(self, x, y, s):
        return (s and x) ^ (1 ^ s)^y
    def get_xi(self, arr, N):
        arr_x = arr[:]
        t = len(arr)
        for i in range(N):
            x = L1(arr_x[-30], arr_x[-29], arr_x[-26], arr_x[-24])
            arr_x.append(x)
        return arr_x[t:]
    def Geffe(self, arr):
        arr_x = arr[:]
        arr_y = arr[:]
        arr_s = arr[:]
        t = len(arr)
        for i in range(self.cypher_length):
            x = L1(arr_x[-30], arr_x[-29], arr_x[-26], arr_x[-24])
            arr_x.append(x)
            y = L2(arr_y[-31], arr_y[-28])
            arr_y.append(y)
            s = L3(arr_s[-32], arr_s[-31], arr_s[-30], arr_s[-29], arr_s[-27], arr_s[-25])
            arr_s.append(s)
        arr_z = []
        for i in range(t, len(arr_x)):
            z = F(arr_x[i], arr_y[i], arr_s[i])
            arr_z.append(z)

        return arr_z

    def get_betta(self, i):
        return 1 / (2 ** self.n_arr[i]) - 0.001

    def count_N_C_L(self, alpha,i, p1=0.25, p2=0.25):
        betta = get_betta(self, self.n_arr[i])
        t_betta = norm.ppf(1 - betta, loc=0, scale=1)
        t_alpha = norm.ppf(1 - alpha, loc=0, scale=1)
        N = t_betta * math.sqrt(p2 * (1 - p2)) + t_alpha * math.sqrt(p1 * (1 - p1))
        N /= (p2 - p1)
        N = N ** 2
        C = N * p1 + t_alpha * math.sqrt(N * p1 * (1 - p1))

        self.C = C
        self.N = N

    def count_R_L1(self,ni,  z):
        arr_Li_candidates =[]
        vector = [0]*ni
        N = len(z)
        while vector != 'end':
            sum = 0
            arr_x = self.get_xi(vector, N)
            for j in arr_x:
                sum += (z[j]^arr_x[j])
            if sum <= self.C:
                arr_Li_candidates.append(vector)
            vector = v.add_one(vector)

class Generator:
    def __init__(self, ni):
        self.ni = ni
        self.arr = []
    def set_key(self, key):
        self.key = key
        self.arr = []

    def get_n_C(self):
        N, C =count_N_C(self.ni)
        self.N = N
        self.C = C


class L1(Generator):
    # def __init__(self, ni):
    #     #self.key = key
    #     self.ni = ni
    #     #self.arr = key.copy()
    #
    # def get_arr(self, arr):
    #     self.arr = arr

    def generate(self):
        new_x = self.key[-30]^self.key[-29]^self.key[-26]^self.key[-24]
        #new_x = self.key[-1]^self.key[-2]
        self.key.append(new_x)
        self.arr.append(self.key[0])
        self.key.pop(0)

    # def get_n_C(self):
    #     N, C =count_N_C(self.n1)
    #     self.N = N
    #     self.C = C

class L2 (Generator):
    # def __init__(self, ni):
    #     #self.key = key
    #     self.ni = ni
    #     #self.arr = key.copy()

    def generate(self):
        new_x = self.key[-31]^self.key[-28]
        self.key.append(new_x)
        self.arr.append(self.key[0])
        self.key.pop(0)

    # def get_arr(self, arr):
    #     self.arr = arr
    # def get_n_C(self):
    #     N, C =count_N_C(self.n2)
    #     self.N = N
    #     self.C = C
        
class L3(Generator):
    # def __init__(self, ni):
    #     #self.key = key
    #     self.ni = ni
    #     # self.arr = key.copy()

    def generate(self):
        new_x = self.key[-32]^self.key[-31]^self.key[-30]^self.key[-29]^self.key[-27]^self.key[-25]
        self.key.append(new_x)
        self.arr.append(self.key[0])
        self.key.pop(0)
    # def get_n_C(self):
    #     N, C =count_N_C(self.n3)
    #     self.N = N
    #     self.C = C
def count_F( x, y, s):
    return (s and x) ^ (1 ^ s)^y

def get_betta(ni):
    return 1 / (2 ** ni)
def count_N_C(ni, p1=0.25, p2=0.5, alpha=0.01):
    betta = get_betta(ni)
    t_betta = norm.ppf(1 - betta, loc=0, scale=1)
    t_alpha = norm.ppf(1 - alpha, loc=0, scale=1)
    N = t_betta * math.sqrt(p2 * (1 - p2)) + t_alpha * math.sqrt(p1 * (1 - p1))
    N /= (p2 - p1)
    N = N ** 2
    C = N * p1 + t_alpha * math.sqrt(N * p1 * (1 - p1))
    return N, C

def count_R_L1(generator, z):
    z_arr = z[:int(generator.N)+1]
    N_star = len(z_arr)
    arr_Li_candidates =[]
    vector = [0]*generator.ni
    generator.set_key(vector)
    r= 0
    while vector != 'end':
        R = 0
        for n in range(N_star):
            generator.generate()
        for j in range(N_star):
            R += (z_arr[j]^generator.arr[j])
        if R < generator.C:
            arr_Li_candidates.append(vector)
            print(vector)
        vector = v.add_one(vector)
        generator.set_key(vector)
        r+= 1
    return arr_Li_candidates

f = open('z')
arr_z_t = list(f)
z = [int(x) for x in arr_z_t[0]]
alpha = 0.01
l1 = L1(30)
l2 = L2(31)
l3 = L3(32)
l1.get_n_C()
arr_cand_l1 = count_R_L1(l1, z)
print(arr_cand_l1)






