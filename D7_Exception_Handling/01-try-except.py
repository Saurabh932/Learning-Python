'''
    It is use to keep the code running even when there is error.
    And also used to handle any specific type of error.
'''

try:
    num = int(input("Enter the number:"))
    a = [1, 3, 5]
    print(a[num])
    
except ValueError:
    print("Entered value is not an integer")
    
except IndexError:
    print("Invalid Index")
    
finally: #finally — runs every time, whether an exception occurs or not.
    print("Code execution completed.")