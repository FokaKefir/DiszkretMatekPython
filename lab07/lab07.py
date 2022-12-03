import random
import math
import time
import datetime

# region 1. task

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

def generateRandomPrimeNumber(digits):
    num = random.randint(10 ** (digits-1), 10 ** digits)
    while (not isPrimeNumber(num)):
        num = random.randint(10 ** (digits-1), 10 ** digits)
    return num

def generateRandomPrimeNumberEratosthenes(digits):
    primes = sieveOfEratosthenes(10 ** digits)
    num = random.randint(10 ** (digits-1), 10 ** digits)
    while (num not in primes):
        num = random.randint(10 ** (digits-1), 10 ** digits)
    return num
    

def task1():
    digits = 8
    print(generateRandomPrimeNumber(digits))
    print(generateRandomPrimeNumberEratosthenes(digits))

# endregion

# region 2. task

def task2():
    n = 100
    primes = sorted(sieveOfEratosthenes(int(n * (math.log(n) + math.log(math.log(n) - 1)))))
    print(primes[n - 1])
    
# endregion

# region 3. task

def task3():
    primes = sieveOfEratosthenes(10 ** 7)
    with open("lab07/primes.txt", "wt") as fout:
        print(*sorted(primes), file=fout)

# endregion

# region 4. task

def task4():
    num = 100
    beforePrime = num - 1
    while (not isPrimeNumber(beforePrime)):
        beforePrime -= 1
    
    afterPrime = num + 1
    while (not isPrimeNumber(afterPrime)):
        afterPrime += 1
    
    print(beforePrime, afterPrime)

# endregion

# region 5. task

def task5():
    num = 6
    if isPrimeNumber(num):
        print(num, " is prime")
    else:
        primes = sorted(sieveOfEratosthenes(num))
        for x in primes:
            if num % x == 0:
                print(x)
                break
        x = num
        while (not isPrimeNumber(x)):
            x -= 1
        
        index = primes.index(x)
        while (num % primes[index] != 0):
            index -= 1
        print(primes[index])

# endregion

# region 6. task 

def task6():
    num1, num2 = 5, 7
    if num2 - num1 == 2 and isPrimeNumber(num1) and isPrimeNumber(num2):
        print(num1, "es", num2, "ikerprimek")
    else:
        print(num1, "es", num2, "nem ikerprimek")

# endregion

# region 7. task

def task7():
    x = 125416
    primes = sieveOfEratosthenes(x)
    for prime in primes:
        if (x - prime) in primes:
            print(x, "=", prime, "+", x - prime)
            return

# endregion

# region 8. task

def numberOfPrimes1(n):
    s = 0
    for x in range(2, n + 1):
        if isPrimeNumber(x):
            s += 1
    return s

def numberOfPrimes2(n):
    primes = sieveOfEratosthenes(n)
    return len(primes)

def task8():
    for i in range(2, 8):
        print(10 ** i, ":")

        start = time.time()
        nop1 = numberOfPrimes1(10 ** i)
        end = time.time()
        print("\t1.", nop1, end - start)

        start = time.time()
        nop2 = numberOfPrimes2(10 ** i)
        end = time.time()
        print("\t2.", nop2, end - start)

# endregion

# region 9. task

def numberOfPrimesLimit1(mini, maxi):
    s = 0
    for x in range(mini, maxi + 1):
        if isPrimeNumber(x):
            s += 1
    return s

def numberOfPrimesLimit2(mini, maxi):
    primes = sieveOfEratosthenes(maxi)
    s = 0
    for x in range(mini, maxi + 1):
        if x in primes:
            s += 1
    return s

def task9():
    k = 20
    maxi = (1 << k) - 1
    mini = 1 << (k - 1)
    print(numberOfPrimesLimit1(mini, maxi))
    print(numberOfPrimesLimit2(mini, maxi))


# endregion 

# region 10. task

def isPrimeWilson(n):
    f = 1
    for i in range(2, n):
        f = (f * i) % n
    if f == n - 1:
        return True
    return False

def task10():
    n = 1153
    print(n, isPrimeWilson(n))

# endregion

# region 11. task

def task11():
    s = 0
    n = 10000
    a = 4
    for x in range(4, n + 1):
        if (a ** (x - 1)) % x == 1 and (not isPrimeNumber(x)):
            s += 1
    print(s)

# endregion

# region 12. task 

def isCarmichaelNumber(num):
    for x in range(1, num):
        if math.gcd(x, num) == 1 and (x ** (num - 1)) % num != 1:
            return False
    return True

def task12():
    isCarmichaelNumber(561)
    for num in range(4, 1000001):
        if not isPrimeNumber(num) and isCarmichaelNumber(num):
            print(num)

# endregion

# region 13. task

def task13():
    d = datetime.date(2004, 3, 16)
    print(d.strftime("%a"))
    print(d.strftime("%j"))

# endregion

if __name__ == "__main__":
    task13()