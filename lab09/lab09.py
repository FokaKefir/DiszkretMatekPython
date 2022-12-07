import math
import random

# region 1. task

def extEuclid(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while True:
        q = a // b
        r = a - b * q
        if r == 0:
            return b, x1, y1
        x = x0 - q * x1
        y = y0 - q * y1
        x0, x1, y0, y1 = x1, x, y1, y
        a, b = b, r

def inverse_(a, m):
    d, x, y = extEuclid(a, m)
    if d != 1:
        return -1
    return x % m
    
def inverse(a, m):
    x0, x1 = 1, 0
    b = m
    while True:
        q = a // b
        r = a - b * q
        if r == 0:
            if b != 1: 
                return -1
            else: 
                return x1 % m
        x = x0 - q * x1
        x0, x1 = x1, x
        a, b = b, r

def task1():
    with open("lab09/szamok.txt", "rt") as fin:
        for row in fin.readlines():
            data = row.split(" ")
            a, m = int(data[0]), int(data[1])
            inv = inverse(a, m)
            print(a, m, ":", inv)

# endregion

# region 2. task

def linearCongruences(a, m, b):
    d, x, y = extEuclid(a, m)
    x0 = x * b // d
    lst = []
    for i in range(d):
        xk = (x0 + i * m // d) % m
        lst += [xk]
        if i > 10:
            lst += ["..."]
            break
    return lst


def task2():
    with open("lab09/szamokH.txt", "rt") as fin:
        for row in fin.readlines():
            data = row.split(" ")
            a, m, b = int(data[0]), int(data[1]), int(data[2])
            lst = linearCongruences(a, m, b)
            print(a, m, b, lst)
            
# endregion

# region 3. task

def millerRabinForX(m, s, r, x):
    y = pow(x, r, m)
    if y == 1 or y == (m - 1):
        return True
    for _ in range(s):
        y = (y ** 2) % m
        if y == 1:
            return False
        if y == m - 1:
            break
    if y != (m - 1):
        return False

def millerRabin(m, t=10):
    s = 0
    r = m - 1
    while (r & 1 == 0):
        s, r = s + 1, r >> 1
    for x in [3, 5, 7]:
        if m % x == 0:
            return False

    for _ in range(t - 3):
        x = random.randint(2, m - 1)
        if millerRabinForX(m, s, r, x) == False:
            return False
    return True

def isPrimeNumber(num):
    if num == 1:
        return False
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    k = 3
    while k * k <= num:
        if num % k == 0:
            return False
        k += 2
    return True

def calcEuler(x, m, eulerF):
    ok = 0
    while m % x == 0:
        m = m // x
        ok = 1
    if ok != 0: 
        eulerF = eulerF // x * (x - 1)
    return m, eulerF

def euler(m):
    eulerF = m
    m, eulerF = calcEuler(2, m, eulerF)
    m, eulerF = calcEuler(3, m, eulerF)
    x = 5
    while x * x <= m:
        m, eulerF = calcEuler(x, m, eulerF)
        m, eulerF = calcEuler(x + 2, m, eulerF)
        x += 6
    if m > 4: 
        eulerF = eulerF // m * (m - 1)
    return eulerF

def inverseEuler(a, m):
    if math.gcd(a, m) != 1:
        return -1
    if millerRabin(m):
        return (a ** (m - 2)) % m
    else:
        return (a ** (euler(m) - 1)) % m


def task3():
    with open("lab09/szamokP.txt", "rt") as fin:
        for row in fin.readlines():
            data = row.split(" ")
            a, m = int(data[0]), int(data[1])
            inv = inverseEuler(a, m)
            print(a, m, ":", inv)

# endregion


if __name__ == "__main__":
    task1()