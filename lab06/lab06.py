import random
import base64

# region 1. task

def generateRandomNumberOnNBit(n):
    return random.randint(2 ** (n - 1), 2 ** n - 1)
    #num = 0
    #for i in range(n):
    #    num = (num << 1) + random.randint(0, 1)
    #return num 

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
    byts = byts.replace(b'\r', b'')
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
    outBin.close()
    outHex.close()

def task3_2():
    filename = "lab06/in.txt"
    foutBin = "lab06/outbin.txt"
    foutHex = "lab06/outhex.txt"

    with open(filename, "rb") as fin:
        byts = fin.read()
        byts = byts.replace(b'\r', b'')

    strHex = ""
    strBin = ""
    ind = 1
    for byt in byts:
        hx = format(byt, 'x')
        strHex +=  "0" * (2 - len(hx)) + hx + ' '
        if ind % 16 == 0:
            strHex += '\n'

        bn = format(byt, 'b')
        strBin += "0" * (8 - len(bn)) + bn + ' '
        if ind % 4 == 0:
            strBin += '\n'

        ind += 1

    with open(foutHex, "wt") as fHex:
        fHex.write(strHex)
    with open(foutBin, "wt") as fBin:
        fBin.write(strBin)


# endregion

# region 4. task

def decodeFile(filename : str, fileOut, base : int):
    out = ""
    with open(filename, "rt") as fin:
        for row in fin:
            for strNum in row.strip().split(" "):
                num = int(strNum, base)
                c = chr(num)
                out += c
    with open(fileOut, "wt") as fout:
        fout.write(out)

def task4():
    filenameBin = "lab06/outbin.txt"
    foutFromBin = "lab06/frombin.txt"
    decodeFile(filenameBin, foutFromBin, base=2)
    filenameHex = "lab06/outhex.txt"
    foutFromHex = "lab06/fromhex.txt"
    decodeFile(filenameHex, foutFromHex, base=16)



# endregion

# region 5. task

def task5():
    with open("lab06/ascii.txt", "wt", encoding="utf-8") as fout:
        for i in range(0, 256):
            fout.write("%5s%5i" % (chr(i), i))
            fout.write("%11s" % format(i, 'b'))
            fout.write("%5s" % format(i, 'o'))
            fout.write("%4s" % format(i, 'x'))
            fout.write("%6s" % ' ')

            if i % 3 == 1:
                fout.write("\n")

# endregion

# region 6. task

def task6():
    filename = "lab06/in.txt"
    with open(filename, "rt") as fin:
        txt = fin.read()
        txt = txt.upper()
        print(txt)

# endregion

# region 7. task

def numberOfPrintableCharacters(txt : bytes):
    n = 0
    for b in txt:
        c = chr(b)
        if c.isprintable():
            n += 1
    return n

def task7():
    filename = "lab06/print.txt"
    with open(filename, "rb") as fin:
        txt = fin.read()
        n = numberOfPrintableCharacters(txt)
        print(n)

# endregion

# region 8. task

def encode(txt : bytes, key):
    out = ""
    for b in txt:
        out += chr(b ^ key)
    return out

def task8():
    filename = "lab06/print.txt"
    with open(filename, "rb") as fin:
        txt = fin.read()
        key = generateRandomNumberOnNBit(8)
        encodedTxt = encode(txt, key)
        print(encodedTxt)

# endregion

# region 9. task

def decodeStringFromBase64(encodedStr):
    bs = base64.b64decode(encodedStr)
    return bs.decode("ascii")

def encodeStringToBase64(mystr):
    mybytes = mystr.encode("ascii")
    encoded = base64.b64encode(mybytes).decode("ascii")
    return encoded

def task9():
    mystr = "Szia Pityu! Hogy vagy?"
    print(encodeStringToBase64(mystr))

# endregion

# region 10. task

def decToBase(num, base=256):
    numBase = []
    while (num):
        numBase = [num % base] + numBase
        num //= base
    return numBase

def encodeNumberToBase64(num):
    lst = decToBase(num, base=256)
    barray = bytearray()
    for x in lst:
        barray.append(x)
    bs = bytes(barray)
    return base64.b64encode(bs).decode("ascii")

def encodeNumberAndWriteToFile(num, filename):
    encodedNum = encodeNumberToBase64(num)
    with open(filename, "wt") as fout:
        fout.write(encodedNum)

def baseToDec(lst, base=256):
    num = 0
    k = 1
    for x in lst[::-1]:
        num += k * x
        k *= base
    return num

def decodeNumberFromBase64(encodedNum : str):
    bs = base64.b64decode(encodedNum)
    lst = []
    for b in bs:
        lst += [int(b)]
    return baseToDec(lst, base=256)

def decodeBase64ToNumberReadedFromFile(filename):
    with open(filename, "rt") as fin:
        encodedNum = fin.read()
        num = decodeNumberFromBase64(encodedNum)
    return num

def task10():
    num = generateRandomNumberOnNBit(1024)
    print(num)
    filename = "lab06/encoded_num_base64.txt"
    encodeNumberAndWriteToFile(num, filename)
    num2 = decodeBase64ToNumberReadedFromFile(filename)
    print(num2)

# endregion

# region 11. task

def encodeFileByKey(filename, filekey):
    key = generateRandomNumberOnNBit(8)
    keyBase64 = encodeStringToBase64(str(key))
    with open(filekey, "wt") as fkey:
        fkey.write(keyBase64)
    encodedContent = ""
    with open(filename, "rb") as fin:
        byts = fin.read()
        for b in byts:
            encodedContent += str(b ^ key) + " "
    with open(filename + ".txt", "wt") as fout:
        fout.write(encodedContent)
    return filename + ".txt"
            
def decodeFileByKey(filenameEncoded, filekey, extension=".pdf"):
    with open(filekey, "rt") as fkey:
        keyBase64 = fkey.read()
        key = int(decodeStringFromBase64(keyBase64))
    with open(filenameEncoded, "rt") as fin:
        content = fin.read()
        barray = bytearray()
        for strNum in content.split(" ")[:-1:]:
            num = int(strNum)
            barray.append(num ^ key)
        bs = bytes(barray)
    with open(filenameEncoded + extension, "wb") as fout:
        fout.write(bs)

def task11():
    filename = "lab06/large.pdf"
    fileKey = "lab06/key.txt"
    filenameEncoded = encodeFileByKey(filename, fileKey)
    extension = filename[filename.index('.'):]
    decodeFileByKey(filenameEncoded, fileKey, extension=extension)

# endregion

# region 12. task

def getKeyList(encodedKey : str):
    return list(base64.b64decode(encodedKey.encode()))

def getKeyNum(keyList, ind):
    return keyList[ind % (len(keyList))]

def cryptFileByKeyList(codedFile, keyList):
    barray = bytearray()
    for i, b in enumerate(codedFile):
        key = getKeyNum(keyList, i)
        barray.append(b ^ key)
    return bytes(barray)

def decodeFileByKeyList(encodedFile, keyList):
    barray = bytearray()
    for i, b in enumerate(encodedFile):
        key = getKeyNum(keyList, i)
        barray.append(b ^ key)
        if i == 3:
            if format(barray[0], 'x') != "25" or format(barray[1], 'x') != "50" or format(barray[2], 'x') != "44" or format(barray[3], 'x') != "46":
                return None
    return bytes(barray)

def task12():
    fileKeys = "lab06/adatokXOR.txt"
    with open(fileKeys, "rt") as fin:
        keys = dict()
        for row in fin.readlines():
            datas = row.replace('"', "").replace("\n", "").split(",")
            keys[datas[0]] = datas[1]

    filename = "lab06/cryptXOR"
    with open(filename, "rb") as fin:
        encodedFile = fin.read()
        for name, encodedKey in keys.items():
            keyList = getKeyList(encodedKey)
            decodedFile = decodeFileByKeyList(encodedFile, keyList)
            if decodedFile != None:
                with open(filename + ".pdf", "wb") as fout:
                    fout.write(decodedFile) 

def task12tmp():
    keyList = [88, 79, 82, 69, 110, 99, 114, 121, 112, 116, 75, 101, 121, 49, 57]
    filename = "lab06/large.pdf"
    with open(filename, "rb") as fin:
        file = fin.read()
        cryptFile = cryptFileByKeyList(file, keyList)
        fileBack = cryptFileByKeyList(cryptFile, keyList)
        with open(filename + ".txt.pdf", "wb") as fout:
            fout.write(fileBack)

# endregion

# region 13. task

def task13():
    pass

# endregion

if __name__ == "__main__":
    task12()
    