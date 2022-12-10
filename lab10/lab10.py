import math
import random
import base64

# region 1. task

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

def chineseRemainder(aL, mL):
    mMul = 1
    for m in mL:
        mMul *= m

    mkL = []
    invMkL = []
    for m in mL:
        tmp = mMul // m
        mkL += [tmp]
        invTmp = inverse(tmp, m)
        invMkL += [invTmp]
    
    x = 0
    for i in range(len(mL)):
        x = (x + aL[i] * mkL[i] * invMkL[i]) % mMul
    return x

def task1():
    aL = [4, 11, 0]
    mL = [5, 12, 7]
    print(chineseRemainder(aL, mL))

# endregion

# region 2. task

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

def chineseRemainderNotRelPrimes(aL, mL):
    a0 = aL[0]
    m0 = mL[0]
    for i in range(1, len(aL)):
        g, k1, k2 = extEuclid(m0, mL[i])
        if abs(a0 - aL[i]) % g != 0:
            return -1
        else:
            lcmV = math.lcm(m0, mL[i])
            a0 = ((a0 * mL[i] * k2) // g + (aL[i] * m0 * k1) // g) % lcmV
            m0 = lcmV
    return a0

def task2():
    aL=[8, 18, 13, 10]
    mL=[9, 35, 20, 17]
    print(chineseRemainderNotRelPrimes(aL, mL))

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


def generateRandomPrimeNumberByBits(bits, t=10):
    num = random.getrandbits(bits)
    while (not millerRabin(num, t)):
        num = random.getrandbits(bits)
    return num

def generateRandomPrimeNumber(digits, t=10):
    num = random.randint(10 ** (digits-1), 10 ** digits)
    while (not millerRabin(num, t)):
        num = random.randint(10 ** (digits-1), 10 ** digits)
    return num

def RSAkeyGen(k):
    p = generateRandomPrimeNumberByBits(k, 10)
    q = generateRandomPrimeNumberByBits(k, 10)
    n = p * q
    phi = (p-1) * (q-1)
    e = 3
    while True:
        if math.gcd(e, phi) == 1: 
            break
        e += 2
    d = inverse(e, phi)
    return (e, d, n, p, q)

def RSAcrypt(k, e, n):
    return pow(k, e, n)

def RSAdecrypt(cK, d, n):
    return pow(cK, d, n)

# chinese remainder shorter
def RSAdecryptCR(cK, d, p, q, n):
    dp = d % (p - 1)
    dq = d % (q - 1)
    mqInverse = inverse(q % p, p)
    mpInverse = inverse(p % q, q)
    cp = pow(cK, dp, p)
    cq = pow(cK, dq, q)
    x = (cp * mqInverse * q + cq * mpInverse * p) % n
    return x

# chinese remainder longer
def RSAdecryptCR2(cK, d, p, q, n):
    dp = d % (p - 1)
    dq = d % (q - 1)
    cp = pow(cK, dp, p)
    cq = pow(cK, dq, q)
    x = chineseRemainder([cp, cq], [p, q])
    return x

def task3():
    nBits = int(input('bit meret: '))
    e, d, n, p, q = RSAkeyGen(nBits)
    print ('nyilvanos kulcs: ', e, n)
    print ('titkos kulcs: ', d, n)
    print('kerek egy szamot, legyen kisebb mint: ', n)
    k = int(input())
    cK = RSAcrypt(k, e, n)
    print ('titkositott ertek: ', cK)
    k = RSAdecryptCR2(cK, d, p, q, n)
    print ('visszafejtett ertek:', k)

# endregion

# region 4. task

def task4():
    k = 4
    p = generateRandomPrimeNumber(k)
    print(p)
    foutKvad = open("lab10/kvadratikus.txt", "wt")
    foutNotKvad = open("lab10/notkvadratikus.txt", "wt")
    for a in range(1, p):
        tmp = pow(a, (p - 1) // 2, p)
        if tmp == 1:
            print(a, file=foutKvad)
        else:
            print(a, file=foutNotKvad)
    
    foutKvad.close()
    foutNotKvad.close()

# endregion

# region 5. task

# Kvadratikus maradek
def quadraticResidue(prime):
    lst = []
    for a in range(1, prime):
        if pow(a, (prime - 1) // 2, prime) == 1:
            lst += [a]
    return lst

def task5():
    p = 11
    qrList = quadraticResidue(p)
    print(p, "kvadratikus maradekai:", qrList)
    for a in qrList:
        x1 = pow(a, (p + 1) // 4, p)
        x2 = p - x1
        print("Kvadratikus maradek:", a, "negyzetgyokei:", x1, x2)

# endregion

# region 6. task

def jacobi(a, n):
    if a == 0:
        return 0
    if a == 1:
        return 1
    e, r = 0, a
    while r & 1 == 0:
        e, r = e + 1, r >> 1
    if e & 1 == 0:
        s = 1
    else:
        temp = n % 8
        if temp == 1 or temp == 7:
            s = 1
        elif temp == 3 or temp == 5:
            s = -1
    if n % 4 == 3 and r % 4 == 3:
        s = -s
    n = n % r
    if r == 1:
        return s
    else:
        return s * jacobi(n, r)

def task6():
    p = 47 
    q = 59
    n = p * q

    foutJacobi = open("lab10/jacobi.txt", "wt")
    foutNotJacobi = open("lab10/notjacobi.txt", "wt")

    sj, snj = 0, 0
    for a in range(1, n):
        if jacobi(a, n) == 1:
            print(a, file=foutJacobi)
            sj += 1
        else:
            print(a, file=foutNotJacobi)
            snj += 1
    
    foutJacobi.close()
    foutNotJacobi.close()

    print("number of jacobi", sj)
    print("number of not jacobi", snj)

# endregion

# region 7. task

def task7():
    p = 47 
    q = 59
    n = p * q
    s = 0
    for a in range(1, n):
        if jacobi(a, n) == 1:
            pInv = inverse(p, q)
            qInv = inverse(q, p)
            xp = pow(a, (p + 1) // 4, p)
            xq = pow(a, (q + 1) // 4, q)
            x1 = (pInv * p * xq + qInv * q * xp) % n
            x2 = (pInv * p * xq - qInv * q * xp) % n
            x3 = n - x1
            x4 = n - x2

            print("Kvadratikus maradek:", a, "negyzetgyokei", x1, x3, x2, x4)
            s += 1
    print(s, "db kvadratikus maradek")

# endregion

# region 8. task

def task8():
    with open("lab10/rabinKey.txt", "rt") as fin:
        for row in fin:
            data = row.split(" ")
            cK, p, q = data[0::3]
            cK, p, q = int(cK), int(p), int(q)
            n = p * q
            phi = (p-1) * (q-1)
            e = 3
            while True:
                if math.gcd(e, phi) == 1: 
                    break
                e += 2
            d = inverse(e, phi)
            k = RSAdecrypt(cK, d, n)
            print(k)
            # TODO decode to string

# endregion

# region 9. task

def encodeBase64(myStr : str):
    return base64.b64encode(myStr.encode()).decode()

def decodeBase64(myStr : str):
    return base64.b64decode(myStr.encode()).decode()

def rabinKeyGen(bits=256):
    while True:
        p = random.getrandbits(bits)
        if p % 8 == 3 and millerRabin(p):
            break
    while True:
        q = random.getrandbits(bits)
        if q % 8 == 7 and millerRabin(q):
            break
    n = p * q
    d = (n - p - q + 5) // 8
    return n, d, p, q

def rabinSign(k, d, n):
    kK = 16 * k + 6
    if jacobi(kK, n):
        return pow(kK, d, n)
    else:
        return pow(kK // 2, d, n)

def rabinVerify(sign, n):
    kK1 = (sign * sign) % n
    temp = kK1 % 8
    if temp == 6:
        kK = kK1
    elif temp == 3:
        kK = 2 * kK1
    elif temp == 7:
        kK = n - kK1
    elif temp == 2:
        kK = 2 * (n - kK1)
    return (kK - 6) // 16

def task9_1():
    foutPrivateKey = open("lab10/rabin_private_key", "wt")
    foutPublicKey = open("lab10/rabin_public_key", "wt")
    n, d, p, q = rabinKeyGen(bits=256)
    #print(n, d)
    privateKey64 = encodeBase64(str(d))
    publicKey64 = encodeBase64(str(n))
    print(privateKey64, file=foutPrivateKey)
    print(publicKey64, file=foutPublicKey)
    foutPrivateKey.close()
    foutPublicKey.close()
    

def task9_2():
    with open("lab10/rabin_private_key", "rt") as finPrivateKey:
        privateKey64 = finPrivateKey.read()
    with open("lab10/rabin_public_key", "rt") as finPublicKey:
        publicKey64 = finPublicKey.read()
    d = int(decodeBase64(privateKey64))
    n = int(decodeBase64(publicKey64))
    k = int(input("adjon meg egy tetszoleges erteket: "))
    sign = rabinSign(k, d, n)
    #print(sign)
    return sign

def task9_3(sign):
    with open("lab10/rabin_public_key", "rt") as finPublicKey:
        publicKey64 = finPublicKey.read()
    n = int(decodeBase64(publicKey64))
    k = rabinVerify(sign, n)
    print(k)

def task9():
    task9_1()
    sign = task9_2()
    task9_3(sign)

# endregion

# region 10. task

def task10():
    x, y = 49841, 98456
    mList = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    xyList = []
    for m in mList:
        xyList += [(x % m) + (y % m)]
    z = chineseRemainder(xyList, mList)
    print(z, x + y)

# endregion

# region 12. task

# a*x+b*y=c
def diofant (a, b, c):
    (d, xk, yk) = extEuclid(a, b)
    if c % d != 0:
        return -1
    x0 = xk * c // d
    y0 = yk * c // d
    bd = b // d
    ad = a // d
    n1 = int (math.ceil(-x0 / bd))
    n2 = int (math.floor(y0 / ad))
    if n1 <= n2:
        lst = []
        for i in range(n1, n2 + 1):
            lst += [(x0 + bd * i, y0 - ad * i)]
        return lst
    else: 
        return -1

def task12():
    with open("lab10/diofant.txt", "rt") as fin:
        for row in fin.readlines():
            a, b, c = row.split(" ")
            a, b, c = int(a), int(b), int(c)
            print(f'{a}*x + {b}*y = {c} : ')
            print("\t", diofant(a, b, c))

# endregion

if __name__ == "__main__":
    task12()