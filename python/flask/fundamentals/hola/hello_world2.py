#Print Hello World
print("Hello World")

#Name var 1
name = "ignacio"

print ("Hello",name)
print ("Hello"+ name)

#Name var 2
name = 42

print ("Hi",str(name))
print ("Hi",str(name))

#Favorite Food
fave_food1 = "sushi"
fave_food2 = "pizza"

#Printing using a .format code type
print (f'I love to eat {fave_food1}')
print (f'I love to eat {fave_food2}')

#Another ways to say "Hello World" lmao

#First Way
saying_hello = "hello world"
busy_tosay_hello = "bye world"


print (f'{saying_hello}')
print (f'{busy_tosay_hello}')


#Plan B: Randomizer

import random

saludos = ['Hello_World', 'Hello World', 'Hola Mundo', 'Hallo Welt']
sal = random.choice(saludos)

print(f'Translating... {sal}')

if sal == 'Hallo Welt':
        print('Successfully Traduced to German')
elif(sal == 'Hola Mundo'):
        print('Successfully Traduced to Spanish')
else:
        print('Error 404')


