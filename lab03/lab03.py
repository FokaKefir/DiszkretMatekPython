import math

# region 1. feladat

def rationalSimple(num):
    x = gcd(num[0], num[1])
    num = (num[0] // x, num[1] // x)
    return num

def gcd(a, b):
    if b == 0 or a == b:
        return a
    a = abs(a)
    b = abs(b)
    if a > b:
        return gcd(b, a % b)
    elif b > a:
        return gcd(a, b % a)

# endregion

# region 2. feladat

def rationalAdd(num1, num2):
    num = (num1[0] * num2[1] + num2[0] * num1[1], num1[1] * num2[1])
    x = gcd(num[0], num[1])
    num = (num[0] // x, num[1] // x)
    return num

def rationalSub(num1, num2):
    num2 = (-num2[0], num2[1])
    return rationalAdd(num1, num2)

def rationalMul(num1, num2):
    num = (num1[0] * num2[0], num1[1] * num2[1])
    x = gcd(num[0], num[1])
    num = (num[0] // x, num[1] // x)
    return num

def rationalDiv(num1, num2):
    num2 = (num2[1], num2[0])
    return rationalMul(num1, num2)

def rationalAbs(num):
    num = (abs(num[0]), abs(num[1]))
    return num

# endregion

# region 3. feladat

def rationalPow(num, n):
    x = gcd(num[0], num[1])
    num = (num[0] // x, num[1] // x)
    return (num[0] ** n, num[1] ** n)

# endregion

# region 4. feladat

def auxRationalNumbersList(n):
    if n % 2 == 0:
        lst = [(n - x + 1, x) for x in range(1, n + 1)]
    else:
        lst = [(x, n - x + 1) for x in range(1, n + 1)]
    return lst

def rationalList(n):
    rNumbers = set()
    for i in range(1, n + 1):
        for num in auxRationalNumbersList(i):
            rNumbers.add(rationalSimple(num))
    return list(rNumbers)

# endregion

# region 5. feladat

def positionRationalNumberInList1(num):
    i = 1
    pos = 1
    while True:
        for j in range(1, i + 1):
            if num == (j, i - j + 1):
                return pos
            pos += 1
        i += 1

def positionRationalNumberInList2(num):
    pos = 1
    aNum = (1, 1)
    while num != aNum:
        nNum = rationalSub((2 * math.floor(aNum[0] / aNum[1]) + 1, 1), aNum)
        aNum = (nNum[1], nNum[0])
        pos += 1
    return pos


# endregion

# region 6. feladat

def continuedFraction(num):
    if num[0] == 0:
        return [0]
    if num[1] == 1:
        return [num[0] - 1, 1]
    return [num[0] // num[1]] + continuedFraction((num[1], num[0] - (num[0] // num[1]) * num[1]))


# endregion

# region 7. feladat 

def auxFarey(n, lst):
    newLst = []
    for i in range(len(lst) - 1):
        a1, a2 = lst[i]
        b1, b2 = lst[i + 1]
        newLst += [lst[i]]
        if a2 + b2 <= n:
            newLst += [(a1 + b1, a2 + b2)]

    newLst += [lst[-1]]
    return newLst

def farey(n):
    if n < 1:
        return "Choose greater number than 0"
    lst = [(0, 1), (1, 1)]
    for i in range(2, n + 1):
        lst = auxFarey(i, lst)
    return lst

# endregion

# region 8. feladat

def fareyListContinuedFraction(n):
    lst = farey(n)
    for num in lst:
        print(num, end=": ")
        cf = continuedFraction(num)
        print(cf, "sum =", sum(cf))

# endregion

if __name__ == '__main__':
    fareyListContinuedFraction(5)