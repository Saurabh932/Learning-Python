'''
    Methods are basically the functions that belongs to Object
'''

class Employee:  # Class
    
    def __init__(self, name, role): # Constructor
        self.name = name
        self.role = role
        
    def hello(self):  # Method
        print(f"Hi employee {self.name}, you are working as {self.role}")
        
e1 = Employee("Saurabh", "SDE-1")
e1.hello()