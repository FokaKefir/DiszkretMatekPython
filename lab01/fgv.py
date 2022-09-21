def aritMuveletek2(x, y):
    print("A ket szam:", x, y)
    print("A ket szam osszege:", x + y)

def aritMuveletek():
    x = 10
    y = 12
    print("A ket szam:", x, y)
    print("A ket szam osszege:", x + y)

def strMuveletek():
    x = "diszkret matek"
    y = "szamtech"
    print(x + " " + y)
    print("Az x tipusa", type(x))
    print(3 * (x + " "))

def strMuveletek2(x, y):
    print(x + " " + y)
    print("Az x tipusa", type(x))
    print(3 * (x + " "))

aritMuveletek2(12, 23)
strMuveletek2("diszkret matek", "szamtech")