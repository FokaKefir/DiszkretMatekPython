import math

# region 1. feladat

def ketSzamMuveletei(x, y):
    print("A ket szam:", x, y)
    print("osszeg:", x + y)
    print("kulonbseg:", x - y)
    print("szorzat:", x * y)
    print("hanyados:", x / y)
    print("osztasi maradek:", x % y)

def myMax(x, y):
    if x > y:
        return x
    else:
        return y

def myMin(x, y):
    if x < y:
        return x
    else:
        return y

def elsofokuEgyenletGyoke(a, b):
    if a == 0:
        print("Az a nem lehet 0")
    else:
        return -b / a

def abszolutErtek(x):
    if x < 0:
        x = -x
    return x

def szamElojele(x):
    if x >= 0:
        return "pozitiv"
    else:
        return "negativ"

def szamEgeszei(x):
    if type(x) == int:
        print(x, "szam egesz szam")
        return
    else:
        return (math.floor(x), math.ceil(x))

def masodfokuEgyenletGyokei(a, b, c):
    if a == 0:
        print("Az a nem lehet 0")
    else:
        delta = (b ** 2) -4 * a * c
        if delta < 0:
            print("Komplex megoldas")
            return
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)

def szuksegesBitek():
    k = int(input("Enter a number: "))
    if k % 8 == 0:
        return k // 8
    else:
        return k // 8 + 1

# endregion

# region 2. feladat

def generalNigTermeszetesSzamot(n):
    lista = list(range(1, n + 1))
    return lista

def generalNdbParosSzamot(n):
    lista = list(range(2, 2*n+1, 2))
    return lista

def generalNdbParatlanSzamot(n):
    lista = list(range(1, 2*n, 2))
    return lista

def generalNdbNegyzetszamot(n):
    lista = [x ** 2 for x in range(1, n+1)]
    return lista

def elsoNSzamOsszege(n):
    return n * (n + 1) // 2

def elsoNSzamSzorzata(n):
    return math.factorial(n)

# endregion

# region tobbi feladat

def kettoNdikHatvanyokon(n):
    lista = [2 ** x for x in range(1, n+1)]
    return lista

def xAzNdikHatvanyokon(x, n):
    lista = [x ** i for i in range(1, n+1)]
    return lista

def legnagyobbSzamSorszama(n):
    num, ind = float(input()), 0
    for i in range(1, n):
        x = float(input())
        if x > num:
            num, ind = x, i
    return ind

def legnagyobbSzamSorszama2(n):
    lst = list(input("Enter your numbers in one row: ").split())
    lst = [float(x) for x in lst]
    ind, num = 0, lst[0]
    for i, x in enumerate(lst):
        if x > num:
            ind, num = i, x
    return ind, num

def szamokOsszege(n):
    sum = 0
    for i in range(n):
        sum += float(input())
    return sum

def szamokOsszege2(n):
    lst = list(input("Enter your numbers in one row: ").split())
    lst = [float(x) for x in lst]
    return sum(lst)

def szamokSzorzata(n):
    mul = 1
    for i in range(n):
        mul *= float(input())
    return mul

def szamokSzorzata2(n):
    lst = list(input("Enter your numbers in one row: ").split())
    lst = [float(x) for x in lst]
    return math.prod(lst)


def nullasokSzamaNFaktorban(n):
    kettesek = 0
    otosok = 0
    tizesek = 0
    for i in range(1, n+1):
        tmp = i
        while tmp % 10 == 0:
            tizesek += 1
            tmp /= 10
        while tmp % 2 == 0:
            kettesek += 1
            tmp /= 2
        while tmp % 5 == 0:
            otosok += 1
            tmp /= 5
    
    return tizesek + min(kettesek, otosok)
    
def nullasokSzamaNFaktorban2(n):
    cnt = 0
    fv = 5
    while n // fv:
        cnt += n // fv
        fv *= 5
    return cnt

# endregion


if __name__ == "__main__":
    n = int(input("Enter your number:"))
    #print(kettoNdikHatvanyokon(n))
    #print(xAzNdikHatvanyokon(3, n))
    #print(legnagyobbSzamSorszama(n))
    #print(legnagyobbSzamSorszama2(n))
    #print(szamokOsszege2(n))
    #print(szamokOsszege(n))
    #print(szamokSzorzata(n))
    #print(szamokSzorzata2(n))
    #print(nullasokSzamaNFaktorban(n))
    print(nullasokSzamaNFaktorban2(n))

    
    
    
