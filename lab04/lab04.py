import math
import decimal
import pygame
from pygame.locals import *

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

# region 3. feladat

def rootN(num, n=2, p=10):
    decimal.getcontext().prec = p + 1
    difference = decimal.Decimal(0.1) ** (p + 1)
    x = decimal.Decimal(1)
    xNext = decimal.Decimal((2 * x + num / (x ** 2)) / 3)
    while x != xNext or abs(xNext - x) > difference:
        x = xNext
        xNext = ((n - 1) * x + num / (x ** (n - 1))) / n
    return xNext

# endregion 

# region 4. feladat 

def quadraticEquationComplexSolution(a, b, c):
    delta = b ** 2 -4 * a * c
    if delta == 0:
        return -b / (2 * a)
    elif delta < 0:
        delta = complex(delta)
    x1 = (-b + delta ** 0.5) / (2 * a) 
    x2 = (-b - delta ** 0.5) / (2 * a) 
    return (x1, x2)

# endregion

# region 5. feladat 

def complexAdd(z1, z2):
    z = (z1[0] + z2[0], z1[1] + z2[1])
    return z

def complexSub(z1, z2):
    z = (z1[0] - z2[0], z1[1] - z2[1])
    return z

def complexMul(z1, z2):
    z = (z1[0] * z2[0] - z1[1] * z2[1], z1[0] * z2[1] + z1[1] * z2[0])
    return z

def complexDiv(z1, z2):
    absZ2 = complexAbs(z2)
    invZ2 = (z2[0] / (z2[0] ** 2 + z2[1] ** 2), -z2[1] / (z2[0] ** 2 + z2[1] ** 2))
    return complexMul(z1, invZ2)

def complexAbs(z):
    return (z[0] ** 2 + z[1] ** 2) ** 0.5

def complexPow(z, n):
    res = (1, 0)
    for i in range(n):
        res = complexMul(res, z)
    return res

# endregion

# region 6. feladat

def mandelbrot():
    width, height = 800, 800
    screen = pygame.display.set_mode((width,height), DOUBLEBUF)
    xaxis = width / 1.5
    yaxis = height / 2
    scale = 250
    iterations = 60
    for iy in range(height):
        for ix in range(width):
            c = complex((ix - xaxis)/scale, (iy - yaxis) / scale)
            z = c
            for i in range(iterations):
                z = z ** 2 + c
                if abs(z) > 2:
                    color = (255, 255, 255)
                    break 
            if abs(z) <= 2:
                color = (0, 0, 0)
            screen.set_at((ix, iy), color)
            screen.set_at((ix, height - iy), color) 

    pygame.display.update()
    while True:
        event = pygame.event.poll()
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            break 
    pygame.quit()

def julia(c : complex):
    width, height = 800, 800
    screen = pygame.display.set_mode((width,height), DOUBLEBUF)
    xaxis = width / 2
    yaxis = height / 2
    scale = (width * height) ** 0.5 / 3
    iterations = 50
    for iy in range(height):
        for ix in range(width):
            z = complex((ix - xaxis)/scale, (iy - yaxis)/scale)
            for i in range(iterations):
                z = z ** 2 + c
                if abs(z) > 2:
                    color = (i % 16, i % 16 * 8, i % 16 * 16)
                    break 
            if abs(z) <= 2:
                v = 765 * i / iterations
                if v > 510:
                    color = (0, 0, 0)
                else:
                    (i%16, i%16*8, i%16*16)
            screen.set_at((ix, iy), color)
            screen.set_at((ix, height - iy), color) 

    pygame.display.update()
    while True:
        event = pygame.event.poll()
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            break 
    pygame.quit()

# endregion

if __name__ == '__main__':
    
    p = 10
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
    p = 30
    print("phi cf:", cfPhi(p=p))
    print("pi cf:", cfDecimalNumber(myPi(), p=p))
    n = 12 # https://mathworld.wolfram.com/PeriodicContinuedFraction.html
    print("sqrt", n, "cf", cfDecimalNumber(mySqrt(n), p=p)) 

    # nth root
    print(rootN(127, n=5, p=20))

    # Quadratic equation complex solution
    print(quadraticEquationComplexSolution(1, 4, 5))
    print(quadraticEquationComplexSolution(1, 4, 4))
    print(quadraticEquationComplexSolution(1, 0, -4))

    # complex numbers
    z1 = (2.5, 4.3)
    z2 = (1.7, 10.25)
    print("z1 =", z1, ", z2 =", z2)
    print("z1 + z2 =", complexAdd(z1, z2))
    print("z1 - z2 =", complexSub(z1, z2))
    print("z1 * z2 =", complexMul(z1, z2))
    print("z1 / z2 =", complexDiv(z1, z2))
    print("abs(z1) =", complexAbs(z1))
    nPow = 3
    print("z1 ^", nPow, "=", complexPow(z1, nPow))

    # fractals
    yn = input("Do you want to see the fractals?(y/n)")
    if yn == "y" or yn == "Y":
        mandelbrot()
        c0 = complex (0, -0.8)
        c1 = complex (0.285, 0.013)
        c2 = complex (-0.295, -0.55)
        c3 = complex (-0.63, -0.407)
        c4 = complex (-0.624, 0.435)
        c5 = complex (-1, -0.25)
        c6 = complex (-1, -0)
        #julia(c0)
        complexList = [c1, c2, c3, c4, c5, c6]
        for c in complexList:
            julia(c)



