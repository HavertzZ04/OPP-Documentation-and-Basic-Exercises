'''
    Create a basic class: Create a class called Person that has attributes such as name, age, and gender. Then, create an instance of this class and print its attributes.
'''

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender 
        
    def data(self):
        return(f'Name: {self.name}, Age: {self.age}, Gender: {self.gender} ')
        
johan = Person("Johan", 25, "M")
print(johan.data())

