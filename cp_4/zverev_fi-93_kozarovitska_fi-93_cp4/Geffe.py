import vectors as v
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


