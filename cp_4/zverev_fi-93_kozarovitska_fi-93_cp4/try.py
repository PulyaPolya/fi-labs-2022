import vectors as v
from scipy.stats import norm
import math
import time

def count_F(s, x, y):
    return (s and x) ^ ((1 ^ s) and y)
class Generator:
    def __init__(self, ni, change_key = True):
        self.ni = ni
        self.arr = []
        self.initial_key_list = []
        self.initial_key = -1
        self.change_key = change_key
        self.R = 0
    def set_key(self, key):
        self.key = key
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
        new_x = self.key[-1] ^ self.key[-2]
        #new_x = (self.key[-3] + self.key[2]) % 5
        self.key.append(new_x)
        self.arr.append(self.key[0])
        self.key.pop(0)
        self.new_x = new_x
        # if self.change_key == False:
        self.initial_key = self.initial_key_list[0]


class L2_simplified(Generator):
    def generate(self):
        new_x = self.key[-2] ^ self.key[-3]
        self.key.append(new_x)
        self.arr.append(self.key[0])
        self.key.pop(0)
        self.new_x = new_x
        # if self.change_key == False:
        self.initial_key = self.initial_key_list[0]


class L3_simplified(Generator):
    def generate(self):
        new_x = self.key[-1] ^ self.key[-2]
        self.key.append(new_x)
        self.arr.append(self.key[0])
        self.key.pop(0)
        self.new_x = new_x
        self.initial_key = self.initial_key_list[0]

l1 = L1_simplified(3)
l2 = L2_simplified(4)
l3 = L3_simplified(4)
key1 = [1,0,1]
l1.set_key(key1)
key2 = [1,0,1,0]
l2.set_key(key2)
key3 = [1,0,0,1]
l3.set_key(key3)
l1.generate_first(100)
l2.generate_first(100)
l3.generate_first(100)
z_arr = []
for i in range(100):
    z = count_F(l3.arr[i], l1.arr[i], l2.arr[i])
    z_arr.append(z)
print(z_arr)