import random

def selection(list):
    print("lista =",list)
    for i in range(0, len(list)-1):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    print(list)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(lst)
selection(lst)