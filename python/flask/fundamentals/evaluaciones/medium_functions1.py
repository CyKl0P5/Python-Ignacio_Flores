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
z = [ {'x' : 10, 'y' : 20} ]
print(z[0]['y'])
z[0]['y'] = 30
print(z) 

#2 iterar mediante una lista de diccionarios

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(x):
    for i in x:
        atletic = '' 
        for key in i:
            atletic += key + '-' + i[key] + ','
            print(atletic)

iterateDictionary(students)

#3 obtener valores de un diccionario

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan',},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def nameDictionary(k,x):
    for i in x:
        print(i[k])
nameDictionary('first_name', students)
nameDictionary('last_name', students)

#4 iterar a travez de un diccionario con valores en la lista

dojo = {
    'places': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(x):
    print(len(x['places']), 'places'.upper())
    for place in x['places']:
        print (place)
    print('')
    print(len(x['instructors']), 'instructors'.upper())
    for instructor in x['instructors']:
        print (instructor)

printInfo(dojo)