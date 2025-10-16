'''
    All classes have a function called __init__(), 
    which is always executed when the object is called.

    The self parameter is a reference to the current instance of the class,
    and is used to access variables that belongs to the class
'''

class Employee:
    company_name = "TCS"  # Common for all
    def __init__(self, name, location, role):   # Constructor (default)
        print("Adding employee info to database")
        self.name = name
        self.location = location
        self.role = role 
        
saurabh = Employee("Saurabh", "Nagpur", "SDE")
print(saurabh.name, saurabh.location, saurabh.role)