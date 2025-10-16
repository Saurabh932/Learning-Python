class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
        
    def showDetails(self):
        print(f"Role = {self.role}")
        print(f"Department = {self.dept}")
        print(f"Salary = {self.salary}")
        
        
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "654654648")
        
emp1 = Employee("Accountant", "Finance", "582151")
emp1.showDetails()
print()
eng1 = Engineer("Saurabh", "23")
eng1.showDetails()