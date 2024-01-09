# class Animal:
#     legs = 4

# dog = Animal()
# print(dog.legs)

class DemoClass:
    a = 10

    def showValue(self):
        print(self.a)

    def sumOf(self, valueOne, valueTwo): 
        print(valueOne+valueTwo*self.a)


obj = DemoClass()

obj.showValue()

obj.sumOf(10,10)