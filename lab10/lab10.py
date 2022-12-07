import math
import random

# region 1. task

def inverse(a, m):
    x0, x1 = 1, 0
    b = m
    while True:
        q = a // b
        r = a - b * q
        if r == 0:
            if b != 1: return -1
            else: return x1 % m
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
    
    #print(mkL, invMkL)
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

def generateRandomPrimeNumber(digits, t=10):
    num = random.randint(10 ** (digits-1), 10 ** digits)
    while (not millerRabin(num, t)):
        num = random.randint(10 ** (digits-1), 10 ** digits)
    return num

def RSAkeyGen(k):
    p = generateRandomPrimeNumber(k, 10)
    q = generateRandomPrimeNumber(k, 10)
    n = p * q
    phi = (p-1) * (q-1)
    e = 3
    while True:
        if math.gcd(e, phi) == 1: 
            break
        e += 2
    d = inverse(e, phi)
    return (e, d, n, p, q)

def RSAcrypt(num, e, n):
    return pow(num, e, n)

def RSAdecrypt(cK, d, n):
    return pow(cK, d, n)

def RSAdecrypt2(cK, d, p, q, n):
    dp = d % (p - 1)
    dq = d % (q - 1)
    mqInverse = inverse(q % p, p)
    mpInverse = inverse(p % q, q)
    cp = pow(cK, dp, p)
    cq = pow(cK, dq, q)
    x = (cp * mqInverse * q + cq * mpInverse * p) % n
    return x

def RSAdecrypt3(cK, d, p, q, n):
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
    num = int(input())
    cK = RSAcrypt(num, e, n)
    print ('titkositott ertek: ', cK)
    num = RSAdecrypt3(cK, d, p, q, n)
    print ('visszafejtett ertek:', num)

# endregion

# region 4. task

def task4():
    k = 4
    p = generateRandomPrimeNumber(k)
    print(p)
    foutKvad = open("lab10/kvadratikus.txt", "wt")
    foutNotKvad = open("lab10/notkvadratikus.txt", "wt")
    for a in range(2, p):
        tmp = pow(a, (p - 1) // 2, p)
        if tmp == 1:
            print(a, file=foutKvad)
        else:
            print(a, file=foutNotKvad)
    
    foutKvad.close()
    foutNotKvad.close()

# endregion

if __name__ == "__main__":
    task4()