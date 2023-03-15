#First Loop (0 to 150)
for x in range(0,151):
    print(x)

#Loop number two (5 to 1000)
for x in range(0,1000,5):
    print(x)

#Loop to "Dojo's Way" (0 to 100)
for x in range(0,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else: print(x)

#Loop "Whoa is a big Fool" (0 to 500)
y = 0
for x in range(0,500000):
    if x % 2 != 0:
        y += x
print(y)

#Loop 4 to 4
for x in range(2018,0,-4):
    print(x)

#Loop with var
lowNum = 0
highNum = 20
Mult = 5

for x in range(lowNum,highNum):
    if x % Mult == 0:
        print(x)