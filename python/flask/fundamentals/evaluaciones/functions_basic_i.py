#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

#Prediction: el resultado en la consola seria "5"


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

#Prediction: el resultado en consola daria error ya que el nombre usado en "print" no esta definido


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

#Prediction: el resultado seria "5" ya que primero retorna a 5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

#Prediction: el resultado seria "10"

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

#Prediction: no se imprimiria nada porque "numer_of_great_lakes" no tiene valora asignado

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

#Prediction: no sumara porque la funcion no esta devolviendo ningun tipo de valor

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

#Prediction: imprimiria "2 y 5" en string

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

#Prediction: imprimiria primero 100 y regresara a 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#Prediction: primero imprimiria 7, luego 14 y al final 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

#Prediction: imprimiria 8 e ignoraria el "return 10"

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

#Prediction: imprimiria 500 2 veces y despues imprimiria 300 para al final imprimir 500 denuevo

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

#Prediction: imprimiria 500 2 veces despues 300 para al final imprimir 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

#Prediction: primero imprimiria 500 2 veces, luego 300 2 veces y a "b" se le da el valor de la funcion "foobar()"

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

#Prediction: imprimiria 1, luego llamara a la funci``òn "bar()" e imprimiria 3 y por ultimo 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

#Prediction: imprimiria 1, despues declara que "x" es igual a "bar()" e imprimiria 3, luego 5 y por ultimp 10