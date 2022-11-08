import math


# region 1. task

def readfile(filename):
    lst = []
    for row in open(filename, "rt"):
        data = row.split()
        name = data[0]
        payment = int(data[1])
        lst += [(name, payment)]
    return lst

def getAvgPayment(lst):
    s = 0
    for name, payment in lst:
        s += payment
    return s / len(lst)

def printNameLowerThanAverage(lst, avg):
    for name, payment in lst:
        if payment <= avg:
            print(name, end=" ")

def task1():
    lst = readfile("temp/szemelyek.txt")
    avg = getAvgPayment(lst)
    printNameLowerThanAverage(lst, avg)

# endregion

# region 2. task

def numberOfComplexBelow1(lst):
    s = 0
    for c in lst:
        # print(c, abs(c))
        if abs(c) <= 1:
            s += 1
    return s

def task2():
    lst = [
        complex(1, 2),
        complex(0.5, 0.1),
        complex(0, 1),
        complex(10, 2)
    ]
    print(numberOfComplexBelow1(lst))

# endregion

# region 3. task

def numberOfDigitsInHexFactorialSlow(n):
    fact = math.factorial(n)
    hexFact = hex(fact)[2:]
    return len(hexFact)

def numberOfDigitsInHexFactorial(n):
    digits = 1
    for i in range(1, n + 1):
        digits += math.log(i, 16)
    return math.floor(digits)

def task3():
    n = 100
    print(numberOfDigitsInHexFactorialSlow(n))
    print(numberOfDigitsInHexFactorial(n))

# endregion

if __name__ == "__main__":
    task3()
