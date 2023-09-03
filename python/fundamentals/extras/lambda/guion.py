class Underscore:
    def map(self, iterable, callback):
        print("map: ", list(map(callback, iterable)))
    def find(self, iterable, callback):
        for i in iterable:
            if callback(i):
                print("find:", i)
                break
    def filter(self, iterable, callback):
        print("filter:", list(filter(callback, iterable)))
    def reject(self, iterable, callback):
        print("reject:", list(filter(lambda x: not callback(x), iterable)))
# acabas de crear una biblioteca con 4 métodos!

# creemos una instancia de nuestra clase
_ = Underscore() # sí, estamos configurando nuestra instancia a una variable que es un underscore

evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# debe devolver [2, 4, 6] después de que termine de implementar el código anterior
_.map([1,2,3], lambda x: x*2) # debería devolver [2,4,6]
_.find([1,2,3,4,5,6], lambda x: x>4) # debería devolver el primer valor que sea mayor que 4
_.filter([1,2,3,4,5,6], lambda x: x%2==0) # debería devolver [2,4,6]
_.reject([1,2,3,4,5,6], lambda x: x%2==0) # debería devolver [1,3,5]