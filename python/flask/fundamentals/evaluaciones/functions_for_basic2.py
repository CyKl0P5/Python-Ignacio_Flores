#1 Cuenta regresiva
def countdown(num):
    output = []
    for i in range(num,-1,-1):
        output.append(i)
        return output
print(countdown(5))

#2 Imprimir y devolver
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))

#3 Primero Más Longitud
def primero_mas_longitud(list):
    return list[0] + len(list)
print(primero_mas_longitud([1,2,3,4,5]))