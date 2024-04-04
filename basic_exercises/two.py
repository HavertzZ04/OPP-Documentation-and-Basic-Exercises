'''
    Extend the Person class by adding a method called introduce that prints an introduction message including the name and age of the person.
'''

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender 
        
    def introduce(self):
        return(f"My name is {self.name}, I'm {self.age} and my gender is: {self.gender} ")
        
johan = Person("Johan", 25, "M")
print(johan.introduce())