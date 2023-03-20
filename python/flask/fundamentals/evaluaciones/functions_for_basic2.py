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

#4 Valores Mayores Que El Segundo
def valores_mayores_que_el_segundo(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output
print(valores_mayores_que_el_segundo([5,2,3,2,1,4]))
print(valores_mayores_que_el_segundo([3]))

#5 Esta longitud, Este valor
def longitud_y_valor(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output
print(longitud_y_valor(5,3))
print(longitud_y_valor(6,9))