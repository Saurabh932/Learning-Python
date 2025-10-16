'''
    Encapsulation - it means wrapping data (variables) and methods (functions) 
                    into a single unit (a class) and restricting direct access to the data
                    — you control how it’s read or modified.

            It’s basically data hiding + controlled access using getters and setters.
'''

class Employee:
    def __init__(self, name, id, salary):
        self.name = name       # public attribute - can be accessed by anyone
        self.__id =id          # private attribute - access restricted
        self.__salary = salary # private attribute - access restricted
  
    ''' Here __salary "__" means we are making the attribute private and cannot access out 
        of class. '''
        
    def get_att(self):
        print(self.__id, self.__salary)
        
e1 = Employee("Saurabh", 235223, 40000)
print(e1.name, e1.get_att())  # It will give error

'''
Traceback (most recent call last):
  File "C:\Saurabh\Dev\Pyhton\D8_OOP\06-encapsulation.py", line 16, in <module>
    print(e1.name, e1.__id, e1.__salary)
                   ^^^^^^^
AttributeError: 'Employee' object has no attribute '__id'
'''