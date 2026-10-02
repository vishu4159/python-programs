# Python program to demonstrate various file modes

# Write mode
file = open("example.txt", "w")
file.write("Hello Python\n")
file.close()

# Read mode
file = open("example.txt", "r")
print("Reading file:")
print(file.read())
file.close()

# Append mode
file = open("example.txt", "a")
file.write("Welcome to file handling.")
file.close()

# Read the updated file
file = open("example.txt", "r")
print("After appending:")
print(file.read())
file.close()
