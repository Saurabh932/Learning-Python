'''
    Print all numbers from 1 to 20, but skip multiples of 3.
'''

for i in range(1, 20):
    if i%3 == 0:
        continue
    print(i)
    


'''
    Print multiplication table of 7 using a for loop
'''

num = 7

for i in range(1, 10+1):
    print(f"{num} * {i} = ", num*i)
    


'''
    Create a while loop that keeps asking for input until the user enters "exit".
'''

# while True:
#     ip = input("Enter someting (type exit to stop): ")
    
#     if ip.lower() == 'exit':
#         print("Exiting from loop")
#         break
    
#     else:
#         print(f"You entered {ip}")



'''
    Print a right-angle triangle pattern:
        *
        **
        ***
        ****
        *****
'''

num = 4
i = 1
while i<=4:
    print("*"*i)
    
    i+=1
    
while num != 0:
    print("* " * num)
    
    num -= 1
    
