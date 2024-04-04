'''
    Polymorphism: Create a base class called Figure with a calculate_area method. Next, create two derived classes, Triangle and Rectangle, that implement the calculate_area method differently to calculate the area of ​​a triangle and a rectangle respectively.
'''

class Figure:
    def __init__(self, base, height):
        self.base = base
        self.height = height   
    
class Triangle(Figure):
    def __init__(self, base, height):
        super().__init__(base, height)
        
    def calculate_area(self):
        area = 0.5 * self.base * self.height
        return area

class Rectangle(Figure):
    def __init__(self, base, height):
        super().__init__(base, height)
        
    def calculate_area(self):
        area = self.base * self.height
        return area
    
obj1 = Rectangle(10, 2)
obj2 = Triangle(10, 2)

print(obj1.calculate_area())
print(obj2.calculate_area())

    