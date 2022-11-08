
import math

# region 1. task

def readfile(filename):
    cars = dict()
    for row in open(filename, "rt"):
        data = row.split(" ")
        name = data[0]
        price = int(data[1])
        cars[name] = price
    return cars

def task1():
    filename = "temp/autok.txt"
    cars = readfile(filename)
    print(cars)
    for name, price in cars.items():
        cars[name] = round(price * 1.15)

    print(cars)

# endregion

# region 2. task

def numberOfBitsAPowXSlow(a, x):
    n = a ** x
    nBin = bin(n)[2:]
    return len(nBin)

def numberOfBitsAPowX(a, x):
    return math.floor(math.log2(a) * x) + 1

def task2():
    a = 101
    x = 1789
    print(numberOfBitsAPowXSlow(a, x))
    print(numberOfBitsAPowX(a, x))

# endregion

# region 3. task

def generateNumberSeries(n):
    lst = []
    k = 1
    while n:
        lst += [3 ** (k - 1)]
        n -= 1
        if n >= k:
            lst += [0] * k
            n -= k
        else: 
            lst += [0] * n
            n = 0
        k += 1
    return lst

def task3():
    print(generateNumberSeries(100))

# endregion

if __name__ == "__main__":
    task3()