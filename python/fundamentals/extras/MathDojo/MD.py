class MathDojo:
    def __init__(self):
        self.resultado = 0
    
    def add(self, num, *nums):
        self.resultado += num
        for i in nums:
            self.resultado += i
        return self
    
    def subtract(self, num, *nums):
        self.resultado -= num
        for i in nums:
            self.resultado -= i
        return self

x = MathDojo()
x = x.add(2).add(2,10,3).add(100).subtract(3,2).subtract(7).subtract(20,2).resultado
print(x)