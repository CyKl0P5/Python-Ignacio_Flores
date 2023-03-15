#First Loop (0 to 151)
for x in range(0,151):
    print(x)

#Loop number two (5 to 1000)
for x in range(0,1000,5):
    print(x)

#Loop to "Dojo's Way" (0 to 100)
for x in range(0,100):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
        print(x)