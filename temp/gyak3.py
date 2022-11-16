

# region 1. taks

def auxFarey(n, lst):
    nLst = []
    for i in range(len(lst) - 1):
        a1, a2 = lst[i]
        b1, b2 = lst[i + 1]
        nLst += [lst[i]]
        if a2 + b2 <= n:
            nLst += [(a1 + b1, a2 + b2)]
    
    nLst += [lst[-1]]
    return nLst

def farey(n):
    lst = [(0, 1), (1, 1)]
    for i in range(2, n + 1):
        lst = auxFarey(i, lst)
    return lst

def task1():
    n = 5
    lst = farey(n)
    even = 0
    odd = 0
    for a, b in lst:
        if b % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Paros:", even, "Paratlan:", odd)

# endregion

# region 2. taks

def task2():
    filename = "temp/words.txt"
    string = ""
    for word in open(filename, "rt"):
        string += word
    string = string.replace("\n", "-")
    
    while string[-1] == "-":
        string = string[:len(string) - 1]
    print(string)

# endregion

# region 3. taks

def task3():
    filename = "temp/szamparok.txt"
    mini = ()
    for row in open(filename, "rt"):
        data = row.split(" ")
        a, b = int(data[0]), int(data[1])
        if len(mini) == 0:
            mini = (a, b)
        elif a / b < mini[0] / mini[1]:
            mini = (a, b)
    print(mini)


# endregion

if __name__ == "__main__":
    task3()