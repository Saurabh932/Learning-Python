'''
    When one class (child/derived) derives the properties and methods of another class (parent/base)
'''

class Car: # Parenet Class
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car started")
        
    @staticmethod
    def stop():
        print("Car stopped")
        
class Toyota(Car): # Child Class
    def __init__(self, name):
        self.name = name
        
        
car1 = Toyota("fortuner")
print(car1.start(), car1.name)
