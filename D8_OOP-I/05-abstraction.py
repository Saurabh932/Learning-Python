'''
    Abstraction - Hiding the implementation details of a class and only showing the essential 
                  features to the user.
'''

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clt = False
        
    def start(self):
        self.clt = True
        self.acc = True
        print("Car started")


'''
    The below code is only visible to user and this process is called abstraction.
'''   
car1 = Car()
car1.start()