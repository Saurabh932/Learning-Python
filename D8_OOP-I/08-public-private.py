class Student:
    __rollno = 45
    def __init__(self, name, contact):
        self.name = name
        self.__contact = contact
    
        
s1 = Student("Saurabh", 44646546546)
try:
    print(s1.name)
    print(s1.__rollno)
    print(s1.__contact)
except ValueError:
        print("The information you are accessing is confiential.")