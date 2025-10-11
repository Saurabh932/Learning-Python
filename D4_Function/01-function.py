'''
    Function - it is the reusable block of code that performs specfic task.
'''

# def myname(name):
#     return name

# ip = input("Enter your name: ")
# print(myname(ip))


'''
    Eg. Find num is prime or not
'''

def prime(num):
    if num<=1:
        return False
    
    for i in range(2, num):
        if num%i == 0:
            return False
        
    return True 

num = int(input("Enter the number: "))

if prime(num) == True:
    print("It is prime")
else:
    print("Not Prime")