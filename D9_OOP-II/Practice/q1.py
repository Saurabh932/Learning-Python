from math import pi as p
class Circle:
    
    def __init__(self, r):
        self.r = r
        
    @property
    def area(self):
        print("Area of circle = ", p*(self.r ** 2))
    
    @property
    def perimeter(self):
        print("Premeter of circle = ", 2*p*self.r)
        
        
c1 = Circle(8)
c1.area
c1.perimeter
