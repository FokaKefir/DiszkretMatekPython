import random
import math

# region 1. task

def middleSquare(r, n):
    k = len(str(r))
    for _ in range(n):
        rStr = str(r * r)
        x = (len(rStr) - k) // 2
        r = int(rStr[x:x+k])
    return r

def middleSquarePeriod(r):
    k = len(str(r))
    lst = []
    while len(lst) == len(set(lst)):
        rStr = str(r * r)
        x = (len(rStr) - k) // 2
        r = int(rStr[x:x+k])
        lst += [r]
    return lst


def task1():
    with open("lab12/midlSqr.txt", "rt") as fin:
        maxmid = ()
        for row in fin:
            seed = int(row)
            lst = middleSquarePeriod(seed)
            print(seed, lst)
            if maxmid == () or len(lst) > len(maxmid[1]):
                maxmid = (seed, lst)
        print(maxmid)
            

# endregion

if __name__ == "__main__":
    task1()