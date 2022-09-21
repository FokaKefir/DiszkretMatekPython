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
    print(x, end=' ')
    if x >= 0:
        print("pozitiv")
    else:
        print("negativ")

def szamEgeszei(x):
    if type(x) == int:
        print(x, "szam egesz szam")


if __name__ == "__main__":
    x = 10
    y = 2
    ketSzamMuveletei(x, y)
    print(myMin(x, y))
    print(abszolutErtek(-7))
    szamElojele(-4)
    szamEgeszei(2)
    
