# #Create a class Rectangle with a constructor to initialize length and width. Write a method to calculate the area and perimeter.
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate(self):
        area = self.length * self.width
        perimeter = 2 * (self.length + self.width)

        print("Area:", area)
        print("Perimeter:", perimeter)


rectangle1 = Rectangle(10, 50)
rectangle1.calculate()

class Car:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def display(self):
        print("Car Name:", self.name)
        print("Car Model:", self.model)


car1 = Car("BMW", "X5")
car2 = Car("Audi", "A6")

car1.display()
car2.display()

class Resort:

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display(self):
        print("Resort Name:", self.name)
        print("Location:", self.location)


resort1 = Resort("Taj Resort", "Goa")
resort2 = Resort("Blue Ocean", "Chennai")

resort1.display()
resort2.display()


    