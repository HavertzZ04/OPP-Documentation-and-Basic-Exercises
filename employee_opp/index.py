class Employee:
    def __init__(self, name, age, salary, company_position):
        self.name = name.title()
        self.age = age
        self.salary = salary
        self.company_position = company_position.title()
        
    def employee_details(self):
        return f"Employee: {self.name} / Age: {self.age} / salary: {self.salary} / Position: {self.company_position}"
    
    
class EmployeeDatabase:
    def __init__(self):
        self.employees_list = []
        
    def add_employees(self, employee):
        self.employees_list.append(employee)
    
    def search_employees(self, key_word): #name or position
        found_employee = False
        for person in self.employees_list:
            if key_word.title() in [person.name, person.company_position]:
                print(f"Employee: {person.name} / Age: {person.age} / salary: {person.salary} / Position: {person.company_position}")
                found_employee = True 
        if not found_employee:
            print("We were not able to find employees with the info you provided")
     
    def show_all_employees(self):
        show_all = False
        for person in self.employees_list:
                print(f"Employee: {person.name} / Age: {person.age} / salary: {person.salary} / Position: {person.company_position}")
                show_all = True
        if not show_all:
            print("We have not employees yet, the list is empty")
    
    def company_total_salary(self):
        show_all_salarys = False
        total_salary = 0
        for person in self.employees_list:
                total_salary += person.salary
                show_all_salarys = True
        print(f"The company salary is : {total_salary}")
                
        if not show_all_salarys:
            print("We have not salaries to show, the list is empty")
        

#create new employees
employee1 = Employee("johan", 25, 2650000, "voice agent")
employee2 = Employee("gabriel", 23, 2850000, "Voice Agent")

#create a new data base
mainDataBase = EmployeeDatabase()

#addedING employee tos the employee list
mainDataBase.add_employees(employee1)
mainDataBase.add_employees(employee2)

#searching employes
mainDataBase.search_employees("JOHAN")
mainDataBase.show_all_employees()

#show all the salarys
mainDataBase.company_total_salary()

