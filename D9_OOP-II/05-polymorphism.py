'''
    Polymorphism - Operator Overloading
    When the same operator is allowed to have different meaning according to the context.
'''

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def showNum(self):
        print(f"{self.real}i + {self.img}j")
        
    def add(self, comp_num2):
        newReal = self.real + comp_num2.real
        newImg = self.img + comp_num2.img
        return Complex(newReal, newImg)
    
    '''Now to use symbols "+" we can use dunder function by adding __ '''
    def __add__(self, comp_num2):
        newReal = self.real + comp_num2.real
        newImg = self.img + comp_num2.img
        return Complex(newReal, newImg)
        
        
comp_num = Complex(1, 3)
comp_num.showNum()

comp_num2 = Complex(5, 2)
comp_num2.showNum()

comp_num3 = comp_num.add(comp_num2)
comp_num3.showNum()

print("Using Duner function")

comp_num4 = comp_num + comp_num2
comp_num4.showNum()