import math
# region 1. feladat

def sumList(lst):
    return sum(lst)

def minNumberAndPosition(lst):
    mini, ind = lst[0], 0
    for i, x in enumerate(lst):
        if x < mini:
            mini, ind = x, i
    
    return (mini, ind)

def maxNumberAndPosition(lst):
    maxi, ind = lst[0], 0
    for i, x in enumerate(lst):
        if x > maxi:
            maxi, ind = x, i
    
    return (maxi, ind)

def numberOfEvenNumbers(lst):
    s = 0
    for x in lst:
        if x % 2 == 0:
            s += 1
    return s

def evenNumbersAndPositions(lst):
    evenNumbers = []
    for i, x in enumerate(lst):
        if x % 2 == 0:
            evenNumbers += [(x, i)]
    return evenNumbers

def averageNumbers(lst):
    return sum(lst) / len(lst)

def isSquare(num):
    return int(num ** 0.5) ** 2 == num

def numberOfSquares(lst):
    s = 0
    for x in lst:
        if isSquare(x):
            s += 1
    return s

def squaresAndPositions(lst):
    squares = []
    for i, x in enumerate(lst):
        if isSquare(x):
            squares += [(x, i)]
    return squares

# endregion

# region 2. feladat

def getListIndexesLowerThanX(lst, x = 0):
    indexes = []
    for i, x in enumerate(lst):
        if x < 0:
            indexes += [i]
    return indexes

def fileRead(filename = 'lab02/homerseklet.txt'):
    fin = open(filename, 'rt')
    tmp = fin.readline()
    months = tmp.split()
    monthIndexes = []  
    while True:
        tmp = fin.readline()
        if not tmp:
            break
        print(tmp.strip(), end='   ')
        tmp = fin.readline()
        maxTemperatures = [int(x) for x in tmp.split()[5:]]
        tmp = fin.readline()
        minTemperatures = [int(x) for x in tmp.split()[5:]]
        fin.readline()
        print(minNumberAndPosition(maxTemperatures)[0], end=' ')
        for ind in getListIndexesLowerThanX(minTemperatures):
            print(months[ind], end=' ')
            if ind not in monthIndexes:
                monthIndexes += [ind]
        print()

    for ind in monthIndexes:
            print(months[ind], end=' ')

    fin.close()

# endregion

# region 3. feladat

def squareNumbers():
    s = 0
    while True:
        line = input()
        if not line:
            break
        x, n = tuple(line.split())
        x, n = int(x), int(n)
        print(x ** n)
        s += n
    return s

# endregion

# region 4. feladat

def numberOfBits(n):
    return math.floor(math.log2(n)) + 1

def numberOfDigitsInFactorialSlow(n):
    return len(str(math.factorial(n)))

def numberOfDigitsInFactorial(n):
    if n < 0:
        return 0
    if n < 1:
        return 1

    return math.floor((n * math.log10(n / math.e) + math.log10(2 * math.pi * n) / 2)) + 1

def numberOfBitsInFactorialSlow(n):
    fact = math.factorial(n)
    return numberOfBits(fact)

def numberOfBitsInFactorial(n):
    numBits = 1
    for i in range(1, n + 1):
        numBits += math.log2(i)
    return math.floor(numBits)

# endregion

# region 5. feladat

# endregion

if __name__ == '__main__':
    n = 100000
    #print("Number of digits in factorial")
    #print("Faster: ", numberOfDigitsInFactorial(n))
    #print("Slower: ", numberOfDigitsInFactorialSlow(n))
    print("Number of bits in factorial")
    print("Faster: ", numberOfBitsInFactorial(n))
    print("Slower: ", numberOfBitsInFactorialSlow(n))


