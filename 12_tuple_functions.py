# Python program to demonstrate tuple and various functions

numbers = (10, 20, 30, 20, 40, 50)

print("Tuple:", numbers)

# Length of tuple
print("Length:", len(numbers))

# Count an element
print("Count of 20:", numbers.count(20))

# Find position of an element
print("Position of 30:", numbers.index(30))

# Maximum and minimum
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Sum of elements
print("Sum:", sum(numbers))
