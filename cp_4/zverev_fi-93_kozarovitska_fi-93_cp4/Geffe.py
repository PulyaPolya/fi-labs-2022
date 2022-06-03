class Geffe :
    def __init__(self, n):
        self.z = ''
        self.cypher_length = n

    def L1(self, x_i, x_i1, x_i4, x_i6):
        return x_i ^ x_i1 ^ x_i4 ^ x_i6

    def L2(self, y_i, y_i3):
        return y_i ^ y_i3

    def L3(self, s_i, s_i1, s_i2, s_i3, s_i5, s_i7):
        return s_i ^ s_i1 ^ s_i2 ^ s_i3 ^ s_i5 ^ s_i7

    def F(self, x, y, s):
        return (s and x) ^ (1 ^ s)^y

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