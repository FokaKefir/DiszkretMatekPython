import math
import decimal
# region 1. feladat

def continuedFractionSqrt(n, k=500):
    if int(n ** 0.5) ** 2 == n:
        return "Doesn't work for square numbers"
    temp = 0
    for i in range(k):
        pass
    
def mySqrt(n, p=500):
    if int(n ** 0.5) ** 2 == n:
        return n ** 0.5

    decimal.getcontext().prec = p
    root = decimal.Decimal(0)
    for i in range(2 * p):
        root = (n - 1) / (2 + root)

    return 1 + root

def myPhi(k=500):
    phi = 0
    for i in range(k):
        phi = 1 / (1 + phi)
    return 1 + phi


# endregion

if __name__ == '__main__':
    print(myPhi())
    print(mySqrt(5))

