'''
    Inheritance: Create a Student class that inherits from the Person class. Add a new course attribute and a study method that prints a message indicating that the student is studying in their respective course.
'''

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender 
        
    def introduce(self):
        return(f"My name is {self.name}, I'm {self.age} and my gender is: {self.gender} ")
    
    
class Student(Person):
    def __init__(self, name, age, gender, course):
        super().__init__(name, age, gender)
        self.course = course
    
    def study(self):
        return(f"{self.name} is in the course {self.course}, {self.name} is {self.age} years old and the gender is: {self.gender}")
           
        
johan = Student("Johan", 25, "M", "Programming")
print(johan.introduce())