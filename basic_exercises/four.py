'''
    Encapsulation: Modifies the Person class to make attributes private and provides methods to safely access and modify these attributes.
'''

class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender 
        
    def get_info(self):
        return self.__name, self.__age, self.__gender
    
    def set_info(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
           
           
person1 = Person("Johan", 25, "M")

#show object info:
print(person1.get_info())

#edit object info:
person1.set_info("Gabriel", 22, "M")

#show object updated:
print(person1.get_info())