import random
import time
from random import randint

random.seed(time.localtime().tm_sec)

def get_mat(v, c):
    res = []

    for i in range(v):
        curr = []

        for j in range(c):
            num = randint(1, 6)
            curr.append(num)

        res.append(sum(curr) / c)

    return sum(res) / v

m1 = get_mat(100, 10)
m2 = get_mat(1000, 100)

def get_disp(m, v, c):
    res = []

    for i in range(v):
        curr = []

        for j in range(c):
            num = randint(1, 6)
            curr.append(abs(num - m) * abs(num - m))

        res.append(sum(curr) / c)

    return sum(res) / v

def get_disp2(m, v, c):
    res = []

    for i in range(v):
        n = randint(1, 6)
        res.append((n - m) * (n - m))

    return sum(res) / v

print(get_disp2(m1, 100, 10))
print(get_disp2(m2, 1000, 100))