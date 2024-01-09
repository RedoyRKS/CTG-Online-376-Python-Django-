# #single inheritence - class A in Class B
# class A:
#     def displayA(self):
#         print("I am from Class A")

# class B(A):
#     def displayB(self):
#         print("I am from Class B")


# obj = B()
# obj.displayA()

#Multilavel inheritence

# class A:
#     def displayA(self):
#         print("I am from Display A")

# class B(A):
#     def displayB(self):
#         print("I am from Display B")

# class C(B):
#     def displayC(self):
#         print("I am from Display C")

# obj = C()
# obj.displayA()   
# ***********************************
#Example:

# class Animal:
#     def __init__(self, name):
#         self.animalName = name

#     def speak(self):
#         print(f"{self.animalName} makes a sound") 

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.animalName} barks")

# class Poodle(Dog):
#     def dance(self):
#         print(f"{self.animalName} dance")

# animal_obj = Animal("Any type of Animal")
# dog_obj = Dog("Buddy Dog")
# poodle_obj = Poodle("Fluffy")

# animal_obj.speak()
# dog_obj.bark()

# poodle_obj.speak()
# poodle_obj.bark()
# poodle_obj.dance()


# multiple.........

class A:
    def displayA(self):
        print("I am from Display A")

class B:
    def displayB(self):
        print("I am from Display B")

class C(A,B):
    def displayC(self):
        print("I am from Display C")

obj = C()
obj
