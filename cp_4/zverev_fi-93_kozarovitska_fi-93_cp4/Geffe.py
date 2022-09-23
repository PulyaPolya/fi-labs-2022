import vectors as v
from scipy.stats import norm
import math
import time
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
    def __init__(self, ni, change_key = True):
        self.ni = ni
        self.arr = []
        self.initial_key_list = []
        self.initial_key = -1
        self.change_key = change_key
    def set_key(self, key):
        self.key = key
        self.arr = []

    def get_n_C(self):
        N, C =count_N_C(self.ni)
        self.N = N
        self.C = C

    def generate_first(self, N_star):
        self.initial_key_list.append(self.key.copy())
        self.generate()

        self.initial_key_list.append(self.key.copy())
        for n in range(N_star-1):
            self.generate()
            self.initial_key_list.append(self.key.copy())
        self.next_end = self.key
        if self.change_key == True:
            self.initial_key = self.initial_key_list[0]
            self.initial_key_list.pop(0)

    def generate_not_first(self):
        self.key = self.next_end
        #self.initial_key = self.key
        self.generate()
        self.arr.pop(0)
        self.next_end = self.key
        if self.change_key == True:
            self.initial_key_list.append(self.key.copy())
            self.initial_key = self.initial_key_list[0]
            self.initial_key_list.pop(0)

    def print_gen(self):
        print('\n generator')
        print(f"initial key {self.initial_key}" )
        print(f"key {self.key}")
        print(f'arr {self.arr}')




class L1_simplified(Generator):
    def generate(self):
        new_x = self.key[-25] ^ self.key[-22]
        #new_x = (self.key[-3] + self.key[2]) % 5
        self.key.append(new_x)
        self.arr.append(self.key[0])
        self.key.pop(0)
        self.new_x = new_x

class L2_simplified(Generator):
    def generate(self):
        new_x = self.key[-26] ^ self.key[-25]^self.key[-24]^self.key[-20]
        self.key.append(new_x)
        self.arr.append(self.key[0])
        self.key.pop(0)
        self.new_x = new_x

class L3_simplified(Generator):
    def generate(self):
        new_x = self.key[-27] ^ self.key[-26]^self.key[-25]^self.key[-22]
        self.key.append(new_x)
        self.arr.append(self.key[0])    
        self.key.pop(0)
        self.new_x = new_x
    


# class L1(Generator):
#     # def __init__(self, ni):
#     #     #self.key = key
#     #     self.ni = ni
#     #     #self.arr = key.copy()
#     #
#     # def get_arr(self, arr):
#     #     self.arr = arr
# 
#     def generate(self):
#         new_x = self.key[-30]^self.key[-29]^self.key[-26]^self.key[-24]
#         #new_x = self.key[-1]^self.key[-2]
#         self.key.append(new_x)
#         self.arr.append(self.key[0])
#         self.key.pop(0)
# 
#     # def get_n_C(self):
#     #     N, C =count_N_C(self.n1)
#     #     self.N = N
#     #     self.C = C
# 
# class L2 (Generator):
#     # def __init__(self, ni):
#     #     #self.key = key
#     #     self.ni = ni
#     #     #self.arr = key.copy()
# 
#     def generate(self):
#         new_x = self.key[-31]^self.key[-28]
#         self.key.append(new_x)
#         self.arr.append(self.key[0])
#         self.key.pop(0)
# 
#     # def get_arr(self, arr):
#     #     self.arr = arr
#     # def get_n_C(self):
#     #     N, C =count_N_C(self.n2)
#     #     self.N = N
#     #     self.C = C
#         
# class L3(Generator):
#     # def __init__(self, ni):
#     #     #self.key = key
#     #     self.ni = ni
#     #     # self.arr = key.copy()
# 
#     def generate(self):
#         new_x = self.key[-32]^self.key[-31]^self.key[-30]^self.key[-29]^self.key[-27]^self.key[-25]
#         self.key.append(new_x)
#         self.arr.append(self.key[0])
#         self.key.pop(0)
#     # def get_n_C(self):
#     #     N, C =count_N_C(self.n3)
#     #     self.N = N
#     #     self.C = C
def count_F( s, x, y):
    return (s and x) ^ ((1 ^ s)and y)

def get_betta(ni):
    return 1 / (2 ** (ni+1))
def count_N_C(ni, p1=0.25, p2=0.5, alpha=0.01):
    betta = get_betta(ni)
    t_betta = norm.ppf(1 - betta, loc=0, scale=1)
    t_alpha = norm.ppf(1 - alpha, loc=0, scale=1)
    N = t_betta * math.sqrt(p2 * (1 - p2)) + t_alpha * math.sqrt(p1 * (1 - p1))
    N /= (p2 - p1)
    N = N ** 2
    C = N * p1 + t_alpha * math.sqrt(N * p1 * (1 - p1))
    return N, C

def count_R(z, arr, N_star):
    R =0
    for j in range(N_star):
        R += (z[j] ^arr[j])
    return R

def create_good_generator(generator, numb_of_generator):
    if numb_of_generator == 1:
        good_generator = L1_simplified(generator.ni)
    elif numb_of_generator == 2:
        good_generator = L2_simplified(generator.ni)
    else:
        good_generator = L3_simplified(generator.ni)
    good_generator.initial_key=generator.initial_key.copy()
    good_generator.key = generator.key.copy()
    good_generator.arr = generator.arr.copy()
    good_generator.change_key = False
    return good_generator

def count_R_L(generator, z, numb_of_generator):
    z_arr = z[:int(generator.N) + 1]
    N_star = len(z_arr)
    arr_Li_candidates = []
    vector = [0] * (generator.ni -1)
    vector.append(1)
    generator.key = vector
    generator.generate_first(N_star)
    R = count_R(z_arr, generator.arr, N_star)
    R_min = 1000
    # for j in range(N_star):
    #     R += (z_arr[j] ^ generator.arr[j])
    if R < generator.C:
        good_generator = create_good_generator(generator, numb_of_generator)
        arr_Li_candidates.append(good_generator)
    for i in range(2**generator.ni-1):
        generator.generate_not_first()
        R = count_R(z_arr, generator.arr, N_star)
        # for j in range(N_star):
        #     R += (z_arr[j] ^ generator.arr[j])
        if R < generator.C:
            # if numb_of_generator == 1:
            #     good_generator = L1_simplified(generator.ni)
            # elif numb_of_generator == 2:
            #     good_generator = L2_simplified(generator.ni)
            # else:
            #     good_generator = L3_simplified(generator.ni)
            # good_generator.set_key(generator.initial_key)
            # good_generator.arr = generator.arr.copy()
            good_generator = create_good_generator(generator, numb_of_generator)
            arr_Li_candidates.append(good_generator)
            # good_generator.print_gen()
        if R < R_min:
            R_min = R
            print(R_min)
        #     end = time.time()
        #     print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(end-start)))
        #     start = time.time()
    return arr_Li_candidates

def check_z(generator1, generator2, generator3,z, N_star):
    supposed_z = []
    luck = True
    for i in range(N_star):
        zi = count_F(generator1.arr[i], generator2.arr[i], generator3.arr[i])
        supposed_z.append(zi)
    if supposed_z == z[:N_star]: #
        print('!!!!!!!!!!!')
        right_bits = N_star
        for i in range(N_star, len(z)):
            generator1.generate()
            generator2.generate()
            generator3.generate()
            zi = count_F(generator1.new_x, generator2.new_x, generator3.new_x)
            if zi !=  z[i]:
                luck = False
                break
            else:
                right_bits += 1
        if luck == True:
            print(generator1.initial_key, generator2.initial_key, generator3.initial_key)
    return luck

def find_L3(generator, arr_cand_l1, arr_cand_l2, z):
    N_star = min(len(arr_cand_l1[0].arr), len(arr_cand_l2[0].arr))
    z_arr = z[:N_star]
    vector = [0] * (generator.ni - 1)
    vector.append(1)
    generator.key = vector
    generator.generate_first(N_star)
    for i in range(2 ** generator.ni - 1):
        for x in arr_cand_l1:
            for y in arr_cand_l2:
                fits = True
                for i in range(N_star):
                    if x.arr[i] != y.arr[i]:
                        if z[i] == x.arr[i] and generator.arr[i]  == 1:
                            fits = True
                        elif z[i] == y.arr[i] and generator.arr[i] == 0:
                            fits = True
                        else:
                            fits = False
                            break
                if fits == False:
                    luck = check_z(x,y, generator, z, N_star)

f = open('z')
arr_z_t = list(f)
z = [int(x) for x in arr_z_t[0]]
alpha = 0.01
l1 = L1_simplified(25)
l1.get_n_C()
arr_cand_l1 = count_R_L(l1, z, 1)
l2 = L2_simplified(26)
l2.get_n_C()
arr_cand_l2 = count_R_L(l2, z, 2)
l3 = L3_simplified(27)
find_L3(l3, arr_cand_l1, arr_cand_l2, z)

# key = [1,2,3,4]
# arr_gen  =[]
# l1 = L1_simplified(4)
# l1.set_key(key)
# l1.generate_first(5)
# for i in range(5):
#     l1.generate_not_first()
#     R = 0
#     for j in range(len(l1.arr)):
#         R += l1.arr[j]
#     if R > 10:
#        generator = create_good_generator(l1, 1)
#        arr_gen.append(generator)
# for generator in arr_gen:
#     generator.print_gen()





