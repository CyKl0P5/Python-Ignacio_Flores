import unittest
import random

def reverseList(list):
    for i in range(0, int(len(list) / 2)):
        list[i], list[len(list) - 1 - i] = list[len(list) - 1 - i], list[i]
    return list

def isPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
def monedas(val):
    m25, m10, m5, m1, vuelto = 25, 10, 5, 1, val
    t = [0, 0, 0, 0]
    x = 0
    j = 1
    while True:
        for j in range(1,val):
            x = m25 * j
            if x >= vuelto:
                t[0] = j - 1
                x -= m25
                break
        for j in range(1,val):
            x += m10 * j
            if x >= vuelto:
                t[1] = j - 1
                x -= m10 * j
                break
        for j in range(1,val):
            x += m5 * j
            if x >= vuelto:
                t[2] = j - 1
                x -= m5 * j
                break
        for j in range(1,val):
            x += m1
            if x >= vuelto:
                t[3] = j
                break
        break
    return t

def factorial(Val):
    list = []
    result = Val
    for i in range(Val, 0, -1):
        list.append(i)
    print(list)
    for i in range(1, Val - 1):
        result *= list[i]
    return result

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

class IsEvenTests(unittest.TestCase):
    def testOne(self):
        lista1 = [random.randint(1,100) for _ in range(10)]
        lista2 = lista1[::-1]
        self.assertEqual(reverseList([1, 2, 3]),[3, 2, 1])
        self.assertEqual(reverseList([4,3,2,1]),[1, 2, 3, 4])
        self.assertEqual(reverseList(lista1), lista2)
        print("Test1 Lista inversa")

    def testTwo(self):
        self.assertTrue(isPalindrome("racecar"))
        self.assertFalse(isPalindrome("A Car, A Torch, A Death"))
        self.assertTrue(isPalindrome("aibofobia"))
        self.assertFalse(isPalindrome("amongus"))
        self.assertTrue(isPalindrome("TDDT"))
        print("Test2 Palindromo")

    def  testTree(self):
        self.assertEqual(monedas(56), [2,0,1,1])
        self.assertEqual(monedas(444), [17,1,1,4])
        self.assertEqual(monedas(731), [29,0,1,1])
        self.assertEqual(monedas(214), [8,1,0,4])
        self.assertEqual(monedas(1000), [39,1,1,10])
        print("Test3 Cambio")

    def testFour(self):
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(1), 1)
        print("Test4 Factorial")

    def testFive(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(1), 1)
        print("Test5 Factorial")

    def setUp(self):
        print("Test iniciado")

    def tearDown(self):
        print("Test finalizado")

if __name__ == '__main__':
    unittest.main()