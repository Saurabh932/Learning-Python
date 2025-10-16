'''
    When one class (child/derived) derives the properties and methods of another class (parent/base)
'''

class Car: # Parenet Class
    color = "white"
    
    def __init__(self, type):
        self.type = type
        
    @staticmethod
    def start():
        print("Car started")
        
    @staticmethod
    def stop():
        print("Car stopped")
        
    
    @classmethod
    def change_color(cls, color):
        cls.color = color
        
class Toyota(Car): # Child Class
    def __init__(self, name, type):
        super().__init__(type)   # Super method
        self.name = name        
    
        
        
car1 = Toyota("fortuner", "electric")
car1.change_color("Blue")   # Using class method
print(car1.start(), car1.name, car1.type, car1.color)
