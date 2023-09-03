import random

def insercion(list):
    print("List:", list)
    for i in range(0, len(list)-1):
        if list[i+1] < list[i]:
            pop(list, i+1)
    print(list)

def pop(listas, y):
    h =listas[y]
    j = y
    while j > 0 and h < listas[j-1]:
        listas[j] = listas[j-1]
        j-= 1
    listas[j] = h
list = []
n = random.randint(1, 7)
for i in range(n):
    list.append(random.randint(0, 9))

insercion(list)