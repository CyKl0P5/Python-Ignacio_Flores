class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self


x = MathDojo()

x = x.add(2).add(2,10,3).add(100).subtract(3,2).result
print(x) 