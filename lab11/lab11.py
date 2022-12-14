import random
import math
import decimal
import time


# region 1. task 

def task1():
    nums = [60886398661138796801453, 18330506023168856466071, 9025708713908783760873431]
    for num in nums:
        p, q = fermatFact(num)
        print(p, q)

# endregion

# region 2. task

TIME_LIMIT_SEC = 10

def fermatFactTimeLimit(n):
    decimal.getcontext().prec = 400
    a = int(decimal.Decimal(n).sqrt()) + 1
    st = time.time()
    while True:
        fs = time.time()
        if (fs - st) >= TIME_LIMIT_SEC:
            return "TL"
        b1 = a * a - n
        b = squareTest(b1)
        if b != -1:
            return (a - b, a + b)
        a += 1

def pollardRhoTimeLimit(n):
    a = 1
    b = 2
    st = time.time()
    while True:
        fs = time.time()
        if (fs - st) >= TIME_LIMIT_SEC:
            return "TL"
        a = (a * a + 1) % n
        b = (b * b + 1) % n
        b = (b * b + 1) % n
        d = math.gcd(a - b, n)
        if 1 < d <= n:
            return d, n // d

def task2():
    nums = [117909607, 21261237198254169127801, 149063950693785473206387643, 6416626799448849184299219222997152546843712511308822463778262756071903295686583190313754050072639159072918419909621481540760781304636463845632523179, 11379881602713805813074408600393657498808359221180270219583433367270200091282805603668259467898750049483687125365056837556555463733092892411265612455581727940831, 10264762919188799324017198473653676357077973949714005441630872637584674644086006446077930626500755999282238632213530271489005199300521704739285262210696019]
    print("Fermat:")
    for num in nums:
        print(num, end=": ")
        res = fermatFactTimeLimit(num)
        if res == "TL":
            print("Time limit")
        else:
            p, q = res
            print(f"{p} * {q}")

    print("Pollar Rho:")
    for num in nums:
        print(num, end=": ")
        res = pollardRhoTimeLimit(num)
        if res == "TL":
            print("Time limit")
        else:
            p, q = res
            print(f"{p} * {q}")



# endregion

# region 3. task

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

def RSAcrypt(k, e, n):
    return pow(k, e, n)

def RSAdecrypt(cK, d, n):
    return pow(cK, d, n)

def squareTest(x):
    i = int(decimal.Decimal(x).sqrt())
    if i * i == x:
        return i
    else:
        return -1

def fermatFact(n):
    decimal.getcontext().prec = 400
    a = int(decimal.Decimal(n).sqrt()) + 1
    while True:
        b1 = a * a - n
        b = squareTest(b1)
        if b != -1:
            return (a - b, a + b)
        a += 1

def task3():
    e = 7
    n = 58708206817278867892348689140243132246676021225428668975471547135435869525105781465754708178982262745679363405352544297022325492380537955403728333153443
    p, q = fermatFact(n)
    d = inverse(e, (p - 1) * (q - 1))
    cK = 314274283998806883515597161983007833495415014249027602529003306186770034647625674131992754877815148009763600003545920000492800000128
    k = RSAdecrypt(cK, d, n)
    print(k)


# endregion

# region 4. task 

def pollardRho(n):
    a = 1
    b = 2
    while True:
        a = (a * a + 1) % n
        b = (b * b + 1) % n
        b = (b * b + 1) % n
        d = math.gcd(a - b, n)
        if 1 < d <= n:
            return d, n // d

def task4():
    e = 11
    n = 9274360000286227529
    p, q = pollardRho(n)
    d = inverse(e, (p - 1) * (q - 1))
    cK = 5717293945922157626
    k = RSAdecrypt(cK, d, n)
    print(k)

# endregion

# region 5. task 

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

def generateRandomPrimeNumberByBits(bits):
    num = random.getrandbits(bits)
    while (not millerRabin(num) or not millerRabin((num - 1) // 2)): # safe primes
        num = random.getrandbits(bits)
    return num

def getGeneratorNumber(p):
    q = (p - 1) // 2
    if not millerRabin(q):
        return None

    g = random.randint(2, p - 2)
    while pow(g, q, p) == 1:
        g = random.randint(2, p - 2)
    return g

def dLogSlow(g, A, p):
    for i in range(1, p-1):
        if pow(g, i, p) == A:
            return i

def dLog(g, A, p):
    m = int((p - 1) ** 0.5) + 1
    lst, qHatv = [], 1
    for j in range(m):
        lst = [qHatv] + lst
        qHatv = (qHatv * g) % p
    gInv = inverse(g, p)
    gInvM = pow(gInv, m, p)
    qHatv = 1
    for i in range(m):
        c = (A * qHatv) % p
        try:
            j = (m-1) - lst.index(c)
            return i * m + j
        except:
            qHatv = (qHatv * gInvM) % p
            continue
    return -1

def task5():
    p = generateRandomPrimeNumberByBits(20)
    g = getGeneratorNumber(p)
    print(p, g)
    for num in range(p // 2, p):
        st1 = time.time()
        dlogslow = dLogSlow(g, num, p)
        fs1 = time.time()

        st2 = time.time()
        dlog = dLog(g, num, p)
        fs2 = time.time()
        print(f"{num}: Slow: {dlogslow} ({fs1 - st1}) Faster: {dlog} ({fs2 - st2})")
        if dlog != dlogslow:
            print("nem jo")
            break


# endregion

if __name__ == "__main__":
    task5()