import math
def evklid(a,n):
    arr_r = []
    arr_r.append(a)
    arr_r.append(n)
    arr_q = []
    arr_s = []
    arr_t = []
    arr_s.append(1)
    arr_s.append(0)
    arr_t.append(0)
    arr_t.append(1)
    r = -10
    while r != 1 or r !=0:
       r = arr_r[-2]%arr_r[-1]
       q = arr_r[-2] // arr_r[-1]
       arr_r.append(r)
       arr_q.append(q)
       s = arr_s[-2] - arr_q[-1] *arr_s[-1]
       t = arr_t[-2] - arr_q[-1] * arr_t[-1]
       arr_s.append(s)
       arr_t.append(t)
       #print(q,r,s,t)
       if r == 0:
           break
    return (arr_r[-2], arr_s[-2], arr_t [-2])

def get_minus(a , n):
    a = a %n
    d = math.gcd(a, n)
    if d == 1:
        r, s, t = evklid(a, n)

        a_minus = s
        return a_minus%n
    else:
        return ':('

def solve_linear_mod(a,b, n):
    a = a %n
    b = b %n
    d = math.gcd(a,n)

    if d == 1:
        r, s, t = evklid(a, n)
        a_minus = s
        x = (a_minus * b) % n
        return x
    else:
        if b % d != 0:
            return ':('
        else:
            a /= d
            b /= d
            n0 = n / d
            r, s, t = evklid(a, n0)
            a_minus = s
            x = (a_minus * b) % n0
            arr_x = []
            for i in range(d):
                x += n0
                arr_x.append(int(x%n))
            return arr_x


