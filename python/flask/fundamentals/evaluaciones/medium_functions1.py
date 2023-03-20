#1 hacer una update en listas y diccionarios

#1.1 cambiar el valor 10 en "x" a 15. Una vez terminado, x deberia ser "[ [5,2,3], [15,8,9] ]"
x = [ [5,2,3], [10,8,9]]

changevalue = x[1][0]
print(changevalue)
x[1][0] = 15
print(x)

#1.2 cambiar "apellido" del primer alumno de "jordan a Bryant"
students = [
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(students [0])
print(students[0]['last_name'])
students[0]['last_name'] = 'Bryant'
print(students[0]['last_name'])
print(students[0])

#1.3 En sports_dir, se cambiaria "Messi" por "Andrés"
sports_dir = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'football' : ['Messi', 'Ronaldo', 'Rooney']
}

print(sports_dir['football'][0])
sports_dir['football'][0] = 'Andrés'
print(sports_dir['football'][0])
print(sports_dir)

#1.4 cambiar valor 20 en z a 30
print()