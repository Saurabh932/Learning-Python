'''
    We use @property decorator on any method in the class to use the method as a property
'''

class A:
    def __init__(self, math, eng, sci):
        self.math = math
        self.eng = eng
        self.sci = sci
        
    @property
    def calculate(self):
        self.percentage = str((self.math + self.eng + self.sci)/3) + "%"
        return self.percentage
        
stud1 = A(87, 55, 91)
print(stud1.calculate)

# So when we can any attribute it will be updated
stud1.eng = 65
print(stud1.calculate)