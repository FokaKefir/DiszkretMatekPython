
# region 1. feladat

def firstDigit(num):
    while num > 9:
        num //= 10
    return num

def numberOfDigits(num):
    return len(str(num))

def numberOfEvenDigits(num):
    eDigits = 0
    while num != 0:
        if num % 2 == 0:
            eDigits += 1
        num //= 10
    return eDigits    

def firstDigitInB(num, b):
    digit = 0
    while num != 0:
        digit = num % b
        num //= b
    return digit    

def numberOfDigitsEqualKInB(num, b, k):
    kDigits = 0
    while num != 0:
        if num % b == k:
            kDigits += 1
        num //= b
    return kDigits  

# endregion

# region 2. feladat

def convBtoBk(lst, b, k):
    n = 0
    lstBk = []
    nr = 0
    for x in lst[::-1]:
        if n == k:
            lstBk = [nr] + lstBk
            n = 0
            nr = 0
        nr += b ** n * x
        n += 1
    lstBk = [nr] + lstBk
    return lstBk

def convBkToB(lstBk, b, k):
    lst = []
    for x in lstBk[::-1]:
        n = 0
        while x != 0:
            lst = [x % b] + lst
            x = x // b
            n += 1
        while n != k:
            lst = [0] + lst
            n += 1
    return lst

def largerDigitInBinK(binNum, k):
    n = 0
    maxNum = 0
    num = 0
    for x in binNum[::-1]:
        if n == k:
            maxNum = max(maxNum, num)
            num = 0
            n = 0
        num += 2 ** n * x
        n += 1
    maxNum = max(maxNum, num)
    return maxNum, bin(maxNum)[2:]

# endregion

# region 4. feladat

def generateFibList(num):
    lst = [1, 2]
    while lst[len(lst) - 1] < num:
        lst += [lst[len(lst) - 1] + lst[len(lst) - 2]]
    lst.pop()
    return lst

def digitsInFibList(num):
    lst = ""
    fibList = generateFibList(num)
    for fibNum in fibList[::-1]:
        if num >= fibNum:
            lst += "1"
            num -= fibNum
        else:
            lst += "0"
    return lst



# endregion

# region 5. feladat

def numberInFibList(lst):
    if len(lst) == 1:
        return int(lst[0])
    lst = lst[::-1]
    num = int(lst[0]) + int(lst[1]) * 2
    a, b = 1, 2
    for x in lst[2:]:
        c = a + b
        num += c * int(x)
        a = b
        b = c
    return num

# endregion

# region 6. feladat

def nthFibNumber(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    n -= 2
    while n != 0:
        c = a + b
        a = b
        b = c
        n -= 1
    return c

def firstAndLastDigitOfnthFibNumber(n):
    num = nthFibNumber(n)
    return firstDigit(num), num % 10

# endregion

if __name__ == '__main__':
    # decimal 
    print(firstDigit(346314))
    print(numberOfDigits(112323))
    print(numberOfEvenDigits(112323))
    print(firstDigitInB(20, 8))
    print(numberOfDigitsEqualKInB(18 + 2 * 8 ** 2, 8, 2))

    # converts
    print(convBtoBk([1, 0, 1, 1, 1, 0, 1, 1], 2, 3))
    print(convBkToB([2, 7, 3], 2, 3))

    print(convBkToB([200, 123, 440, 50], 3, 6))
    print(convBtoBk(convBkToB([200, 123, 440, 50], 3, 6), 3, 6))

    print(largerDigitInBinK([1, 0, 1, 1, 1, 0, 1, 1], 3))

    # fibonacci 
    print(generateFibList(49))
    print(digitsInFibList(49))
    print(numberInFibList("10100010"))

    print(nthFibNumber(14))
    print(firstAndLastDigitOfnthFibNumber(14))