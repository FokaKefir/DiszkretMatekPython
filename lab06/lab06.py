import random

# region 1. task

def generateRandomNumberOnNBit(n):
    num = 0
    for i in range(n):
        num = (num << 1) + random.randint(0, 1)
    return num 

def numberOfOneBits(num):
    nBits = 0
    while num:
        num &= num - 1
        nBits += 1
    return nBits

def task1():
    n = 32
    num1 = generateRandomNumberOnNBit(n)
    num2 = generateRandomNumberOnNBit(n)
    numOR = num1 | num2
    numAND = num1 & num2
    numXOR = num1 ^ num2
    print(numOR, numberOfOneBits(numOR))
    print(numAND, numberOfOneBits(numAND))
    print(numXOR, numberOfOneBits(numXOR))

# endregion 

# region 2. task

def task2():
    n = 32
    num1 = 2 ** n
    num2 = 2 ** n - 1
    num3 = 2 ** n + 1
    print(num1, numberOfOneBits(num1))
    print(num2, numberOfOneBits(num2))
    print(num3, numberOfOneBits(num3))

# endregion

# region 3. task

def task3():
    filename = "lab06/in.txt"
    foutBin = "lab06/outbin.txt"
    foutHex = "lab06/outhex.txt"

    inp = open(filename, "rb")
    byts = inp.read()
    inp.close()

    outBin = open(foutBin, "wt")
    outHex = open(foutHex, "wt")

    for i, byt in enumerate(byts, start=1):
        bn = bin(byt)[2:]
        bn = "0" * (8 - len(bn)) + bn
        hx = hex(byt)[2:]
        hx = "0" * (2 - len(hx)) + hx

        outBin.write(bn + " ")
        if i % 4 == 0:
            outBin.write("\n")
        outHex.write(hx + " ")
        if i % 16 == 0:
            outHex.write("\n")
        


# endregion

if __name__ == "__main__":
    task3()
    
    