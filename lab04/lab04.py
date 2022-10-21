import math
import decimal

# region 1. feladat
    
def mySqrt(n, p=500):
    if int(n ** 0.5) ** 2 == n:
        return n ** 0.5

    decimal.getcontext().prec = p
    root = decimal.Decimal(0)
    for i in range(2 * p):
        root = (n - 1) / (2 + root)

    return 1 + root

def myPhi(p=500):
    decimal.getcontext().prec = p
    phi = decimal.Decimal(0)
    for i in range(2 * p):
        phi = 1 / (1 + phi)
    return 1 + phi

def myPi(p=500):
    decimal.getcontext().prec = p
    pi = decimal.Decimal(0)
    for i in range(2 * p, 0, -1):
        pi = (i ** 2) / ((2 * i + 1) + pi)
    return 4 / (1 + pi)

def myPiRec(p=500, n=0):
    decimal.getcontext().prec = p
    if p == n:
        return decimal.Decimal(p ** 2 / (2 * p - 1))
    elif n == 0:
        return 4 / myPiRec(p, n + 1)
    else:
        return (2 * n - 1) + n ** 2 / myPiRec(p, n + 1)

def myEulerNumber(p=500):
    decimal.getcontext().prec = p
    e = decimal.Decimal(0)
    for i in range(0,  2 * p):
        e +=  1 / decimal.Decimal(math.factorial(i))
    return e
    
def myLn(n, p=500):
    n -= 1
    decimal.getcontext().prec = p
    lnN = decimal.Decimal(0)
    for i in range(2 * p, 0, -1):
        lnN = (((i + 1) // 2) ** 2 * n) / (i + 1 + lnN)
    return n / (1 + lnN)

def mySin(x, p=500):
    x = decimal.Decimal(math.radians(x))
    decimal.getcontext().prec = p
    sinX = decimal.Decimal(0)
    for i in range(2 * p, 0, -2):
        sinX = (i * (i + 1) * x ** 2) / ((i + 2) * (i + 3) - x ** 2 + sinX)
    sinX = x ** 2 / (2 * 3 - x ** 2 + sinX)
    return x / (1 + sinX)

def myCos(x, p=500):
    return mySin(90 - x, p)

def myTg(x, p=500):
    return mySin(x, p) / myCos(x, p)

def myCtg(x, p=500):
    return myCos(x, p) / mySin(x, p)

# endregion

# region 2. feldat

def cfDecimalNumber(dNum, p=500):
    lst = []
    for _ in range(p):
        lst += [math.floor(dNum)]
        dNum = 1 / (dNum - math.floor(dNum))
    return lst

def cfPhi(p=500):
    return [1 for _ in range(p)]


# endregion

if __name__ == '__main__':
    
    p=10
    print("phi =", myPhi(p=p))
    print("sqrt =", mySqrt(5, p=p))
    print("pi =", myPi(p=p))
    print("e =", myEulerNumber(p=p))
    print("ln =", myLn(2, p=p))
    print("sin =", mySin(60, p=p))
    print("cos =", myCos(45, p=p))
    print("tg =", myTg(30, p=p))
    print("ctg =", myCtg(30, p=p))

    # continued fraction 
    p = 50
    print("phi cf:", cfPhi(p=p))
    print("pi cf:", cfDecimalNumber(myPi(), p=p))
    n = 12 # https://mathworld.wolfram.com/PeriodicContinuedFraction.html
    print("sqrt", n, "cf", cfDecimalNumber(mySqrt(n), p=p)) 



