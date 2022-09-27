import cProfile
import pickle
from scipy.stats import norm
import math
import pickle as pickle
import time
class Generator:
    def __init__(self, ni, change_key = True):
        self.ni = ni
        self.arr = []
        self.initial_key_list = []
        self.initial_key = -1
        self.change_key = change_key
        self.R = 0
    def set_key(self, key):
        self.key = key.copy()
        self.arr = []

    def return_init_key(self):
        return self.initial_key

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
        self.key.append(new_x)
        self.arr.append(self.key[0])
        self.key.pop(0)
        self.new_x = new_x
        # if self.change_key == False:
        self.initial_key = self.initial_key_list[0]


class L2_simplified(Generator):
    def generate(self):
        new_x = self.key[-26] ^ self.key[-25]^self.key[-24]^self.key[-20]
        self.key.append(new_x)
        self.arr.append(self.key[0])
        self.key.pop(0)
        self.new_x = new_x
        # if self.change_key == False:
        self.initial_key = self.initial_key_list[0]


class L3_simplified(Generator):
    def generate(self):
        new_x = self.key[-27] ^ self.key[-26]^self.key[-25]^self.key[-22]
        self.key.append(new_x)
        self.arr.append(self.key[0])
        self.key.pop(0)
        self.new_x = new_x
        self.initial_key = self.initial_key_list[0]


def count_F(s, x, y):
    return (s and x) ^ ((1 ^ s) and y)


def get_betta(ni):
    return 1 / (2 ** (ni + 1))


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
    R = 0
    for j in range(N_star):
        R += (z[j] ^ arr[j])
    return R


def create_good_generator(generator, numb_of_generator):
    if numb_of_generator == 1:
        good_generator = L1_simplified(generator.ni)
    elif numb_of_generator == 2:
        good_generator = L2_simplified(generator.ni)
    else:
        good_generator = L3_simplified(generator.ni)
    good_generator.initial_key = generator.initial_key.copy()
    good_generator.key = generator.key.copy()
    good_generator.arr = generator.arr.copy()
    good_generator.next_end = generator.next_end.copy()
    good_generator.change_key = False
    good_generator.initial_key_list = generator.initial_key_list.copy()
    return good_generator


def count_R_L(generator, z, numb_of_generator):
    z_arr = z[:int(generator.N) + 1]
    N_star = len(z_arr)
    arr_Li_candidates = []
    vector = [0] * (generator.ni - 1)
    vector.append(1)
    generator.set_key(vector.copy())
    generator.generate_first(N_star)
    dict_of_freq = {}
    R = count_R(z_arr, generator.arr, N_star)
    R_min = 1000
    if numb_of_generator == 1:
        C = 65
    else:
        C = generator.C
    # for j in range(N_star):
    #     R += (z_arr[j] ^ generator.arr[j])
    if R < C:
        if R in dict_of_freq:
            dict_of_freq[R] += 1
        else:
            dict_of_freq[R] = 1
        print(dict_of_freq)
        good_generator = create_good_generator(generator, numb_of_generator)
        good_generator.R = R
        arr_Li_candidates.append(good_generator)
        # print(generator.initial_key, good_generator.R)
    for i in range(2 ** generator.ni - 1):
        generator.generate_not_first()
        R = count_R(z_arr, generator.arr, N_star)
        # for j in range(N_star):
        #     R += (z_arr[j] ^ generator.arr[j])
        if R < C:

            if R in dict_of_freq:
                dict_of_freq[R] += 1
            else:
                dict_of_freq[R] = 1
            print(dict_of_freq)
            good_generator = create_good_generator(generator, numb_of_generator)
            good_generator.R = R
            arr_Li_candidates.append(good_generator)
        if R < R_min:
            R_min = R

    return arr_Li_candidates


def check_z(generator1, generator2, generator3, z, N_star):
    supposed_z = []
    key1, key2, key3= generator1.initial_key.copy(), generator2.initial_key.copy(), generator3.initial_key.copy()

    # l1 = L1_simplified(3)
    # l2 = L2_simplified(4)
    # l3 = L3_simplified(4)
    # key1 = [0, 0, 1]
    # l1.set_key(key1)
    # key2 = [0, 0, 0, 1]
    # l2.set_key(key2)
    # key3 = [0, 0, 0, 1]
    # l3.set_key(key3)
    # N = 100
    # l1.generate_first(N)
    # l2.generate_first(N)
    # l3.generate_first(N)
    # z1 = []
    # for i in range(N):
    #     zj = count_F(l3.arr[i], l1.arr[i], l2.arr[i])
    #     z1.append(zj)

    #print(key1, key2, key3)
    luck = False
    N2 = len(generator2.arr)
    N1 = len(generator1.arr)
    init_key = generator3.initial_key
    for i in range(N1):
        zi = count_F(generator3.arr[i],generator1.arr[i], generator2.arr[i])
        supposed_z.append(zi)
    if supposed_z == z[:N_star]:  #
        print('!!!!!!!!!!!')
        for i in range(N2 - N1):
            generator1.generate_not_first()
            generator3.generate_not_first()
            zn = count_F(generator3.arr[-1], generator1.arr[-1], generator2.arr[-((N2 - N1) - i)])
            if zn != z[N1+i]:
                return False
            supposed_z.append(zn)
        for j in range(N2, len(z)):
            generator1.generate_not_first()
            generator2.generate_not_first()
            generator3.generate_not_first()
            zn = count_F(generator3.arr[-1], generator1.arr[-1], generator2.arr[-1])
            if zn != z[j]:
                return False
            supposed_z.append(zn)
        print(key1, key2, key3)

    # print(supposed_z)
    # print(z)
    return luck

def check_z_dumb(generator1, generator2, generator3, z, N_star):
    supposed_z = []
    key1, key2, key3 = generator1.initial_key.copy(), generator2.initial_key.copy(), generator3.initial_key.copy()
    #print(key1, key2, key3)
    luck = False
    init_key = generator3.initial_key
    for i in range(N_star):
        zi = count_F(generator3.arr[i], generator1.arr[i], generator2.arr[i])
        supposed_z.append(zi)
    if supposed_z == z[:N_star]:  #
        print('!!!!!!!!!!!')
        right_bits = N_star
        generator1.set_key(generator1.initial_key)
        generator2.set_key(generator2.initial_key)
        generator3.set_key(init_key)

        generator1.generate_first(len(z))
        generator2.generate_first(len(z))
        generator3.generate_first(len(z))
        cand_z = []
        for i in range(len(z)):
            zi = count_F(generator3.arr[i], generator1.arr[i], generator2.arr[i])
            cand_z.append(zi)
            if zi != z[i]:
                luck = False
                break
            else:
                right_bits += 1
                luck = True
        if luck == True:
            print(key1, key2, key3)
            # print(generator1.initial_key, generator2.initial_key, generator3.initial_key)
    return luck

def create_gate_s(x, y, z, N_star):
    dict_ind = {}
    for i in range(N_star):
        if x.arr[i] != y.arr[i]:
            if z[i] == x.arr[i]:
                dict_ind[i] = 1
            elif z[i] == y.arr[i]:
                dict_ind[i] = 0
    return dict_ind


def create_gate_s(x, y, z, N_star):
    dict_ind = {}
    for i in range(N_star):
        if x.arr[i] != y.arr[i]:
            if z[i] == x.arr[i]:
                dict_ind[i] = 1
            elif z[i] == y.arr[i]:
                dict_ind[i] = 0
    return dict_ind


def check_gate(dict_ind, z_candidate, N_star):
    for i in range(N_star):
        if i in dict_ind:
            if z_candidate[i] != dict_ind[i]:
                return ':('
    return (':)')


def find_L3_v2(generator, arr_cand_l1, arr_cand_l2, z):
    N_star = min(len(arr_cand_l1[0].arr), len(arr_cand_l2[0].arr))
    z_arr = z[:N_star]

    for x in arr_cand_l1:
        for y in arr_cand_l2:

            dict_ind = create_gate_s(x, y, z_arr, N_star)
            vector = [0] * (generator.ni - 1)
            vector.append(1)
            generator.key = vector.copy()
            generator.initial_key = vector.copy()
            generator.generate_first(N_star)
            result = check_gate(dict_ind, generator.arr, N_star)
            if result == ':)':
                check_z(x, y, generator, z, N_star)
            for i in range(2 ** generator.ni - 1):
                generator.generate_not_first()
                result = check_gate(dict_ind, generator.arr, N_star)
                if result == ':)':
                    check_z(x, y, generator, z, N_star)
# key1 = [1,0,1]
# l1.set_key(key1)
# key2 = [1,0,1,1]
# l2.set_key(key2)
# key3 = [0,1,0,1]
# l3.set_key(key3)
# l1.generate_first(100)
# l2.generate_first(100)
# l3.generate_first(100)
# z_arr = []
# for i in range(100):
#     z = count_F(l3.arr[i], l1.arr[i], l2.arr[i])
#     z_arr.append(z)
# print(z_arr)
#
# f = open('z')
# arr_z_t = list(f)
# z = [int(x) for x in arr_z_t[0]]
# f = open('string')
f = '01111101101101010101110101011000010011111111011011001000000111101110101100000000011101101001110100000010100000010001101010000010010000011110011001111100001000011110111010000011110110100010110100001001010001111001001011111000010000110111011011010101100100000001000001111110000101101111110110011101100011001010100101101101111000110110001100001110111110101011110110000011000111001010000101010100111101000101100111111001100011010110111101111111001010110010101001010111001110110000111001010111011110101110111011011011011110000010110011111110101110001111010110010101111100000101110010011111001001010110010010011111011000110101100001100111101111111011110010000100001000011000000100000000101110111101111010010000011101010101110010011101110111111100110010011111011010001111000010110010111001110000100100011010011000110011100000000100010010001000101100110011001001000000001101011111000110110100101100011010101010110111110010000000111000100010001001010001010110010000111111010110011110000010111110101010110111101011100010011010100101000010011111001011011110100001011010000111010110111011010101110111100101101111101100111100000010000001101001101101000010110000100111110111001000101100011000010110100010000100000101011011010001011001110111100011100000001100001111100110001101010100010001001000100100010100011100100011111100001111111100011111000110110011001111101011101110100101000101101011000110011011001110001000011111001111010110000010110111000111010101001100011101011111100100111010011000000101110011110001100100010100110001100000111111111001111001110001100011101110111110111011010011101110000110110100000000000010010101001101110011010010000101111110010111000100110110110100100110010010011100010000101010001110110101001101100000010101010101110001100110000110110011000010110110111110010110010000101011010000111111000001111011000101000110000110000110000100011100000111001100100001010110110111010100101111000101110010111001101001011110111011011011111111010111011001110010000001000000110010010001001000110011001110001100010000001110010110111010011100111110001010'
arr_z_t = list(f)
z = [int(x) for x in arr_z_t[0]]
alpha = 0.01
arr_z_t = list(z)
z = [int(x) for x in arr_z_t]
l1 = L1_simplified(25)
l1.get_n_C()
cProfile.run('arr_cand_l1 = count_R_L(l1, z, 1)')
#arr_cand_l1 = count_R_L(l1, z, 1)
# start = time.time()



# l2 = L2_simplified(4)
# l2.get_n_C()
# l3 = L3_simplified(4)
# arr_cand_l2 = count_R_L(l2, z, 2)
# with open('cand_l1.pkl', 'wb') as outp:
#     for candidate in arr_cand_l1:
#         pickle.dump(candidate, outp, pickle.HIGHEST_PROTOCOL)
# with open('cand_l1.pkl', 'rb') as inp:
#     for i in range(len(arr_cand_l1)):
#         print(f'candidate {i}')
#         candidate = pickle.load(inp)
#         candidate.print_gen()
#find_L3_v2(l3, arr_cand_l1, arr_cand_l2, z)
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





