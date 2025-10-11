# Create dictionary
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
