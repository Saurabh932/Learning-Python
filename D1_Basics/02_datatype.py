# int - Interger
a= 5 
print(type(a))  # <class 'int'>

# float - Decimal Number
b= 1.2
print(type(b))   # <class 'float'>

# -----------------------------------------------------------------------------------

# str - String
c = "Saurabh"
print(type(c))   # <class 'str'>


''' String Slicing '''
# slice = c[0:3]
# slice = c[-1]   #prints last character ie., h
# slice = c[1:5:2]    # print the char after every 2 jumps
# print(slice)


''' String Function '''
print("1. Length of string ", len(c))
print("2. Starts with and Ends with ",c.startswith("Sa"), c.endswith("bh"))
print("3. Counts: ", c.count("a"))
print("4. Captialize: ", c.capitalize())
print("5. Find word: ", c.find("u"))
print("6. Replace word: ", c.replace("bh", "v"))

# bool - Boolean value (True/False)
print(type(5>6))  # <class 'bool'>

# None - Represents no value
print(type(None)) # <class 'NoneType'>