import random
import math
import time

# region 1. task

def middleSquare(r, n):
    k = len(str(r))
    for _ in range(n):
        rStr = str(r * r)
        x = (len(rStr) - k) // 2
        r = int(rStr[x:x+k])
    return r

def middleSquarePeriod(r):
    k = len(str(r))
    lst = []
    while len(lst) == len(set(lst)):
        rStr = str(r * r)
        x = (len(rStr) - k) // 2
        r = int(rStr[x:x+k])
        lst += [r]
    return lst


def task1():
    with open("lab12/midlSqr.txt", "rt") as fin:
        maxmid = ()
        for row in fin:
            seed = int(row)
            lst = middleSquarePeriod(seed)
            print(seed, lst)
            if maxmid == () or len(lst) > len(maxmid[1]):
                maxmid = (seed, lst)
        print(maxmid)
            

# endregion

# region 2. task

def pLinGen(z0, m=10, a=1, b=7):
    if z0 != None:
        z1 = z0
    else: 
        z1 = int(time.time())
    z1 = (z1 * a + b ) % m
    return z1

def randAnsiC(seed=None):
    return pLinGen(seed, m=(1 << 31), a=1103515245, b=12345)

def randCPP(seed=None):
    return pLinGen(seed, m=(1 << 31), a=214013, b=2531011)

def randJava(seed=None):
    return pLinGen(seed, m=(1 << 48), a=25214903917, b=11)

def task2():
    print("Standard:")
    seed = None
    for i in range(100):
        seed = pLinGen(seed)
        print(seed, end = ' ')

    print("\nANSI C:")
    seed = None
    for i in range(100):
        seed = pLinGen(seed, m=(1 << 31), a=1103515245, b=12345)
        print(seed, end = ' ')

    print("\nC/C++:")
    seed = None
    for i in range(100):
        seed = pLinGen(seed, m=(1 << 31), a=214013, b=2531011)
        print(seed, end = ' ')

    print("\nJava:")
    seed = None
    for i in range(100):
        seed = pLinGen(seed, m=(1 << 48), a=25214903917, b=11)
        print(seed, end = ' ')

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

    for _ in range(t - 3):
        x = random.randint(2, m - 1)
        if millerRabinForX(m, s, r, x) == False:
            return False
    return True

def mersenne(n):
    return (1 << n) - 1

def task3():
    k = 100
    for i in range(1, k + 1):
        num = mersenne(i)
        if num != 1 and millerRabin(num) :
            print(num, "primszam")
        else:
            print(num)

# endregion

# region 4. task

def safePrime(k):
    q = random.getrandbits(k)
    if not (q & 1): 
        q += 1
    while True:
        p = 2 * q + 1
        if millerRabin(q, t=10) and millerRabin(p, t=10):
            return p
        q = random.getrandbits(k)
        if not (q & 1): 
            q += 1

def bbs(k, l):
    p = safePrime(k//2)
    q = safePrime(k//2)
    n = p * q
    r = random.randint(2, n)
    u = (r * r) % n
    lst = []
    for _ in range(0, l):
        u = (u * u) % n
        lst += [u % 2]

def task4():
    print(bbs(64, 16))


# endregion

if __name__ == "__main__":
    task4()