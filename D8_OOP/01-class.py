'''
    Class - it is a blueprint for creating objects
'''

class Employee:   # Class 
    language = 'py'  # Class attribute
    salary = 12000000   ## Class attribute
    
# Object Or Instance
saurabh = Employee() # Object Or Instance attribute
saurabh.name = "Saurabh"  # Object Or Instance attribute

print(saurabh.name, saurabh.language, saurabh.salary)