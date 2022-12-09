import random
import math
import time
import base64


# region 0. task

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
    
def sieveOfEratosthenes(n):
    primes = set([i for i in range(3, n + 1, 2)])
    primes.add(2)
    k = 3
    while k * k <= n + 1:
        if k in primes:
            for i in range(k * k, n + 1, k):
                primes.discard(i)
        k += 2
    return primes

# endregion

# region 1. task

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
    while (r % 2 == 0):
        s, r = s + 1, r // 2
    for x in [3, 5, 7]:
        if millerRabinForX(m, s, r, x) == False:
            return False

    for _ in range(t - 3):
        x = random.randint(2, m - 1)
        if millerRabinForX(m, s, r, x) == False:
            return False
    return True

def generateRandomPrimeNumber(digits):
    num = random.randint(10 ** (digits-1), 10 ** digits)
    while (not millerRabin(num)):
        num = random.randint(10 ** (digits-1), 10 ** digits)
    return num

def task1():
    for _ in range(10):
        start = time.time()
        num = generateRandomPrimeNumber(100)
        end = time.time()
        print(num, end-start)

# endregion

# region 2. task

def task2():
    with open("lab08/in1.txt", "rt") as fin:
        for row in fin.readlines():
            num = int(row)
            print(num, millerRabin(num))    

# endregion

# region 3. task

def task3():
    k = 1000
    with open("lab08/safe_primes.txt", "wt") as fout:
        print(5, end=" ", file=fout)
        for x in range(3, k + 1, 2):
            p = 2 * x + 1
            if isPrimeNumber(x) and isPrimeNumber(p):
                if p <= k:
                    print(p, end=" ", file=fout)
                else:
                    break

# endregion

# region 4. task

def getGeneratorNumbers(p):
    q = (p - 1) // 2
    if (not isPrimeNumber(p)) or (not isPrimeNumber(q)):
        return None

    lst = []
    for g in range(2, p):
        if pow(g, q, p) != 1:
            lst += [g]

    return lst

def task4():
    p = 47
    print(getGeneratorNumbers(p))

# endregion 

# region 5. task

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

def decToBase256List(num):
    lst = []
    while num: 
        lst = [num % 256] + lst
        num //= 256
    return lst

def base256ToDecList(num256 : list):
    k = 1
    num = 0
    for x in num256[::-1]:
        num += k * x
        k *= 256
    return num

def decToBase256Str(num):
    lst = ""
    while num: 
        x = str(num % 256)
        lst = "0" * (3 - len(x)) + x + lst
        num //= 256
    return lst

def base256ToDecStr(num256 : str):
    l = len(num256)
    num = 0
    k = 1
    while num256:
        x = int(num256[l-3:l])
        num += x * k
        k *= 256
        num256 = num256[0:-3]
        l -= 3
    return num

def encodeToBase64(num256 : str):
    return base64.b64encode(num256.encode()).decode()

def decodeFromBase64(encodedNum : str):
    return base64.b64decode(encodedNum.encode()).decode()

def task5():
    size = 10
    numOfBits = 256
    generatorNumbers = []
    for _ in range(size):
        p = generateRandomPrimeNumberByBits(numOfBits)
        g = getGeneratorNumber(p)
        generatorNumbers += [g]

    with open("lab08/generator_number.txt", "wt") as fout:
        for g in generatorNumbers:
            g256 = decToBase256Str(g)
            gEncoded = encodeToBase64(g256)
            print(gEncoded, file=fout)

def task5_2():
    with open("lab08/generator_number.txt", "rt") as fin:
        for row in fin.readlines():
            gEncoded = row[:-1:]
            g256 = decodeFromBase64(gEncoded)
            g = base256ToDecStr(g256)
            print(g)


# endregion

if __name__ == "__main__":
    task5_2()