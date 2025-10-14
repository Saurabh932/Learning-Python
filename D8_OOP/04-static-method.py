'''
    Static Method - it is method that don't uses the self parameter (work at class level)
    
    Decorators allows us to wrap another function in order to extend the behaviour of the 
    wrapped function, without permanently modifying it.
'''

class Employee:  # Class
    
    def __init__(self, name, role): # Constructor
        self.name = name
        self.role = role
    
    @staticmethod   # Decorator 
    def welcome():
        print("Welcome to the company!")
        
    def hello(self):  # Method
        print(f"Hi employee {self.name}, you are working as {self.role}")
        
e1 = Employee("Saurabh", "SDE-1")
e1.welcome()
e1.hello()