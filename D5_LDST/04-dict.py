# Create dictionary
from pydantic import BaseModel


person = {
    "name": "Saurabh",
    "age": 24,
    "city": "Nagpur"
}

# Access
print(person["name"])

# Modify
person["age"] = 25

# Add
person["email"] = "saurabh@example.com"

# Delete
del person["city"]

# Loop through
for key, value in person.items():
    print(key, ":", value)



'''
    Important Concept
'''
class detail(BaseModel):
    name:str
    age:int
    height:str
    
def information(info:detail):
    print(info.name)
    print(info.age)
    print(info.height)
    
details = {'name':'saurabh', 'age':23, 'height':'5`10'}
print(detail(**details))