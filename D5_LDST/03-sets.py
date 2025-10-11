'''Unordered, mutable, no duplicates'''

# Create set
numbers = {1, 2, 3, 3, 4}
print(numbers)   # {1, 2, 3, 4}

# Add
numbers.add(5)

# Remove
numbers.discard(2)

# Operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # Union
print(a & b)   # Intersection
print(a - b)   # Difference
