'''
    Q1.
'''

class student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        
    def average(self):
        avg = (self.sub1 + self.sub2 + self.sub3)//3
        print(avg)
        
avg = student("Saurabh", 98, 87, 92)
avg.average()