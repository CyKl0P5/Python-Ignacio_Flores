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
    return(print)