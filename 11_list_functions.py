# Python program to demonstrate list and various functions

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

# Add an element
numbers.append(60)
print("After append:", numbers)

# Insert an element
numbers.insert(2, 25)
print("After insert:", numbers)

# Remove an element
numbers.remove(25)
print("After remove:", numbers)

# Sort the list
numbers.sort()
print("After sorting:", numbers)

# Reverse the list
numbers.reverse()
print("After reverse:", numbers)

# Find length
print("Length of list:", len(numbers))

# Find maximum and minimum
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Count an element
print("Count of 20:", numbers.count(20))
