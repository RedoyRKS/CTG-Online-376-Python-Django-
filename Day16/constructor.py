class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def dispalyCarInfo(self):
        print(f"{self.name} {self.model} {self.year}")


my_car = Car("Toyota", "Camry", 2023)

my_car.dispalyCarInfo()
