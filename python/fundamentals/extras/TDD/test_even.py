import unittest

#Test
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

# inicializado creando una clase que hereda de unittest.TestCase
class IsEvenTests(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(isEven(2), True)
        #otra forma de escribir lo de arriba(mas rapido)
        self.assertTrue(isEven(2))

    def testThree(self):
        self.assertEqual(isEven(3), False)
        #otra forma de escribir lo de arriba(mas rapido)
        self.assertFalse(isEven(3))

    def setUp(self):
        print("running setUp")

    def tearDown(self):
        print("running tearDown task")

if __name__ == '__main__':
    unittest.main()