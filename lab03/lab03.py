
# region input

def inputPair():
    temp = input("a, b: ")
    if temp == "" or temp is None:
        return -1
    try:
        a, b = temp.split()
        a, b = int(a), int(b)
    except:
        return -2
    return a, b

# endregion

# region 1. feladat

def lnko(a, b):
    if b == 0 or a == b:
        return a
    a = abs(a)
    b = abs(b)
    if a > b:
        return lnko(b, a % b)
    elif b > a:
        return lnko(a, b % a)

# endregion

# region 2. feladat

def racionalisOsszeg(num1, num2):
    num = (num1[0] * num2[1] + num2[0] * num1[1], num1[1] * num2[1])
    x = lnko(num[0], num[1])
    num = (num[0] // x, num[1] // x)
    return num

def racionalisKivonas(num1, num2):
    num2 = (-num2[0], num2[1])
    return racionalisOsszeg(num1, num2)

def racionalisSzorzat(num1, num2):
    num = (num1[0] * num2[0], num1[1] * num2[1])
    x = lnko(num[0], num[1])
    num = (num[0] // x, num[1] // x)
    return num

def racionalisOsztas(num1, num2):
    num2 = (num2[1], num2[0])
    return racionalisSzorzat(num1, num2)

def racionalisAbs(num):
    num = (abs(num[0]), abs(num[1]))
    return num

# endregion

# region 3. feladat

def racionalisHatvany(num, n):
    x = lnko(num[0], num[1])
    num = (num[0] // x, num[1] // x)
    return (num[0] ** n, num[1] ** n)

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

# endregion

if __name__ == '__main__':
    lst = [(0, 1), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4), (1, 1)]
    nLst = auxFarey(5, lst)
    print(nLst)
    print(len(nLst))