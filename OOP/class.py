class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")

my_car = Car("Toyota", "Camry", 2022)
my_car.display_info()

another_car = Car("Honda", "Civic", 2021)
another_car.display_info()
