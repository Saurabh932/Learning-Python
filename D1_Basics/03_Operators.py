# Arithmetic Operators (+, -, *, /, //, %, **)
a, b = 10, 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)  # 	Divides the left operand by the right, resulting in a floating-point number.
print(a//b) #   Divides and returns the largest integer less than or equal to the result (rounds down to the nearest whole number).
print(a%b)  #   Divides and returns the remainder
print(a**b) #`  Raises the left operand to the power of the right.


# Comparison Operators (==, !=, >, <, >=, <=)
c, d = 5, 3
print(c == d)
print(c != d)
print(c > d)
print(c < d)
print(c >= d)
print(c <= d)


# Logical Operators (and, or, not)
x, y = True, False
print(x and y)  # False
print(x or y)
print(not x)


# Assignment Operators (=, +=, -=, *=, /=)
x = 3
x += 2
print(x)

x -= 2
print(x)

x *= 2
print(x)

x /= 2
print(x)


# Membership Operators (in, not in)  -  It checks the value
print("py" in "python")
print("py" not in "python")


# Identity Operators (is, is not)   -   It checks memory location
e = [1, 2]
f = e
print(e is f)       # # True (same memory reference)
print( e is not f)


# Input / Output

name = input("Enter your name: ")
age = int(input("Enter age: "))
print(f"Hi {name}, you are {age} years old.")  # f  signifies that the string is a formatted string literal

# IQ - input() always returns a string — convert it for numeric operations.


# Type Casting - Converting one data type to another

x = "10"
y = int(x)       # str → int
z = float(y)     # int → float
s = str(z)       # float → str

# Common conversions
int()   # Converts to integer
float() # Converts to float
str()   # Converts to string
list(), tuple(), set()  # Convert between sequences
