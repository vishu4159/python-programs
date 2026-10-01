# Python program to demonstrate dictionary and various functions

student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA",
    "city": "Rajkot"
}

print("Original dictionary:", student)

# Access a value
print("Student name:", student["name"])

# Add a new item
student["marks"] = 85
print("After adding marks:", student)

# Update a value
student["age"] = 21
print("After updating age:", student)

# Get keys
print("Keys:", student.keys())

# Get values
print("Values:", student.values())

# Get items
print("Items:", student.items())

# Remove an item
student.pop("city")
print("After removing city:", student)

# Find length
print("Length:", len(student))
