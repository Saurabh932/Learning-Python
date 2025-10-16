'''
    del keyword is used to delete any class.
'''

class Student:
    def __init__(self, name):
        self.name = name
        
s1 = Student("Saurabh")
print(s1.name)

# Now deleting class s1
del s1
print(s1.name)