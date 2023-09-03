import random

n = random.randint(5, 10)
lst = [random.randint(0, 15) for _ in range(n)]

def bubble(arr):
    print("Arr =",arr)
    L = len(arr)
    for i in range(L):
        for a in range(0, L-1):
            if arr[a] > arr[a+1]:
                arr[a], arr[a + 1] = arr[a + 1], arr[a]
            print(arr)
        print("end bucle 1")

bubble(lst)